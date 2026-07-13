import datetime

import networkx as nx

from database.DAO import DAO

class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._idMap = {}

    def getRatings(self):
        return DAO.getRangeRatings()


    def buildGraph(self, rating1, rating2):
        self._graph.clear()
        self._idMap.clear()

        # NODI
        anno_corrente = datetime.datetime.now().year
        allNodes = DAO.getAllActors(rating1, rating2)

        for node in allNodes:
            eta_calcolata = anno_corrente - node.date_of_birth.year
            if eta_calcolata > 0:
                self._graph.add_node(node)
                self._idMap[node.id] = node

        # ARCHI
        allEdges = DAO.getAllEdges(rating1, rating2)  # <-- NON PASSIAMO idMap

        for e in allEdges:
            # e.id1 e e.id2 ora sono le stringhe (es. 'nm0000123')

            # IL MURO DI GOMMA: Entrano solo gli attori "sani"
            if e.id1 in self._idMap and e.id2 in self._idMap:
                # Prendo i veri oggetti Actor dalla mappa
                attore1 = self._idMap[e.id1]
                attore2 = self._idMap[e.id2]

                # Aggiungo l'arco passando gli oggetti e il peso
                self._graph.add_edge(attore1, attore2, weight=e.peso)

    def getGraphDetails(self):
        return len(self._graph.nodes), len(self._graph.edges)

    def getTop5(self):
        return sorted(self._graph.edges(data = True),
                      key = lambda x: x[2]['weight'], reverse = True)[:5]

    def getConnessaInfo(self):
        components = list(nx.connected_components(self._graph))
        return len(components)
