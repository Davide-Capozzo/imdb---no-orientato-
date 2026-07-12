import flet as ft

class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDDsRating(self):
        self._view._ddrating1.options.clear()
        self._view._ddrating2.options.clear()

        allRatings = self._model.getRatings()
        for rating in allRatings:
            self._view._ddrating1.options.append(ft.dropdown.Option(rating))
            self._view._ddrating2.options.append(ft.dropdown.Option(rating))

        self._view.update_page()

    def handleCreaGrafo(self, e):
        self._view.txt_result.controls.clear()

        rating1= self._view._ddrating1.value
        rating2 = self._view._ddrating2.value

        self._model.buildGraph(rating1, rating2)
        nNodi, nArchi = self._model.getGraphDetails()

        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato"))
        self._view.txt_result.controls.append(ft.Text(f"Numero di nodi: {nNodi} \nNumero di Archi: {nArchi}"))

        self._view.update_page()

    def handleCammino(self, e):
        pass