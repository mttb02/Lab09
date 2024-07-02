from database.DAO import DAO
import networkx as nx
class Model:
    def __init__(self):
        self._aereoporti = DAO.get_aereoporti()
        self._collegamenti = {}
        self._grafo = nx.DiGraph()

    def build_graph(self, distanza_min):
        self._grafo.clear()
        self._collegamenti = DAO.get_collegamenti(distanza_min)
        temp_collegamenti = {}
        for c in self._collegamenti.keys():
            _c = (c[1], c[0])
            if c not in temp_collegamenti and _c not in temp_collegamenti:
                temp_collegamenti[c] = self._collegamenti[c]
            else:
                temp_collegamenti[_c] = (temp_collegamenti[_c][0]*temp_collegamenti[_c][1]+self._collegamenti[_c][0]*self._collegamenti[c][1])/(temp_collegamenti[_c][1]+self._collegamenti[c][1])
                print(temp_collegamenti[_c])
        self._collegamenti = temp_collegamenti
        #self._grafo.add_nodes_from(self._aereoporti)
        for c in self._collegamenti.keys():
            if type(self._collegamenti[c]) is not tuple:
                self._grafo.add_edge(c[0], c[1], weight=self._collegamenti[c])
                print(type(self._collegamenti[c]))
            else:
                self._grafo.add_edge(c[0], c[1], weight=self._collegamenti[c][0])
                print("EHI")
        # temp_nodes = {}
        # for e in self._grafo.nodes:
        #     if len(self._grafo[e].items()) > 0:
        #         temp_nodes = self._grafo.remove_node(e)
        #self._grafo.

    @property
    def get_nodes(self):
        return self._grafo.nodes

    def get_edges(self):
        return self._grafo.edges
