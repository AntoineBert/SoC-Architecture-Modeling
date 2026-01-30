import unittest
from architecture import *
from comportement import *

class TestNode(unittest.TestCase):
    """
    Tests unitaires pour la class Node (noeud)
    """

    def setUp(self):
        self.node1 = Node(1,"C")
        self.node2 = Node(2,"M")

    def test_add_connection(self):
        # Test d'ajout d'une connexion entre deux noeuds
        self.node1.add_connection(self.node2, 5)
        self.assertIn(2, self.node1.connections)
        self.assertEqual(self.node1.connections[2], 5)
        self.assertIn(1, self.node2.connections)
        self.assertEqual(self.node2.connections[1], 5)

    def test_add_connection_with_self(self):
        # Test d'ajout d'une connexion avec le même noeud
        with self.assertRaises(IndexError):
            self.node1.add_connection(self.node1, 3)

    def test_add_connection_with_non_node(self):
        # Test d'ajout d'une connexion avec un objet qui n'est pas un noeud
        with self.assertRaises(TypeError):
            self.node1.add_connection("not a node", 2)

    def test_add_connection_already_exists(self):
        # Test d'ajout d'une connexion déjà existante
        self.node1.add_connection(self.node2, 5)
        with self.assertRaises(ValueError):
            self.node1.add_connection(self.node2, 2)

    def test_get_latency(self):
        # Test de récupération de la latence d'une connexion
        self.node1.add_connection(self.node2, 5)
        self.assertEqual(self.node1.get_latency(self.node2), 5)

    def test_get_latency_no_connection(self):
        # Test de récupération de la latence d'une connexion inexistante
        with self.assertRaises(ValueError):
            self.node1.get_latency(self.node2)


class TestCalculNode(unittest.TestCase):
    """
    Tests unitaires pour la classe CalculNode (noeud de calcul)
    """

    def setUp(self):
        self.node1 = CalculNode(1, 5, 3)

    def test_cache(self):
        # Test de création d'un noeud de calcul avec un cache
        self.assertEqual(self.node1.cache_size, 5)
        self.assertEqual(self.node1.computation_time, 3)
        self.assertEqual(self.node1.type, "C")
        self.assertEqual(self.node1.cache, [None]*5)

    def test_add_to_cache(self):
        # Test d'ajout d'une valeur dans le cache d'un noeud de calcul
        self.node1.cache = [1, 2, 3, 4, 5]
        self.assertEqual(self.node1.cache, [1, 2, 3, 4, 5])

    def test_add_to_cache_too_big(self):
        # Test d'ajout d'une valeur dans un cache déjà plein
        with self.assertRaises(IndexError):
            self.node1.cache = [1, 2, 3, 4, 5, 6]

    def test_delete_cache(self):
        # Test de suppression du cache d'un noeud de calcul
        self.node1.cache = [1, 2, 3, 4, 5]
        del self.node1.cache
        self.assertEqual(self.node1.cache, [None]*5)


class TestMemoryNode(unittest.TestCase):
    """
    Tests unitaires pour la classe MemoryNode (noeud de mémoire)
    """

    def setUp(self):
        # Création d'un noeud de mémoire
        self.node1 = MemoryNode(id=1, capacity=10)

    def test_capacity(self):
        # Teste que la capacité ne peut être définie nulle
        with self.assertRaises(ValueError):
            self.node2 = MemoryNode(id=99,capacity=0)


    def test_memory(self):
        # Teste que la capacité, le type et le contenu initial du noeud sont corrects
        self.assertEqual(self.node1.capacity, 10)
        self.assertEqual(self.node1.type, "M")
        self.assertEqual(self.node1.memory, [None]*10)

    def test_add_data(self):
        # Ajout d'une liste de valeurs dans une plage de mémoire
        self.node1.add_data([1, 2, 3, 4, 5])
        # Vérification que la plage de mémoire modifiée contient les bonnes valeurs
        self.assertEqual(self.node1.memory, [1, 2, 3, 4, 5]+[None]*5)
        self.assertEqual(self.node1.protected_range, (0,4))

    def test_add_memory_too_big(self):
        # Vérification qu'une erreur est levée lorsqu'on tente d'ajouter une liste de valeurs plus grande que la capacité du noeud
        with self.assertRaises(ValueError):
            self.node1.add_data([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

    def test_delete_memory(self):
        # On vérifie que le décorateur fonctionne bien pour supprimer la mémoire
        del self.node1.memory
        self.assertEqual(self.node1.memory, [None] * self.node1.capacity)
        self.assertEqual(self.node1.protected_range, None)


class TestNoC(unittest.TestCase):
    """
    Tests unitaires pour la classe NoC
    """
    def setUp(self):
        # Création d'un NoC
        self.noc = NoC()

        # Création de noeuds
        self.node1 = CalculNode(id=1, cache_size=16, computation_time=1)
        self.node2 = CalculNode(id=2, cache_size=8, computation_time=2)
        self.node3 = MemoryNode(id=3, capacity=128)

        # On ajoute ces noeuds au NoC
        self.noc.add_node(self.node1)
        self.noc.add_node(self.node2)
        self.noc.add_node(self.node3)

        # On ajoute des connexions entre ces noeuds
        self.noc.add_connection(1, 2, 10)
        self.noc.add_connection(2, 3, 20)

    def test_add_node(self):
        # Test d'ajout d'un nouveau noeud de calcul
        node4 = CalculNode(id=4, cache_size=32, computation_time=3)
        self.noc.add_node(node4)
        self.assertEqual(len(self.noc.calcul_nodes), 3)
        self.assertEqual(self.noc.size, 4)

        # Test d'ajout d'un nouveau noeud de mémoire
        node5 = MemoryNode(id=5, capacity=256)
        self.noc.add_node(node5)
        self.assertEqual(len(self.noc.memory_nodes), 2)
        self.assertEqual(self.noc.size, 5)

        # Test d'ajout d'un noeud avec un id déjà existant
        with self.assertRaises(KeyError):
            self.noc.add_node(MemoryNode(id=1, capacity=64))

    def test_get_node_type(self):
        # Test pour un noeud de calcul
        self.assertEqual(self.noc.get_node(1).type, "C")

        # Test pour un noeud de mémoire
        self.assertEqual(self.noc.get_node(3).type, "M")

        # Test pour un noeud inexistant
        with self.assertRaises(KeyError):
            self.noc.get_node(6).type

    def test_get_node(self):
        # Test pour un noeud de calcul
        self.assertEqual(self.noc.get_node(1), self.node1)

        # Test pour un noeud de mémoire
        self.assertEqual(self.noc.get_node(3), self.node3)

        # Test pour un noeud inexistant
        with self.assertRaises(KeyError):
            self.noc.get_node(6)

    def test_remove_node(self):
        # Test de suppression d'un noeud de calcul
        self.noc.remove_node(1)
        self.assertEqual(len(self.noc.calcul_nodes), 1)
        self.assertEqual(self.noc.size, 2)

        # Test de suppression d'un noeud de mémoire
        self.noc.remove_node(3)
        self.assertEqual(len(self.noc.memory_nodes), 0)
        self.assertEqual(self.noc.size, 1)

        # Test de suppression d'un noeud inexistant
        with self.assertRaises(KeyError):
            self.noc.remove_node(6)

    def test_are_nodes_connected(self):
        # Test avec deux noeuds connectés directement
        self.assertTrue(self.noc.are_nodes_connected(1, 2))

        # Test avec des noeuds qui ne sont pas connectés
        self.assertFalse(self.noc.are_nodes_connected(1, 5))

        # Test avec un noeud qui n'existe pas
        self.assertFalse(self.noc.are_nodes_connected(1, 69))

    def test_shortest_path(self):
        self.noc = NoC()
        self.noc.add_node(MemoryNode(1, capacity=64))
        self.noc.add_node(MemoryNode(2, capacity=64))
        self.noc.add_node(CalculNode(3, cache_size = 10, computation_time=3))
        self.noc.add_node(CalculNode(4, cache_size = 10, computation_time=2))
        self.noc.add_node(CalculNode(5, cache_size = 10, computation_time=4))

        self.noc.add_connection(1, 3, 1)
        self.noc.add_connection(1, 4, 5)
        self.noc.add_connection(3, 2, 2)
        self.noc.add_connection(3, 5, 4)
        self.noc.add_connection(4, 2, 3)
        self.noc.add_connection(4, 5, 2)

        # Test avec deux noeuds connectés directement
        path, weight = self.noc.shortest_path(1, 3)
        self.assertEqual(path, [1, 3])
        self.assertEqual(weight, 4) # le poids vaut 1 (latence de connection entre 1 et 3) + 3 (temps de calcul du noeud 3)

        # Test avec deux noeuds connectés indirectement
        path, weight = self.noc.shortest_path(1, 2)
        self.assertEqual(path, [1, 3, 2])
        self.assertEqual(weight, 6)

        # Test avec un noeud qui n'existe pas
        with self.assertRaises(KeyError):
            path, weight = self.noc.shortest_path(1, 40)

        # Test avec le même noeud en départ et arrivée
        path, weight = self.noc.shortest_path(1, 1)
        self.assertEqual(path, [1])
        self.assertEqual(weight, 0)

        # Test avec des connexions en boucle
        node4 = MemoryNode(6, capacity=64)
        node5 = MemoryNode(7, capacity=64)
        self.noc.add_node(node4)
        self.noc.add_node(node5)
        self.noc.add_connection(1, 6, 15)
        self.noc.add_connection(6, 7, 5)
        path, weight = self.noc.shortest_path(1, 7)
        self.assertEqual(path, [1, 6, 7])
        self.assertEqual(weight, 20)

        # Test entre des noeuds non connectés
        node6 = MemoryNode(8, capacity=64)
        self.noc.add_node(node6)
        path, weight = self.noc.shortest_path(1, 8)
        self.assertEqual(path, None)
        self.assertEqual(weight, float('inf'))





class TestTaskAndRequest(unittest.TestCase):
    """
    Tests unitaires pour le volet comportemental, sur les classes Task et Request
    """

    def setUp(self):
        self.noc=NoC()

    def test_request_creation(self):
        # Test la création d'une requête et vérifie ses attributs
        req = Request(1, 2, data="test_data", priority=0)
        self.assertEqual(req.source, 1)
        self.assertEqual(req.destination, 2)
        self.assertEqual(req.data, "test_data")
        self.assertEqual(req.priority, 0)

    def test_task_creation(self):
        # Test la création d'une tâche et vérifie si elle est vide
        task = Task()
        self.assertEqual(len(task),0)

    def test_enqueue(self):
        # Test l'ajout et la suppression de requêtes dans une tâche
        task = Task()
        req1 = Request(1, 2, data="req1", priority=0)
        req2 = Request(2, 3, data="req2", priority=1)
        task.enqueue_request(req1)
        task.enqueue_request(req2)
        self.assertNotEqual(len(task),0)
        self.assertEqual(task[0], req1)
        self.assertEqual(task[1], req2)

    def test_clear(self):
        # Test la suppression de toutes les requêtes d'une tâche
        task = Task()
        req1 = Request(1, 2, data="req1", priority=0)
        req2 = Request(2, 3, data="req2", priority=1)
        task.enqueue_request(req1)
        task.enqueue_request(req2)
        task.clear()
        self.assertEqual(len(task),0)

    def test_str_representation(self):
        # Test la représentation sous forme de chaîne de caractères d'une tâche
        task = Task()
        req1 = Request(1, 2, data="req1", priority=0)
        req2 = Request(2, 3, data="req2", priority=1)
        task.enqueue_request(req1)
        task.enqueue_request(req2)
        expected_str = "Task: {\n  0: Request(source=1, destination=2, data=req1, priority=0)\n  1: Request(source=2, destination=3, data=req2, priority=1)\n}"
        self.assertEqual(str(task), expected_str)

    def test_exec(self):
        start_node = CalculNode(id=2, cache_size=8, computation_time=2)
        end_node = MemoryNode(id=3, capacity=128) # Ces deux noeuds ont été testés précédemment

        # Ajouter les noeuds au NoC
        self.noc.add_node(start_node)
        self.noc.add_node(end_node)

        # Créer une Task
        task = Task(3, 2, [99])
        task.enqueue_request(Request(3, 2, [99]))

        # Executer la Task
        task.exec(self.noc)

        # Vérifier que les données ont bien été ajoutées aux noeuds appropriés
        self.assertTrue(99 in start_node.cache)
        self.assertTrue(99 in end_node.memory)



if __name__ == '__main__':
    unittest.main()

