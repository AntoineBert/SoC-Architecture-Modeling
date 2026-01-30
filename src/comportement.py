import copy

class Task(dict):
    """
    Objet contenant les requêtes dans un dictionnaire rangées par ordre de priorité
    """
    def __init__(self, start_node_id=None, end_node_id=None, data=[]):
        """
        Crée un dictionnaire vide de requêtes. Les requêtes représentent le chemin le plus court pour transférer
        certaines données d'un nœud de départ à un nœud d'arrivée dans un certain réseau noc (Network on Chip).
        """
        super().__init__()
        self.time = None
        self.start_node_id = start_node_id
        self.end_node_id = end_node_id
        self.data = data

    def fill(self, noc):
        """
        Permet de remplir l'objet Task avec des requêtes. On séquence la tâche en plusieurs requêtes.
        """

        # On crée une copie du NoC que l'on modifie de sorte à ce qu'il ne comporte que des nœuds ayant assez de
        # cache ou mémoire libre pour stocker la data.
        noc_tmp = copy.deepcopy(noc)

        all_nodes = list(noc_tmp.memory_nodes.values()) + list(noc_tmp.calcul_nodes.values())

        for node in all_nodes:
            if node.remaining_space() < len(self.data):
                if node.id == self.start_node_id or node.id == self.end_node_id:
                    raise ValueError("Le nœud de départ ou le nœud d'arrivé n'a pas assez d'espace libre pour stocker la donnée saisie.")
                else:
                    print(f"Le noeud {node.id} n'a pas assez d'espace libre pour stocker la donnée saisie.")
                    noc_tmp.remove_node(node.id)

        path, time = noc_tmp.shortest_path(self.start_node_id, self.end_node_id)
        self.time = time
        if path != None:
            for i in range(len(path) - 1):
                request = Request(path[i], path[i + 1], self.data)
                self.enqueue_request(request)
        else:
            self.time = None
            self.clear()
            raise IndexError("Il n'y a pas de chemin permettant de réaliser cette requête.")

    def enqueue_request(self, request, priority=None):
        """
        Ajoute une requête au bout d'une tâche et modifie la priorité de la requête.

        :param request: requête à ajouter
        :param priority: priorité à laquelle ajouter la requête (None pour ajouter à la fin)
        :return: None
        """
        if priority is None:
            priority = len(self)

        if priority in self:
            for p in range(len(self), priority, -1):
                self[p] = self[p - 1]
                self[p].priority = p

        request.priority = priority
        self[priority] = request

    def exec(self, noc):
        """
        Permet d'exécuter la tâche, c'est-à-dire transférer les données de la tâche de son point de départ à son
        point d'arrivée via les nœuds du réseau NoC (Network on Chip). Elle suit la séquence de requêtes ajoutées
        à la tâche par la méthode fill.
        """
        node = noc.get_node(self.start_node_id)
        node.add_data(self.data)
        for request in self.values():
            node = noc.get_node(request.destination)
            node.add_data(self.data)

    def get_requests_for_node(self, node_id):
        """
        Obtient la liste des requêtes pour un nœud spécifique.

        :param node_id: l'ID du nœud spécifique
        :return: la liste des requêtes pour ce nœud
        """
        requests_for_node = []
        for priority in self:
            request = self[priority]
            if request.source == node_id or request.destination == node_id:
                requests_for_node.append(request)
        return requests_for_node

    def clear(self):
        """
        Supprime toutes les requêtes de la tâche.

        :return: None
        """
        super().clear()
        self.time = None

    def __str__(self):
        """
        Retourne une représentation lisible de l'objet Task.

        :return: une chaîne de caractères représentant l'objet Task
        """
        task_representation = "Task: {"
        for priority in sorted(self.keys()):
            request = self[priority]
            task_representation += f"\n  {priority}: {str(request)}"
        task_representation += "\n}"
        return task_representation


class Request:
    """
    Une requête possède un nœud d'origine, un nœud de destination, de la donnée et une priorité.
    """
    def __init__(self, source, destination, data=None, priority=0):
        """
        Crée une requête.

        :param source: noeud source de la requête
        :param destination: noeud destination de la requête
        :param data: donnée concernée par la requête
        :param priority: priorité de la requête (0 est la plus haute priorité)
        :return None
        """
        self.source = source
        self.destination = destination
        self.data = data
        self.priority = priority

    def __str__(self):
        """
        Retourne une représentation lisible de l'objet Request.

        :return: une chaîne de caractères représentant l'objet Request
        """
        return f"Request(source={self.source}, destination={self.destination}, data={self.data}, priority={self.priority})"
