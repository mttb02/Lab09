import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleAnalizza(self,e):
        _distanza_min = self._view._txtIn.value
        try:
            distanza_min = float(_distanza_min)
            self._view._txt_result.controls.clear()
            self._model.build_graph(distanza_min)
            nodes = self._model.get_nodes()
            edges = self._model.get_edges()
            self._view._txt_result.controls.clear()
            self._view._txt_result.controls.append(ft.Text(f"Il grafo ha {len(nodes)} vertici."))
            self._view._txt_result.controls.append(ft.Text(f"Il grafo ha {len(edges)} archi."))
            for e in edges.keys():
                self._view._txt_result.controls.append(ft.Text(f"{e}: {edges[e]["weight"]}"))
            self._view.update_page()

        except ValueError:
            self._view._txt_result.controls.append(ft.Text("Inserire una distanza minima in miglia"))
            self._view.update_page()
