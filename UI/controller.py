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
        pass

    def handleCammino(self, e):
        pass