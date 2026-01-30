import networkx as nx
import random


class SoC:
    """
    La classe SoC (System on Chip) est un dictionnaire de NoC
    """
    def __init__(self):
        """
        Crée un objet de type SoC contenant un dictionnaire vide dans lequel seront stockés les NoC.
        """
        self.NoC = {}
        self.size = 0  # nombre de NoC que contient le SoC


class NoC:
    """
    La classe NoC (Network on Chip) est un dictionnaire de nœuds de mémoire et un dictionnaire de nœuds de calcul.
    """
    def __init__(self):
        """
        Crée un objet de type NoC contenant un dictionnaire vide de nœuds de mémoire et un dictionnaire vide de nœuds
        de calcul.
        """
        self.memory_nodes = {}
        self.calcul_nodes = {}
        self.size = 0  # nombre de nœuds que contient le NoC

    def to_networkx_graph(self):
        """
        Transforme le NoC en un graphe NetworkX.

        :return: Graphe NetworkX représentant le NoC
        """
        graph = nx.Graph() # On crée un graphe

        # On ajoute les nœuds de mémoire au graphe
        for node in self.memory_nodes.values():
            graph.add_node(node.id, type="M", size=node.capacity)

        # On ajoute les nœuds de calcul au graphe
        for node in self.calcul_nodes.values():
            graph.add_node(node.id, type="C", size=node.cache_size)

        # On ajoute les connexions entre les nœuds de mémoire et de calcul au graphe
        for node in self.memory_nodes.values():
            for neighbor_id, latency in node.connections.items():
                if neighbor_id != node.id:  # Exclure les connexions du nœud avec lui-même
                    graph.add_edge(node.id, neighbor_id, weight=latency)

        for node in self.calcul_nodes.values():
            for neighbor_id, latency in node.connections.items():
                if neighbor_id != node.id:  # Exclure les connexions avec le nœud lui-même
                    graph.add_edge(node.id, neighbor_id, weight=latency)

        return graph

    def add_node(self, node):
        """
        Ajoute un nœud au SoC.

        : param node: nœud à ajouter au SoC
        : return: None
        """
        if node.id in self.memory_nodes or node.id in self.calcul_nodes:
            # L'identifiant est unique (même un nœud de mémoire et un nœud calcul ne peuvent avoir le même id).
            raise KeyError(f"Un nœud de mémoire avec l'ID {node.id} existe déjà dans le NoC.")

        if node.type == "M":
            self.memory_nodes[node.id] = node
        else:
            self.calcul_nodes[node.id] = node
        self.size += 1

    def get_node(self, node_id):
        """
        Renvoie le nœud correspondant à l'identifiant donné.

        :param node_id: Identifiant du nœud recherché
        :return: Nœud correspondant à l'identifiant donné en argument
        """
        if node_id in self.memory_nodes:
            return self.memory_nodes[node_id]
        elif node_id in self.calcul_nodes:
            return self.calcul_nodes[node_id]
        else:
            raise KeyError(f"Le nœud avec l'ID {node_id} n'existe pas dans le NoC.")

    def remove_node(self, node_id):
        """
        Supprime un nœud du NoC.

        :param node_id: identifiant du nœud à supprimer
        :return: None
        """
        try:
            node_type = self.get_node(node_id).type
        except KeyError as e:
            raise KeyError(f"Le nœud avec l'ID {node_id} n'existe pas. Erreur: {e}")

        if node_type == "M":
            if node_id in self.memory_nodes:
                del self.memory_nodes[node_id]
            else:
                raise KeyError("Le nœud de mémoire n'existe pas.")
        else:
            if node_id in self.calcul_nodes:
                del self.calcul_nodes[node_id]
            else:
                raise KeyError("Le nœud de calcul n'existe pas.")

        # Supprimer les connexions au nœud supprimé
        for node in self.memory_nodes.values():
            if node_id in node.connections:
                del node.connections[node_id]

        for node in self.calcul_nodes.values():
            if node_id in node.connections:
                del node.connections[node_id]

        self.size -= 1

    def shortest_path(self, start_node_id, end_node_id, visited=None, current_path=None, current_weight=0):
        """
        Trouve le chemin le plus court en se basant sur l'algorithme de Dijkstra.
        Renvoie le chemin le plus court s'il existe et son poids total (en terme de latence et de temps de calcul).

        :param start_node_id: nœud de départ
        :param end_node_id: nœud de destination
        :param visited: liste des nœuds visités (utile pour la récursivité)
        :param current_path: chemin actuel (utile pour la récursivité)
        :param current_weight: poids total du chemin actuel (utile pour la récursivité)
        :return: (shortest, min_weight)
        """
        if visited is None:
            visited = []  # Ensemble des nœuds visités
        if current_path is None:
            current_path = []  # Liste des nœuds dans le chemin en cours

        # Vérifier si les nœuds de départ et d'arrivée existent
        if not self.get_node(start_node_id) or not self.get_node(end_node_id):
            raise ValueError("Le nœud de départ ou d'arrivée n'existe pas dans le NoC.")

        # Ajouter le nœud de départ à l'ensemble des nœuds visités et au chemin en cours
        visited.append(start_node_id)
        current_path.append(start_node_id)

        start_node = self.get_node(start_node_id)
        if start_node.type == 'C':
            current_weight += start_node.computation_time

        if start_node_id == end_node_id:
            # Si le nœud de départ est le nœud de destination, retourner le chemin en cours et son poids total
            return current_path, current_weight

        shortest = None  # Variable pour stocker le chemin le plus court
        min_weight = float('inf')  # Variable pour stocker le poids du chemin le plus court

        # Parcourir les voisins du nœud de départ
        neighbors = list(self.get_node(start_node_id).connections.items())
        index = 0
        while index < len(neighbors):
            neighbor_id, latency = neighbors[index]
            if neighbor_id not in visited:
                # Si le voisin n'a pas été visité, appeler récursivement la fonction 'shortest_path'
                path, weight = self.shortest_path(neighbor_id, end_node_id, visited.copy(), current_path.copy(), current_weight + latency)
                if path:  # Si un chemin a été trouvé
                    if weight < min_weight:
                        # Si le poids du chemin trouvé est inférieur au poids minimal actuel,
                        # mettre à jour les variables 'shortest' et 'min_weight'
                        shortest = path
                        min_weight = weight
            index += 1

        return shortest, min_weight

    def are_nodes_connected(self, node_id1, node_id2):
        """
        Vérifie si deux nœuds sont connectés directement.

        :param node_id1: identifiant du nœud 1
        :param node_id2: identifiant du nœud 2
        :return: True s'ils sont connectés, False sinon
        """
        try:
            node1, node2 = self.get_node(node_id1), self.get_node(node_id2)
        except KeyError:
            # Si l'un des nœuds n'existe pas dans le NoC, les nœuds ne sont pas connectés
            return False

        # Vérifier si les deux nœuds ont une connexion entre eux
        return node_id2 in node1.connections

    def add_connection(self, node_id1, node_id2, latency):
        """
        Ajoute une connexion entre deux nœuds.

        :param node_id1: identifiant du premier nœud
        :param node_id2: identifiant du deuxième nœud
        :param latency: latence de la connexion (vitesse de transmission des données entre les nœuds)
        :return: None
        """
        node1 = self.get_node(node_id1)
        node2 = self.get_node(node_id2)

        if node_id2 not in node1.connections and node_id1 not in node2.connections:
            node1.add_connection(node2, latency)
        else:
            raise ValueError(f"Une connexion existe déjà entre les nœuds {node_id1} et {node_id2}.")

    def remove_connection(self, node_id_1, node_id_2):
        """
        Supprime la connexion entre deux nœuds dans le NoC.

        :param node_id_1: identifiant du premier nœud
        :param node_id_2: identifiant du deuxième nœud
        :return: None
        """
        try:
            node_1 = self.get_node(node_id_1)
            node_2 = self.get_node(node_id_2)
        except KeyError as e:
            raise KeyError(f"Un des nœuds avec l'ID {node_id_1} ou {node_id_2} n'existe pas. Erreur: {e}")

        if node_id_2 not in node_1.connections or node_id_1 not in node_2.connections:
            raise ValueError(f"Les nœuds {node_id_1} et {node_id_2} ne sont pas connectés.")

        del node_1.connections[node_id_2]
        del node_2.connections[node_id_1]

    def clear(self):
        """
        Supprime tous les nœuds et les connexions du NoC.

        :return: None
        """
        self.memory_nodes.clear()
        self.calcul_nodes.clear()
        self.size = 0

        for node in self.memory_nodes.values():
            node.connections.clear()

        for node in self.calcul_nodes.values():
            node.connections.clear()

    def clean(self):
        """
        Supprime toutes les données stockées dans les mémoires des nœuds du NoC.
        :return: None
        """
        all_nodes = list(self.memory_nodes.values()) + list(self.calcul_nodes.values())
        for node in all_nodes:
            if node.type == 'M':
                del node.memory
            else:
                del node.cache

    def random(self,
               size=30,
               prop=0.5,
               minMemorySize=100,
               maxMemorySize=1000,
               minCacheSize=100,
               maxCacheSize=100,
               minComputationTime=5,
               maxComputationTime=10):
        """
        Permet de générer des nœuds de façon aléatoires au sein du NoC.
        :param size: Nombre de nœuds souhaité
        :param prop: Proportion de nœuds de mémoire souhaitée
        :return:
        """
        # On supprime tous les nœuds du NoC.
        self.clear()

        # La proportion de nœuds de mémoire doit être comprise entre 0 et 1.
        if prop>1 or prop<0:
            raise ValueError("Veuillez choisir une proportion de nœuds de mémoire comprise entre 0 et 1.")

        # Création des nœuds avec des valeurs aléatoires
        for i in range(size):
            memory_size = random.randint(minMemorySize, maxMemorySize)
            cache_size = random.randint(minCacheSize, maxCacheSize)
            computation_time = random.randint(minComputationTime, maxComputationTime)

            if i % 1/prop == 0:
                node = MemoryNode(i, memory_size)
            else:
                node = CalculNode(i, cache_size, computation_time)

            self.add_node(node)

        # Création des connexions entre les nœuds avec des valeurs aléatoires
        all_nodes = list(self.memory_nodes.values()) + list(self.calcul_nodes.values())

        for i in range(len(all_nodes)):
            for j in range(i + 1, len(all_nodes)):
                node1 = all_nodes[i]
                node2 = all_nodes[j]
                if node1 != node2 and not self.are_nodes_connected(node1, node2):
                    latency = random.randint(5, 10)
                    rnd = random.randint(0, 10)
                    if node1.connections == {node1.id: 0} or node2.connections == {node2.id: 0} or rnd > 5:
                        node1.add_connection(node2, latency)

    def new_random(self, nb_cac=5, nb_mem=5, rnd=10, **kwargs):
        #Valeurs par défaut des caractéristiques du noc
        (a, b) = (5, 10)
        (c, d) = (100, 1000)
        (e, f) = (100, 1000)
        (g, h) = (5, 10)
        for key, value in kwargs.items():
            if key == "latency":
                (a, b) = value
            if key == "cache":
                (c, d) = value
            if key == "memory":
                (e, f) = value
            if key == "computation_time":
                (g, h) = value
        self.clear()

        # Création des noeuds de calcul avec des valeurs aléatoires
        for i in range(nb_cac):
            cache_size = random.randint(c, d)
            computation_time = random.randint(g, h)
            node = CalculNode(i, cache_size, computation_time)
            self.add_node(node)
        # Création des noeuds de mémoire
        for j in range(nb_mem):
            memory_size = random.randint(e, f)
            node = MemoryNode(nb_cac+j, memory_size)
            self.add_node(node)

        # Création des connexions entre les noeuds avec des valeurs aléatoires
        if rnd == 0: return # Si la chance est de 1/0, on ne lie pas les noeuds
        all_nodes = list(self.memory_nodes.values()) + list(self.calcul_nodes.values())
        for i in range(len(all_nodes)):
            for j in range(i + 1, len(all_nodes)):
                node1 = all_nodes[i]
                node2 = all_nodes[j]
                if node1 != node2 and not self.are_nodes_connected(node1, node2):
                    latency = random.randint(a, b)
                    rand = random.randint(0, 10)
                    if node1.connections == {node1.id: 0} or node2.connections == {node2.id: 0} or rand > rnd:
                        node1.add_connection(node2, latency)


class Node:
    """
    Classe décrivant les relations entre les nœuds
    """
    def __init__(self, id, type):
        """
        Crée un nœud avec un dictionnaire vide contenant les nœuds ayant une connexion avec lui-même.

        :param id: Identifiant du nœud
        """
        self.id = id
        self.connections = {id: 0}
        self.type = type

    def add_connection(self, other, latency):
        """
        Ajoute une connexion avec un autre nœud en précisant la latence (vitesse à laquelle circule les informations entre ceux-ci).

        :param other: Noeud connecté
        :param latency: temps de transmission de l'information
        :return: None
        """
        if not isinstance(other, Node):
            raise TypeError("L'argument 'other' doit être une instance de la classe Node.")

        if self.id != other.id:
            if other.id in self.connections:
                raise ValueError(f"Une connexion existe déjà entre les nœuds {self.id} et {other.id}.")
            self.connections[other.id] = latency
            other.connections[self.id] = latency
        else:
            raise IndexError("On ne peut pas ajouter une liaison entre un nœud et lui-même.")

    def get_latency(self, other):
        """
        Renvoie la latence de connexion entre deux nœuds ou une erreur s'ils ne sont pas connectés.

        :param other: Noeud connecté
        :return: Latence de la connexion entre les deux nœuds
        """
        if other.id in self.connections:
            return self.connections[other.id]
        else:
            raise ValueError("Pas de connexion trouvée avec le nœud saisi.")

    def add_data(self, data):
        """
        Ajoute des données à un nœud.

        :param data: Données à ajouter au nœud
        :return: None
        """
        if self.type == 'C':
            self.cache = data
        if self.type == 'M':
            self.memory = data

    def remaining_space(self):
        """
        Permet d'obtenir l'espace libre dans la mémoire d'un nœud.

        :return: Espace disponible dans la mémoire du nœud
        """
        if self.type == 'C':
            return self.cache_size
        if self.type == 'M':
            if self.protected_range == None:
                return self.capacity
            else:
                return self.capacity - self.protected_range[1] - 1

    def use(self):
        """
        Cette méthode permet d'obtenir le taux d'utilisation de la mémoire d'un nœud (en pourcentage).

        :return: Le taux d'utilisation du nœud (en pourcentage).
        """

        # Si le noeud est un noeud de calcul, alors il faut calculer le taux d'utilisation du cache.
        if self.type == 'C':
            # Compteur initialisé à zéro
            k = 0
            # Parcourt le cache
            for i, element in enumerate(self.cache):
                # Si l'élément dans le cache n'est pas None, c'est-à-dire s'il y a des données,
                # alors on incrémente le compteur.
                if element is not None:
                    k += 1
            # Le taux d'utilisation est calculé comme le ratio entre le nombre d'emplacements utilisés (k)
            # et la taille totale du cache (self.cache_size), le tout multiplié par 100 pour obtenir un pourcentage.
            return (k / self.cache_size) * 100
        else:
            # Si le noeud est un noeud de mémorie, le taux d'utilisation est déterminé par la plage protégée (mémoire utilisée).
            if self.protected_range == None:
                # Si aucune plage n'est protégée, le taux d'utilisation est de 0%
                return 0
            else:
                # Sinon, le taux d'utilisation est calculé comme le ratio la taille de la plage protégée
                # (self.protected_range[1] + 1) et la capacité totale du nœud (self.capacity), le tout multiplié par 100.
                return ((self.protected_range[1] + 1) / self.capacity) * 100


class CalculNode(Node):
    """
    Classe décrivant la structure des nœuds de calcul
    """
    def __init__(self, id, cache_size, computation_time):
        """
        Crée un nœud de calcul.

        :param id: Identifiant du nœud
        :param cache_size: taille du cache
        :param computation_time: temps de calcul
        """
        super().__init__(id, "C")
        self._cache = [None]*cache_size
        self.computation_time = computation_time
        if cache_size<=0:
            raise ValueError("La taille du cache doit être un entier naturel non nul.")
        self.cache_size = cache_size


    @property
    def cache(self):
        """
        Accès au cache du nœud de calcul.

        :return: le cache du nœud de calcul
        """
        return self._cache

    @cache.setter
    def cache(self, data):
        """
        Cette méthode ajoute des données dans le cache du nœud.

        :param data: Les données à ajouter.
        :return: None, sauf si la taille des données est supérieure à la taille du cache, auquel cas une exception est levée.
        """

        # Calcule la taille des données à ajouter
        data_size = len(data)

        # Initialise le point de départ pour l'ajout des données dans le cache
        start = 0

        # Parcourt le cache pour trouver le premier emplacement vide (None)
        for i, element in enumerate(self.cache):
            if element is None:
                # Une fois trouvé, le point de départ est défini et la boucle est interrompue
                start = i
                break

        # Vérifie si la taille des données à ajouter est plus grande que la taille totale du cache
        if data_size > self.cache_size:
            # Si c'est le cas, une exception est levée
            raise IndexError("La taille de cache est trop petite par rapport à la taille de la donnée")

        # Vérifie si la taille des données à ajouter est plus grande que l'espace restant dans le cache
        if data_size > self.cache_size - start:
            # Si c'est le cas, remplir le cache jusqu'à sa fin avec les premières données
            self.cache[start:] = data[:self.cache_size - start]
            # Ajoute les données restantes au début du cache, écrasant les données existantes
            remaining_data = data[self.cache_size - start:]
            self.cache[:len(remaining_data)] = remaining_data
        else:
            # Si la taille des données est inférieure à l'espace disponible dans le cache, ajoute simplement les données
            self.cache[start:data_size + start] = data


    @cache.deleter
    def cache(self):
        """
        Supprime les données du cache.

        :return: None
        """
        self._cache = [None] * self.cache_size


class MemoryNode(Node):
    """
    Classe décrivant la structure des nœuds de mémoire
    """
    def __init__(self, id, capacity):
        """
        Crée un nœud de mémoire.

        :param id: Identifiant du nœud
        :param capacity: taille de la mémoire
        """
        super().__init__(id, "M")
        self._memory = [None]*capacity
        if type(capacity)==int and capacity > 0:
            self.capacity = capacity
        else:
            raise ValueError("La capacité d'un noeud de mémoire doit être un entier naturel non nul.")
        self.protected_range = None

    @property
    def memory(self):
        """
        Accès à la mémoire du nœud.

        : return: Mémoire contenue dans le nœud de mémoire
        """
        return self._memory

    @memory.setter
    def memory(self, data):
        """
        Ajoute des données dans la mémoire.

        :param data : Informations à mettre en mémoire
        :return : None / Erreur si la plage d'adresse est différente à la taille de la mémoire
        """

        data_size = len(data)
        if self.protected_range == None:
            start = 0
        else:
            start = self.protected_range[1]+1
        if data_size > self.capacity - start:
            raise ValueError("La donnée est trop lourde pour être stockée dans ce nœud de mémoire.")
        else:
            self.memory[start:data_size+start] = data
            self.protected_range = (0, start+data_size-1)

    @memory.deleter
    def memory(self):
        """
        Supprime toutes les données de la mémoire. Supprime les plages protégées.
        :return: None
        """
        self._memory = [None] * self.capacity
        self.protected_range = None