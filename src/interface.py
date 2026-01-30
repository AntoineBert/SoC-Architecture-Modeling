# -*- coding: utf-8 -*-

# Created by: PyQt5 UI code generator 5.14.0


import copy
import sys
import pickle
import io
import datetime
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QPushButton, QFileDialog, QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices, QTextDocument
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import networkx as nx
from architecture import *
from comportement import *
import random

import warnings
from matplotlib import MatplotlibDeprecationWarning

warnings.filterwarnings("ignore", category=MatplotlibDeprecationWarning) #On ignore les avertissements de dépréciation

class Ui_fig_size(object):
    def setupUi(self, fig_size):
        fig_size.setObjectName("fig_size")
        fig_size.resize(414, 192)
        fig_size.setStyleSheet("background-color: rgb(60, 63, 65);")
        self.buttonBox = QtWidgets.QDialogButtonBox(fig_size)
        self.buttonBox.setGeometry(QtCore.QRect(130, 150, 193, 28))
        self.buttonBox.setStyleSheet("background-color: rgb(77, 77, 77);\n"
"color: rgb(255, 255, 255);")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label_8 = QtWidgets.QLabel(fig_size)
        self.label_8.setGeometry(QtCore.QRect(-60, 70, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(fig_size)
        self.label_9.setGeometry(QtCore.QRect(-60, 100, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")
        self.label_11 = QtWidgets.QLabel(fig_size)
        self.label_11.setGeometry(QtCore.QRect(80, 20, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_11.setObjectName("label_11")
        self.height = QtWidgets.QSpinBox(fig_size)
        self.height.setGeometry(QtCore.QRect(230, 100, 61, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.height.setFont(font)
        self.height.setStyleSheet("color: rgb(255, 255, 255);")
        self.height.setObjectName("height")
        self.width = QtWidgets.QSpinBox(fig_size)
        self.width.setGeometry(QtCore.QRect(230, 70, 61, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.width.setFont(font)
        self.width.setStyleSheet("color: rgb(255, 255, 255);")
        self.width.setObjectName("width")

        self.retranslateUi(fig_size)
        self.buttonBox.accepted.connect(self.fig_size_)
        self.buttonBox.accepted.connect(fig_size.accept)
        self.buttonBox.rejected.connect(fig_size.reject)
        QtCore.QMetaObject.connectSlotsByName(fig_size)

    def retranslateUi(self, fig_size):
        _translate = QtCore.QCoreApplication.translate
        fig_size.setWindowTitle(_translate("fig_size", "Dialog"))
        self.label_8.setText(_translate("fig_size", "<html><head/><body><p align=\"right\">Largeur :</p></body></html>"))
        self.label_9.setText(_translate("fig_size", "<html><head/><body><p align=\"right\">Hauteur :</p></body></html>"))
        self.label_11.setText(_translate("fig_size", "<html><head/><body><p align=\"center\">Modifier la taille du graphe</p></body></html>"))

    def fig_size_(self):
        global figsize
        figsize = (self.width.value(), self.height.value())


class Ui_info(object):
    def setupUi(self, info):
        info.setObjectName("info")
        info.resize(526, 361)
        info.setStyleSheet("background-color: rgb(60, 63, 65);")
        self.buttonBox = QtWidgets.QDialogButtonBox(info)
        self.buttonBox.setGeometry(QtCore.QRect(170, 320, 193, 28))
        self.buttonBox.setStyleSheet("background-color: rgb(77, 77, 77);\n"
"color: rgb(255, 255, 255);")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label_8 = QtWidgets.QLabel(info)
        self.label_8.setGeometry(QtCore.QRect(-30, 60, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.label_11 = QtWidgets.QLabel(info)
        self.label_11.setGeometry(QtCore.QRect(120, 20, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_11.setObjectName("label_11")
        self.label_9 = QtWidgets.QLabel(info)
        self.label_9.setGeometry(QtCore.QRect(-30, 90, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(info)
        self.label_10.setGeometry(QtCore.QRect(-30, 120, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_10.setObjectName("label_10")
        self.label_12 = QtWidgets.QLabel(info)
        self.label_12.setGeometry(QtCore.QRect(-30, 150, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(info)
        self.label_13.setGeometry(QtCore.QRect(120, 200, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(info)
        self.label_14.setGeometry(QtCore.QRect(-30, 270, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(info)
        self.label_15.setGeometry(QtCore.QRect(-30, 240, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_15.setObjectName("label_15")
        self.textBrowser_tasks = QtWidgets.QTextBrowser(info)
        self.textBrowser_tasks.setGeometry(QtCore.QRect(260, 60, 141, 21))
        self.textBrowser_tasks.setStyleSheet("background-color: rgb(77, 77, 77);\n"
"color: rgb(255, 255, 255);")
        self.textBrowser_tasks.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_tasks.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textBrowser_tasks.setObjectName("textBrowser_tasks")
        self.textBrowser_tasks_2 = QtWidgets.QTextBrowser(info)
        self.textBrowser_tasks_2.setGeometry(QtCore.QRect(260, 90, 141, 21))
        self.textBrowser_tasks_2.setStyleSheet("background-color: rgb(77, 77, 77);\n"
"color: rgb(255, 255, 255);")
        self.textBrowser_tasks_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_tasks_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textBrowser_tasks_2.setObjectName("textBrowser_tasks_2")
        self.textBrowser_tasks_3 = QtWidgets.QTextBrowser(info)
        self.textBrowser_tasks_3.setGeometry(QtCore.QRect(260, 120, 141, 21))
        self.textBrowser_tasks_3.setStyleSheet("background-color: rgb(77, 77, 77);\n"
"color: rgb(255, 255, 255);")
        self.textBrowser_tasks_3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_tasks_3.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textBrowser_tasks_3.setObjectName("textBrowser_tasks_3")
        self.textBrowser_tasks_4 = QtWidgets.QTextBrowser(info)
        self.textBrowser_tasks_4.setGeometry(QtCore.QRect(260, 150, 141, 21))
        self.textBrowser_tasks_4.setStyleSheet("background-color: rgb(77, 77, 77);\n"
"color: rgb(255, 255, 255);")
        self.textBrowser_tasks_4.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_tasks_4.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textBrowser_tasks_4.setObjectName("textBrowser_tasks_4")
        self.textBrowser_tasks_5 = QtWidgets.QTextBrowser(info)
        self.textBrowser_tasks_5.setGeometry(QtCore.QRect(260, 240, 141, 21))
        self.textBrowser_tasks_5.setStyleSheet("background-color: rgb(77, 77, 77);\n"
"color: rgb(255, 255, 255);")
        self.textBrowser_tasks_5.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_tasks_5.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textBrowser_tasks_5.setObjectName("textBrowser_tasks_5")
        self.textBrowser_tasks_6 = QtWidgets.QTextBrowser(info)
        self.textBrowser_tasks_6.setGeometry(QtCore.QRect(260, 270, 141, 21))
        self.textBrowser_tasks_6.setStyleSheet("background-color: rgb(77, 77, 77);\n"
"color: rgb(255, 255, 255);")
        self.textBrowser_tasks_6.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_tasks_6.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textBrowser_tasks_6.setObjectName("textBrowser_tasks_6")

        self.retranslateUi(info)
        self.buttonBox.accepted.connect(info.accept)
        self.buttonBox.rejected.connect(info.reject)
        QtCore.QMetaObject.connectSlotsByName(info)

        node = noc.get_node(selected_node)
        l = []
        for task in task_list:
            l += task.get_requests_for_node(selected_node)

        self.textBrowser_tasks.setText(str(selected_node))
        self.textBrowser_tasks_2.setText("calcul" if node.type == 'C' else "mémoire")
        size = (node.capacity if node.type == 'M' else node.cache_size)
        self.textBrowser_tasks_3.setText(str(size)+" bit" if size == 0 or size == 1 else str(size)+" bits")
        self.textBrowser_tasks_4.setText(str(node.computation_time if node.type == 'C' else 0))
        self.textBrowser_tasks_5.setText(f"{round(node.use(), 1)}%")
        self.textBrowser_tasks_6.setText(str(len(l)))
    def retranslateUi(self, info):
        _translate = QtCore.QCoreApplication.translate
        info.setWindowTitle(_translate("info", "Dialog"))
        self.label_8.setText(_translate("info", "<html><head/><body><p align=\"right\">Identifiant :</p></body></html>"))
        self.label_11.setText(_translate("info", "<html><head/><body><p align=\"center\">Information sur le nœud</p></body></html>"))
        self.label_9.setText(_translate("info", "<html><head/><body><p align=\"right\">Type de nœud :</p></body></html>"))
        self.label_10.setText(_translate("info", "<html><head/><body><p align=\"right\">Taille cache/mémoire :</p></body></html>"))
        self.label_12.setText(_translate("info", "<html><head/><body><p align=\"right\">Temps de calcul :</p></body></html>"))
        self.label_13.setText(_translate("info", "<html><head/><body><p align=\"center\">Simulation</p></body></html>"))
        self.label_14.setText(_translate("info", "<html><head/><body><p align=\"right\">Nombre de requêtes :</p></body></html>"))
        self.label_15.setText(_translate("info", "<html><head/><body><p align=\"right\">Taux d\'utilisation en mémoire :</p></body></html>"))


class Ui_add_node(object):
    """
    Permet d'ajouter un nœud au NoC depuis l'IHM.
    """
    def setupUi(self, add_node):
        add_node.setObjectName("add_node")
        add_node.resize(589, 263)
        add_node.setStyleSheet("background-color: rgb(60, 63, 65);")
        self.buttonBox = QtWidgets.QDialogButtonBox(add_node)
        self.buttonBox.setGeometry(QtCore.QRect(220, 220, 193, 28))
        self.buttonBox.setStyleSheet("background-color: rgb(77, 77, 77);\n"
"color: rgb(255, 255, 255);")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label_7 = QtWidgets.QLabel(add_node)
        self.label_7.setGeometry(QtCore.QRect(40, 70, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(add_node)
        self.label_8.setGeometry(QtCore.QRect(40, 100, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(add_node)
        self.label_9.setGeometry(QtCore.QRect(40, 130, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(add_node)
        self.label_10.setGeometry(QtCore.QRect(40, 160, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(add_node)
        self.label_11.setGeometry(QtCore.QRect(170, 20, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_11.setObjectName("label_11")
        self.node_type = QtWidgets.QComboBox(add_node)
        self.node_type.setGeometry(QtCore.QRect(330, 70, 171, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.node_type.setFont(font)
        self.node_type.setStyleSheet("color: rgb(255, 255, 255);")
        self.node_type.setObjectName("node_type")
        self.node_type.addItem("")
        self.node_type.addItem("")
        self.capacity = QtWidgets.QSpinBox(add_node)
        self.capacity.setGeometry(QtCore.QRect(330, 130, 61, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.capacity.setFont(font)
        self.capacity.setStyleSheet("color: rgb(255, 255, 255);")
        self.capacity.setObjectName("capacity")
        self.time = QtWidgets.QSpinBox(add_node)
        self.time.setGeometry(QtCore.QRect(330, 160, 61, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.time.setFont(font)
        self.time.setStyleSheet("color: rgb(255, 255, 255);")
        self.time.setObjectName("time")
        self.id = QtWidgets.QSpinBox(add_node)
        self.id.setGeometry(QtCore.QRect(330, 100, 61, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.id.setFont(font)
        self.id.setStyleSheet("color: rgb(255, 255, 255);")
        self.id.setObjectName("id")

        self.parent_widget = add_node

        self.retranslateUi(add_node)
        self.buttonBox.accepted.connect(self.validate_and_add_node)
        self.buttonBox.accepted.connect(add_node.accept)
        self.buttonBox.rejected.connect(add_node.reject)
        QtCore.QMetaObject.connectSlotsByName(add_node)

    def validate_and_add_node(self):
        capacity = self.capacity.value()

        if isinstance(capacity, int) and capacity > 0:
            self.add_node_()
        else:
            message_box = QtWidgets.QMessageBox(self.parent_widget)
            message_box.setIcon(QtWidgets.QMessageBox.Critical)
            message_box.setWindowTitle("Capacité non conforme.")
            message_box.setText("La capacité d'un nœud de mémoire doit être un entier naturel non nul.")
            message_box.exec_()

    def retranslateUi(self, add_node):
        _translate = QtCore.QCoreApplication.translate
        add_node.setWindowTitle(_translate("add_node", "Dialog"))
        self.label_7.setText(_translate("add_node", "<html><head/><body><p align=\"right\">Type de nœud :</p></body></html>"))
        self.label_8.setText(_translate("add_node", "<html><head/><body><p align=\"right\">Id :</p></body></html>"))
        self.label_9.setText(_translate("add_node", "<html><head/><body><p align=\"right\">Taille cache/mémoire :</p></body></html>"))
        self.label_10.setText(_translate("add_node", "<html><head/><body><p align=\"right\">Temps de calcul (Si nœud de calcul) :</p></body></html>"))
        self.label_11.setText(_translate("add_node", "<html><head/><body><p align=\"center\">Ajouter/modifier un nœud</p></body></html>"))
        self.node_type.setItemText(0, _translate("add_node", "Noeud de calcul"))
        self.node_type.setItemText(1, _translate("add_node", "Noeud de memoire"))

    def add_node_(self):
        global noc_is_modified
        type = self.node_type.currentText()
        id = self.id.value()
        capacity = self.capacity.value()
        time = self.time.value()
        try:
            if self.node_type.currentIndex() == 1:
                node = MemoryNode(id, capacity)
            else:
                node = CalculNode(id, capacity, time)
            noc.add_node(node)
            noc_is_modified = True
            print(f"Ajout du nœud {id} (type: {type}, capacity: {capacity}, time: {time})")

        except KeyError:  # Erreur levée si le nœud saisi existe déjà
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText(f"Attention : Le nœud {id} existe déjà.  Souhaitez-vous le remplacer?")
            msg.setWindowTitle("Attention")

            delete_button = QPushButton("Supprimer et remplacer")
            ignore_button = QPushButton("Abandonner")

            msg.addButton(delete_button, QMessageBox.YesRole)
            msg.addButton(ignore_button, QMessageBox.NoRole)

            msg.exec_()

            if msg.clickedButton() == delete_button:
                noc.remove_node(id)
                noc.add_node(node)


class Ui_del_node(object):
    """
    Supprimer un nœud depuis l'IHM.
    """
    def setupUi(self, del_node):
        del_node.setObjectName("del_node")
        del_node.resize(354, 156)
        del_node.setStyleSheet("background-color: rgb(60, 63, 65);")
        self.buttonBox = QtWidgets.QDialogButtonBox(del_node)
        self.buttonBox.setGeometry(QtCore.QRect(80, 110, 193, 28))
        self.buttonBox.setStyleSheet("background-color: rgb(77, 77, 77);\n"
"color: rgb(255, 255, 255);")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label_8 = QtWidgets.QLabel(del_node)
        self.label_8.setGeometry(QtCore.QRect(-100, 60, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.label_11 = QtWidgets.QLabel(del_node)
        self.label_11.setGeometry(QtCore.QRect(30, 20, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_11.setObjectName("label_11")
        self.id = QtWidgets.QSpinBox(del_node)
        self.id.setGeometry(QtCore.QRect(190, 60, 61, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.id.setFont(font)
        self.id.setStyleSheet("color: rgb(255, 255, 255);")
        self.id.setObjectName("id")

        self.retranslateUi(del_node)
        self.buttonBox.accepted.connect(self.del_node_)
        self.buttonBox.accepted.connect(del_node.accept)
        self.buttonBox.rejected.connect(del_node.reject)
        QtCore.QMetaObject.connectSlotsByName(del_node)

    def retranslateUi(self, del_node):
        _translate = QtCore.QCoreApplication.translate
        del_node.setWindowTitle(_translate("del_node", "Dialog"))
        self.label_8.setText(_translate("del_node", "<html><head/><body><p align=\"right\">Id :</p></body></html>"))
        self.label_11.setText(_translate("del_node", "<html><head/><body><p align=\"center\">Supprimer un nœud</p></body></html>"))

    def del_node_(self):
        global noc_is_modified
        id = self.id.value()
        try:
            noc.remove_node(id)
            noc_is_modified=True

        except KeyError:
            print(f"Le nœud {id} n'a pas pu être supprimé car il est introuvable dans le NoC.")
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Erreur")
            msg.setInformativeText(f'Le nœud {id} n\'existe pas dans le NoC.')
            msg.setWindowTitle("Erreur")
            msg.exec_()


class Ui_add_connection(object):
    def setupUi(self, add_connection):
        add_connection.setObjectName("add_connection")
        add_connection.resize(439, 207)
        add_connection.setStyleSheet("background-color: rgb(60, 63, 65);")
        self.buttonBox = QtWidgets.QDialogButtonBox(add_connection)
        self.buttonBox.setGeometry(QtCore.QRect(140, 160, 193, 28))
        self.buttonBox.setStyleSheet("background-color: rgb(77, 77, 77);\n"
"color: rgb(255, 255, 255);")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label_8 = QtWidgets.QLabel(add_connection)
        self.label_8.setGeometry(QtCore.QRect(-40, 90, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(add_connection)
        self.label_9.setGeometry(QtCore.QRect(-40, 120, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")
        self.label_11 = QtWidgets.QLabel(add_connection)
        self.label_11.setGeometry(QtCore.QRect(90, 20, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_11.setObjectName("label_11")
        self.id1 = QtWidgets.QSpinBox(add_connection)
        self.id1.setGeometry(QtCore.QRect(250, 120, 61, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.id1.setFont(font)
        self.id1.setStyleSheet("color: rgb(255, 255, 255);")
        self.id1.setObjectName("id1")
        self.id2 = QtWidgets.QSpinBox(add_connection)
        self.id2.setGeometry(QtCore.QRect(250, 90, 61, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.id2.setFont(font)
        self.id2.setStyleSheet("color: rgb(255, 255, 255);")
        self.id2.setObjectName("id2")
        self.latence = QtWidgets.QSpinBox(add_connection)
        self.latence.setGeometry(QtCore.QRect(250, 60, 61, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.latence.setFont(font)
        self.latence.setStyleSheet("color: rgb(255, 255, 255);")
        self.latence.setObjectName("latence")
        self.label_10 = QtWidgets.QLabel(add_connection)
        self.label_10.setGeometry(QtCore.QRect(-40, 60, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_10.setObjectName("label_10")

        self.retranslateUi(add_connection)
        self.buttonBox.accepted.connect(self.add_connection_)
        self.buttonBox.accepted.connect(add_connection.accept)
        self.buttonBox.rejected.connect(add_connection.reject)
        QtCore.QMetaObject.connectSlotsByName(add_connection)

    def retranslateUi(self, add_connection):
        _translate = QtCore.QCoreApplication.translate
        add_connection.setWindowTitle(_translate("add_connection", "Dialog"))
        self.label_8.setText(_translate("add_connection", "<html><head/><body><p align=\"right\">Id1 :</p></body></html>"))
        self.label_9.setText(_translate("add_connection", "<html><head/><body><p align=\"right\">Id2 :</p></body></html>"))
        self.label_11.setText(_translate("add_connection", "<html><head/><body><p align=\"center\">Ajouter/modifier une connexion</p></body></html>"))
        self.label_10.setText(_translate("add_connection", "<html><head/><body><p align=\"right\">Latence :</p></body></html>"))

    def add_connection_(self):
        global noc_is_modified
        id1 = self.id1.value()
        id2 = self.id2.value()
        latence = self.latence.value()
        try:
            noc.add_connection(id1, id2, latence)
            noc_is_modified = True
            print(f"Ajout de la connexion entre les noeuds {id1} et {id2} avec une latence de {latence}")

        except KeyError as e: # Une erreur est levée si un des noeud n'existe pas
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Erreur")
            msg.setInformativeText(
                f"Une erreur s'est produite:\n{e}"
            )
            msg.setWindowTitle("Erreur")
            msg.exec_()

        except ValueError:  # Erreur levée si la connexion existe déjà
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Attention : La connexion entre les nœuds saisis existe déjà.  Souhaitez-vous la remplacer?")
            msg.setWindowTitle("Attention")

            delete_button = QPushButton("Supprimer et remplacer")
            ignore_button = QPushButton("Abandonner")

            msg.addButton(delete_button, QMessageBox.YesRole)
            msg.addButton(ignore_button, QMessageBox.NoRole)

            msg.exec_()

            if msg.clickedButton() == delete_button:
                noc.remove_connection(id1, id2)
                noc.add_connection(id1, id2, latence)


class Ui_del_connection(object):
    def setupUi(self, del_connection):
        del_connection.setObjectName("del_connection")
        del_connection.resize(354, 174)
        del_connection.setStyleSheet("background-color: rgb(60, 63, 65);")
        self.buttonBox = QtWidgets.QDialogButtonBox(del_connection)
        self.buttonBox.setGeometry(QtCore.QRect(80, 130, 193, 28))
        self.buttonBox.setStyleSheet("background-color: rgb(77, 77, 77);\n"
"color: rgb(255, 255, 255);")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label_8 = QtWidgets.QLabel(del_connection)
        self.label_8.setGeometry(QtCore.QRect(-100, 60, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.label_11 = QtWidgets.QLabel(del_connection)
        self.label_11.setGeometry(QtCore.QRect(30, 20, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_11.setObjectName("label_11")
        self.id1 = QtWidgets.QSpinBox(del_connection)
        self.id1.setGeometry(QtCore.QRect(190, 60, 61, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.id1.setFont(font)
        self.id1.setStyleSheet("color: rgb(255, 255, 255);")
        self.id1.setObjectName("id1")
        self.id2 = QtWidgets.QSpinBox(del_connection)
        self.id2.setGeometry(QtCore.QRect(190, 90, 61, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.id2.setFont(font)
        self.id2.setStyleSheet("color: rgb(255, 255, 255);")
        self.id2.setObjectName("id2")
        self.label_9 = QtWidgets.QLabel(del_connection)
        self.label_9.setGeometry(QtCore.QRect(-100, 90, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")

        self.retranslateUi(del_connection)
        self.buttonBox.accepted.connect(self.del_connection_)
        self.buttonBox.accepted.connect(del_connection.accept)
        self.buttonBox.rejected.connect(del_connection.reject)
        QtCore.QMetaObject.connectSlotsByName(del_connection)

    def retranslateUi(self, del_connection):
        _translate = QtCore.QCoreApplication.translate
        del_connection.setWindowTitle(_translate("del_connection", "Dialog"))
        self.label_8.setText(_translate("del_connection", "<html><head/><body><p align=\"right\">Id1 :</p></body></html>"))
        self.label_11.setText(_translate("del_connection", "<html><head/><body><p align=\"center\">Supprimer une connexion</p></body></html>"))
        self.label_9.setText(_translate("del_connection", "<html><head/><body><p align=\"right\">Id2 :</p></body></html>"))

    def del_connection_(self):
        global noc_is_modified
        id1 = self.id1.value()
        id2 = self.id2.value()
        try:
            noc.remove_connection(id1,id2)
            noc_is_modified = True
            print(f"La connexion entre les nœuds {id1} et {id2} a bien été supprimée.")
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Erreur")
            msg.setInformativeText(f"Les nœuds {id1} et {id2} ne sont déjà pas connectés. \n\nVeuillez vérifier votre saisie et réessayer.")
            msg.setWindowTitle("Erreur")
            msg.exec_()

class Ui_add_task(object):
    def setupUi(self, add_task):
        add_task.setObjectName("add_task")
        add_task.resize(508, 263)
        add_task.setStyleSheet("background-color: rgb(60, 63, 65);")
        self.buttonBox = QtWidgets.QDialogButtonBox(add_task)
        self.buttonBox.setGeometry(QtCore.QRect(180, 220, 193, 28))
        self.buttonBox.setStyleSheet("background-color: rgb(77, 77, 77);\n"
"color: rgb(255, 255, 255);")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label_8 = QtWidgets.QLabel(add_task)
        self.label_8.setGeometry(QtCore.QRect(0, 80, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(add_task)
        self.label_9.setGeometry(QtCore.QRect(0, 110, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(add_task)
        self.label_10.setGeometry(QtCore.QRect(0, 140, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(add_task)
        self.label_11.setGeometry(QtCore.QRect(130, 20, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_11.setObjectName("label_11")
        self.source = QtWidgets.QSpinBox(add_task)
        self.source.setGeometry(QtCore.QRect(290, 110, 61, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.source.setFont(font)
        self.source.setStyleSheet("color: rgb(255, 255, 255);")
        self.source.setObjectName("source")
        self.destination = QtWidgets.QSpinBox(add_task)
        self.destination.setGeometry(QtCore.QRect(290, 140, 61, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.destination.setFont(font)
        self.destination.setStyleSheet("color: rgb(255, 255, 255);")
        self.destination.setObjectName("destination")
        self.pos = QtWidgets.QSpinBox(add_task)
        self.pos.setGeometry(QtCore.QRect(290, 80, 61, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pos.setFont(font)
        self.pos.setStyleSheet("color: rgb(255, 255, 255);")
        self.pos.setObjectName("pos")
        self.data_size = QtWidgets.QSpinBox(add_task)
        self.data_size.setGeometry(QtCore.QRect(290, 170, 61, 22))
        self.data_size.setMinimum(1)
        self.data_size.setMaximum(999)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.data_size.setFont(font)
        self.data_size.setStyleSheet("color: rgb(255, 255, 255);")
        self.data_size.setObjectName("data_size")
        self.label_12 = QtWidgets.QLabel(add_task)
        self.label_12.setGeometry(QtCore.QRect(0, 170, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_12.setObjectName("label_12")

        self.retranslateUi(add_task)
        self.buttonBox.accepted.connect(self.add_task_)
        self.buttonBox.accepted.connect(add_task.accept)
        self.buttonBox.rejected.connect(add_task.reject)
        QtCore.QMetaObject.connectSlotsByName(add_task)

    def retranslateUi(self, add_task):
        _translate = QtCore.QCoreApplication.translate
        add_task.setWindowTitle(_translate("add_task", "Dialog"))
        self.label_8.setText(_translate("add_task", "<html><head/><body><p align=\"right\">Position dans la liste de tâche :</p></body></html>"))
        self.label_9.setText(_translate("add_task", "<html><head/><body><p align=\"right\">Numéro id du nœud source :</p></body></html>"))
        self.label_10.setText(_translate("add_task", "<html><head/><body><p align=\"right\">Numéro id du nœud destination :</p></body></html>"))
        self.label_11.setText(_translate("add_task", "<html><head/><body><p align=\"center\">Ajouter/modifier un nœud</p></body></html>"))
        self.label_12.setText(_translate("add_task", "<html><head/><body><p align=\"right\">Taille de la donnée (octet) :</p></body></html>"))

    def add_task_(self):
        global task_list, noc
        all_nodes = list(noc.memory_nodes.values()) + list(noc.calcul_nodes.values())

        if len(all_nodes)==0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Erreur")
            msg.setInformativeText(
                "Veuillez générer au moins au noeud avant de générer des tâches."
            )
            msg.setWindowTitle("Erreur")
            msg.exec_()
            return

        try:
            task_list.insert(self.pos.value(), Task(self.source.value(), self.destination.value(), [random.randint(0, 1) for i in range(self.data_size.value()*8)]))
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Erreur")
            msg.setInformativeText(
                f"Une erreur s'est produite lors de l'ajout de la tâche.\n"
                f"\n"
                f"Veuillez vérifier votre saisie et réessayer."
            )
            msg.setWindowTitle("Erreur")
            msg.exec_()


class Ui_random_tasks(object):
    def setupUi(self, random_tasks):
        random_tasks.setObjectName("random_tasks")
        random_tasks.resize(623, 271)
        random_tasks.setStyleSheet("background-color: rgb(60, 63, 65);")
        self.buttonBox = QtWidgets.QDialogButtonBox(random_tasks)
        self.buttonBox.setGeometry(QtCore.QRect(220, 230, 193, 28))
        self.buttonBox.setStyleSheet("background-color: rgb(77, 77, 77);\n"
"color: rgb(255, 255, 255);")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label_11 = QtWidgets.QLabel(random_tasks)
        self.label_11.setGeometry(QtCore.QRect(170, 20, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_11.setObjectName("label_11")
        self.nb_task = QtWidgets.QSpinBox(random_tasks)
        self.nb_task.setGeometry(QtCore.QRect(400, 100, 61, 22))
        self.nb_task.setMinimum(1)
        self.nb_task.setMaximum(99)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nb_task.setFont(font)
        self.nb_task.setStyleSheet("color: rgb(255, 255, 255);")
        self.nb_task.setObjectName("nb_task")
        self.label_10 = QtWidgets.QLabel(random_tasks)
        self.label_10.setGeometry(QtCore.QRect(70, 100, 321, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_10.setObjectName("label_10")
        self.data_min = QtWidgets.QSpinBox(random_tasks)
        self.data_min.setGeometry(QtCore.QRect(340, 180, 61, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.data_min.setFont(font)
        self.data_min.setStyleSheet("color: rgb(255, 255, 255);")
        self.data_min.setObjectName("data_min")
        self.data_min.setMinimum(1)
        self.data_min.setMaximum(999)
        self.label_12 = QtWidgets.QLabel(random_tasks)
        self.label_12.setGeometry(QtCore.QRect(0, 180, 323, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_12.setObjectName("label_12")
        self.data_max = QtWidgets.QSpinBox(random_tasks)
        self.data_max.setMinimum(1)
        self.data_max.setMaximum(999)
        self.data_max.setGeometry(QtCore.QRect(430, 180, 61, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.data_max.setFont(font)
        self.data_max.setStyleSheet("color: rgb(255, 255, 255);")
        self.data_max.setObjectName("data_max")
        self.label_13 = QtWidgets.QLabel(random_tasks)
        self.label_13.setGeometry(QtCore.QRect(350, 150, 27, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(random_tasks)
        self.label_14.setGeometry(QtCore.QRect(440, 150, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_14.setObjectName("label_14")
        self.pos = QtWidgets.QSpinBox(random_tasks)
        self.pos.setGeometry(QtCore.QRect(400, 70, 61, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pos.setFont(font)
        self.pos.setStyleSheet("color: rgb(255, 255, 255);")
        self.pos.setObjectName("pos")
        self.label_15 = QtWidgets.QLabel(random_tasks)
        self.label_15.setGeometry(QtCore.QRect(70, 70, 321, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_15.setObjectName("label_15")

        self.retranslateUi(random_tasks)
        self.buttonBox.accepted.connect(self.random_task_list)
        self.buttonBox.accepted.connect(random_tasks.accept)
        self.buttonBox.rejected.connect(random_tasks.reject)
        QtCore.QMetaObject.connectSlotsByName(random_tasks)
        self.error_shown = False

    def random_task_list_once(self):
        self.random_task_list()
        self.buttonBox.accepted.disconnect(self.random_task_list_once)

    def retranslateUi(self, random_tasks):
        _translate = QtCore.QCoreApplication.translate
        random_tasks.setWindowTitle(_translate("random_tasks", "Dialog"))
        self.label_11.setText(_translate("random_tasks", "<html><head/><body><p align=\"center\">Liste de tâches aléatoires</p></body></html>"))
        self.label_10.setText(_translate("random_tasks", "<html><head/><body><p align=\"right\">Nombre de tâches :</p></body></html>"))
        self.label_12.setText(_translate("random_tasks", "<html><head/><body><p align=\"right\">Taille de la donnée (octect) :</p></body></html>"))
        self.label_13.setText(_translate("random_tasks", "<html><head/><body><p align=\"right\">min</p></body></html>"))
        self.label_14.setText(_translate("random_tasks", "<html><head/><body><p align=\"right\">max</p></body></html>"))
        self.label_15.setText(_translate("random_tasks", "<html><head/><body><p align=\"right\"> Position dans la liste de tâches :</p></body></html>"))

    def random_task_list(self):
        global task_list, noc
        task_list_tmp = []
        all_nodes = list(noc.memory_nodes.values()) + list(noc.calcul_nodes.values())

        if len(all_nodes)==0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Erreur")
            msg.setInformativeText(
                "Pour générer une liste de tâches, vous devez d'abord générer des noeuds."
            )
            msg.setWindowTitle("Erreur")
            msg.exec_()
            return

        for i in range(self.nb_task.value()):
            start_node_id = all_nodes[random.randint(0, len(all_nodes))-1].id
            end_node_id = all_nodes[random.randint(0, len(all_nodes))-1].id
            while end_node_id == start_node_id:
                end_node_id = all_nodes[random.randint(0, len(all_nodes))-1].id
            max_size = self.data_max.value()
            min_size = self.data_min.value()
            if min_size > max_size:
                if not self.error_shown:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText("Erreur")
                    msg.setInformativeText(
                        "La taille de la donnée maximale saisie est inférieure à la taille de la donnée mininimale saisie."
                        "\n\nVeuillez vérifier votre saisie et réessayer."
                    )
                    msg.setWindowTitle("Erreur")
                    msg.exec_()
                    self.error_shown = True
                return
            else:
                data_size = random.randint(min_size, max_size) * 8 # Taille en termes d'éléments (multiple de 8)
                data = [random.randint(0, 1) for i in range(data_size)]
                task_list_tmp.append(Task(start_node_id, end_node_id, data))
        for i, task in enumerate(task_list_tmp):
            task_list.insert(self.pos.value() + i, task)


class Ui_random_noc(object):
    def setupUi(self, random_noc):
        random_noc.setObjectName("random_noc")
        random_noc.resize(661, 659)
        random_noc.setStyleSheet("background-color: rgb(60, 63, 65);")
        self.buttonBox = QtWidgets.QDialogButtonBox(random_noc)
        self.buttonBox.setGeometry(QtCore.QRect(270, 580, 193, 28))
        self.buttonBox.setStyleSheet("background-color: rgb(77, 77, 77);\n"
"color: rgb(255, 255, 255);")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label_11 = QtWidgets.QLabel(random_noc)
        self.label_11.setGeometry(QtCore.QRect(210, 20, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_11.setObjectName("label_11")
        self.nb_mem = QtWidgets.QSpinBox(random_noc)
        self.nb_mem.setGeometry(QtCore.QRect(400, 130, 61, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nb_mem.setFont(font)
        self.nb_mem.setStyleSheet("color: rgb(255, 255, 255);")
        self.nb_mem.setObjectName("nb_mem")
        self.label_10 = QtWidgets.QLabel(random_noc)
        self.label_10.setGeometry(QtCore.QRect(70, 130, 321, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_10.setObjectName("label_10")
        self.latence_min = QtWidgets.QSpinBox(random_noc)
        self.latence_min.setGeometry(QtCore.QRect(470, 380, 61, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.latence_min.setFont(font)
        self.latence_min.setStyleSheet("color: rgb(255, 255, 255);")
        self.latence_min.setObjectName("latence_min")
        self.label_12 = QtWidgets.QLabel(random_noc)
        self.label_12.setGeometry(QtCore.QRect(130, 380, 323, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_12.setObjectName("label_12")
        self.latence_max = QtWidgets.QSpinBox(random_noc)
        self.latence_max.setGeometry(QtCore.QRect(560, 380, 61, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.latence_max.setFont(font)
        self.latence_max.setStyleSheet("color: rgb(255, 255, 255);")
        self.latence_max.setObjectName("latence_max")
        self.label_13 = QtWidgets.QLabel(random_noc)
        self.label_13.setGeometry(QtCore.QRect(480, 350, 27, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(random_noc)
        self.label_14.setGeometry(QtCore.QRect(570, 350, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_14.setObjectName("label_14")
        self.nb_calcul = QtWidgets.QSpinBox(random_noc)
        self.nb_calcul.setGeometry(QtCore.QRect(400, 100, 61, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nb_calcul.setFont(font)
        self.nb_calcul.setStyleSheet("color: rgb(255, 255, 255);")
        self.nb_calcul.setObjectName("nb_calcul")
        self.label_15 = QtWidgets.QLabel(random_noc)
        self.label_15.setGeometry(QtCore.QRect(70, 100, 321, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(random_noc)
        self.label_16.setGeometry(QtCore.QRect(80, 160, 394, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_16.setObjectName("label_16")
        self.connection = QtWidgets.QSpinBox(random_noc)
        self.connection.setGeometry(QtCore.QRect(480, 160, 61, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.connection.setFont(font)
        self.connection.setStyleSheet("color: rgb(255, 255, 255);")
        self.connection.setObjectName("connection")
        self.label_17 = QtWidgets.QLabel(random_noc)
        self.label_17.setGeometry(QtCore.QRect(100, 190, 394, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_17.setObjectName("label_17")
        self.mem_max = QtWidgets.QSpinBox(random_noc)
        self.mem_max.setGeometry(QtCore.QRect(560, 460, 61, 22))
        self.mem_max.setMinimum(1)
        self.mem_max.setMaximum(999)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.mem_max.setFont(font)
        self.mem_max.setStyleSheet("color: rgb(255, 255, 255);")
        self.mem_max.setObjectName("mem_max")
        self.mem_min = QtWidgets.QSpinBox(random_noc)
        self.mem_min.setGeometry(QtCore.QRect(470, 460, 61, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.mem_min.setFont(font)
        self.mem_min.setStyleSheet("color: rgb(255, 255, 255);")
        self.mem_min.setObjectName("mem_min")
        self.mem_min.setMinimum(1)
        self.mem_min.setMaximum(999)
        self.label_18 = QtWidgets.QLabel(random_noc)
        self.label_18.setGeometry(QtCore.QRect(130, 460, 323, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(random_noc)
        self.label_19.setGeometry(QtCore.QRect(82, 500, 371, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_19.setObjectName("label_19")
        self.cache_min = QtWidgets.QSpinBox(random_noc)
        self.cache_min.setGeometry(QtCore.QRect(470, 500, 61, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cache_min.setFont(font)
        self.cache_min.setStyleSheet("color: rgb(255, 255, 255);")
        self.cache_min.setObjectName("cache_min")
        self.cache_min.setMinimum(1)
        self.cache_min.setMaximum(999)
        self.cache_max = QtWidgets.QSpinBox(random_noc)
        self.cache_max.setGeometry(QtCore.QRect(560, 500, 61, 22))
        self.cache_max.setMinimum(1)
        self.cache_max.setMaximum(999)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cache_max.setFont(font)
        self.cache_max.setStyleSheet("color: rgb(255, 255, 255);")
        self.cache_max.setObjectName("cache_max")
        self.label_20 = QtWidgets.QLabel(random_noc)
        self.label_20.setGeometry(QtCore.QRect(-70, 420, 521, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_20.setObjectName("label_20")
        self.cac_min = QtWidgets.QSpinBox(random_noc)
        self.cac_min.setGeometry(QtCore.QRect(470, 420, 61, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cac_min.setFont(font)
        self.cac_min.setStyleSheet("color: rgb(255, 255, 255);")
        self.cac_min.setObjectName("cac_min")
        self.cac_max = QtWidgets.QSpinBox(random_noc)
        self.cac_max.setGeometry(QtCore.QRect(560, 420, 61, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cac_max.setFont(font)
        self.cac_max.setStyleSheet("color: rgb(255, 255, 255);")
        self.cac_max.setObjectName("cac_max")
        self.checkBox = QtWidgets.QCheckBox(random_noc)
        self.checkBox.setGeometry(QtCore.QRect(210, 540, 301, 20))
        self.checkBox.setStyleSheet("color: rgb(255, 255, 255);")
        self.checkBox.setObjectName("checkBox")
        self.label_21 = QtWidgets.QLabel(random_noc)
        self.label_21.setGeometry(QtCore.QRect(160, 70, 361, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(random_noc)
        self.label_22.setGeometry(QtCore.QRect(160, 310, 361, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_22.setObjectName("label_22")

        self.retranslateUi(random_noc)
        self.buttonBox.accepted.connect(self.random_noc_)
        self.buttonBox.accepted.connect(random_noc.accept)
        self.buttonBox.rejected.connect(random_noc.reject)
        QtCore.QMetaObject.connectSlotsByName(random_noc)

    def retranslateUi(self, random_noc):
        _translate = QtCore.QCoreApplication.translate
        random_noc.setWindowTitle(_translate("random_noc", "Dialog"))
        self.label_11.setText(_translate("random_noc", "<html><head/><body><p align=\"center\">Créer un NoC aléatoire</p></body></html>"))
        self.label_10.setText(_translate("random_noc", "<html><head/><body><p align=\"right\">Nombre de nœuds de mémoire :</p></body></html>"))
        self.label_12.setText(_translate("random_noc", "<html><head/><body><p align=\"right\">Latence (en unité de temps) :</p></body></html>"))
        self.label_13.setText(_translate("random_noc", "<html><head/><body><p align=\"right\">min</p></body></html>"))
        self.label_14.setText(_translate("random_noc", "<html><head/><body><p align=\"right\">max</p></body></html>"))
        self.label_15.setText(_translate("random_noc", "<html><head/><body><p align=\"right\">Nombre de nœuds de calcul :</p></body></html>"))
        self.label_16.setText(_translate("random_noc", "<html><head/><body><p align=\"right\">Chance d\'avoir une connexion entre deux nœuds : 1/</p></body></html>"))
        self.label_17.setText(_translate("random_noc", "<html><head/><body><p align=\"center\">(rq: si 1/0 il n\'y a aucune connexion entre les nœuds)</p></body></html>"))
        self.label_18.setText(_translate("random_noc", "<html><head/><body><p align=\"right\">Capacité des nœuds de mémoire (octet) :</p></body></html>"))
        self.label_19.setText(_translate("random_noc", "<html><head/><body><p align=\"right\">Taille du cache des nœuds de calcul (octet) :</p></body></html>"))
        self.label_20.setText(_translate("random_noc", "<html><head/><body><p align=\"right\">Temps de calcul des nœuds de calcul (en unité de temps) :</p></body></html>"))
        self.checkBox.setText(_translate("random_noc", "Remplir les caractéristiques automatiquement"))
        self.label_21.setText(_translate("random_noc", "<html><head/><body><p align=\"center\">--------------------- Générale ---------------------</p></body></html>"))
        self.label_22.setText(_translate("random_noc", "<html><head/><body><p align=\"center\">--------------------- Caractéristiques ---------------------</p></body></html>"))

    def random_noc_(self):
        global noc,noc_is_modified
        nb_calcul_node = self.nb_calcul.value()
        nb_memory_node = self.nb_mem.value()
        rnd_connection = self.connection.value()
        min_latency, max_latency = self.latence_min.value(), self.latence_max.value()
        cac_min, cac_max = self.cac_min.value(), self.cac_max.value()
        mem_min, mem_max = self.mem_min.value(), self.mem_max.value()
        time_min, time_max = self.cache_min.value(), self.cache_max.value()
        auto = self.checkBox.isChecked()

        if noc_is_modified and noc.size>0:  # Vérifiez si le NoC actuel a été modifié et non enregistré et qu'il est non vide
            message_box = QMessageBox()
            message_box.setIcon(QMessageBox.Warning)
            message_box.setWindowTitle("Avertissement")
            message_box.setText(
                "Le NoC actuel n'a pas été enregistré. Voulez-vous continuer et perdre les modifications?")
            message_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            button_result = message_box.exec_()
            if button_result == QMessageBox.No:
                return None  # Annule la génération d'un nouveau NoC

        try:
            if not auto:
                noc.new_random(nb_calcul_node, nb_memory_node, rnd_connection,
                               latency=(min_latency, max_latency),
                               cache=(cac_min, cac_max),
                               memory=(mem_min, mem_max),
                               computation_time=(time_min, time_max))
            else:
                noc.new_random(nb_calcul_node, nb_memory_node, rnd_connection)
            print("Le NoC a bien été créé.")
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Erreur")
            msg.setInformativeText(f"Une erreur s'est produite dans la création du NoC. \n\nVeuillez réessayer.")
            msg.setWindowTitle("Erreur")
            msg.exec_()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1310, 837)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\bertr\\PycharmProjects\\pythonProject\\Informatique\\TD4\\IHM_Test\\Final\\Best\\Icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(60, 63, 65);\n"
"color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(85, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.container = QtWidgets.QWidget(self.centralwidget)
        self.container.setGeometry(QtCore.QRect(19, 9, 811, 641))
        self.container.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.container.setObjectName("container")
        self.button_generate = QtWidgets.QPushButton(self.centralwidget)
        self.button_generate.setGeometry(QtCore.QRect(30, 670, 191, 41))
        self.button_generate.setStyleSheet("background-color: rgb(77, 77, 77);")
        self.button_generate.setObjectName("button_generate")
        self.button_generate.clicked.connect(self.plot_graph)
        self.button_add_node = QtWidgets.QPushButton(self.centralwidget)
        self.button_add_node.setGeometry(QtCore.QRect(230, 670, 191, 41))
        self.button_add_node.setStyleSheet("background-color: rgb(77, 77, 77);")
        self.button_add_node.setObjectName("button_add_node")
        self.button_add_node.clicked.connect(self.open_add_node)
        self.button_add_connection = QtWidgets.QPushButton(self.centralwidget)
        self.button_add_connection.setGeometry(QtCore.QRect(430, 670, 191, 41))
        self.button_add_connection.setStyleSheet("background-color: rgb(77, 77, 77);")
        self.button_add_connection.setObjectName("button_add_connection")
        self.button_add_connection.clicked.connect(self.open_add_connection)
        self.button_show_info = QtWidgets.QPushButton(self.centralwidget)
        self.button_show_info.setGeometry(QtCore.QRect(630, 720, 191, 41))
        self.button_show_info.setStyleSheet("background-color: rgb(77, 77, 77);")
        self.button_show_info.setObjectName("button_show_info")
        self.button_show_info.clicked.connect(self.open_info)
        self.button_del_node = QtWidgets.QPushButton(self.centralwidget)
        self.button_del_node.setGeometry(QtCore.QRect(230, 720, 191, 41))
        self.button_del_node.setStyleSheet("background-color: rgb(77, 77, 77);")
        self.button_del_node.setObjectName("button_del_node")
        self.button_del_node.clicked.connect(self.open_del_node)
        self.button_del_connection = QtWidgets.QPushButton(self.centralwidget)
        self.button_del_connection.setGeometry(QtCore.QRect(430, 720, 191, 41))
        self.button_del_connection.setStyleSheet("background-color: rgb(77, 77, 77);")
        self.button_del_connection.setObjectName("button_del_connection")
        self.button_del_connection.clicked.connect(self.open_del_connection)
        self.button_random_soc = QtWidgets.QPushButton(self.centralwidget)
        self.button_random_soc.setGeometry(QtCore.QRect(30, 720, 191, 41))
        self.button_random_soc.setStyleSheet("background-color: rgb(77, 77, 77);")
        self.button_random_soc.setObjectName("button_random_soc")
        self.button_random_soc.clicked.connect(self.open_random_noc)
        self.button_random_soc.clicked.connect(self.plot_graph)
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(780, 680, 41, 21))
        self.spinBox.setObjectName("spinBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(630, 670, 151, 41))
        self.label.setObjectName("label")
        self.button_simulate = QtWidgets.QPushButton(self.centralwidget)
        self.button_simulate.setGeometry(QtCore.QRect(860, 670, 191, 91))
        self.button_simulate.setStyleSheet("background-color: rgb(77, 77, 77);")
        self.button_simulate.setObjectName("button_simulate")
        self.button_simulate.clicked.connect(self.simulate)
        self.button_simulate.clicked.connect(self.show_time)
        self.button_simulate.clicked.connect(self.show_use)
        self.button_simulate.clicked.connect(self.show_treated_task)
        self.button_raz = QtWidgets.QPushButton(self.centralwidget)
        self.button_raz.setGeometry(QtCore.QRect(1090, 670, 191, 91))
        self.button_raz.setStyleSheet("background-color: rgb(77, 77, 77);")
        self.button_raz.setObjectName("button_raz")
        self.button_raz.clicked.connect(self.raz)
        self.textBrowser_msg = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_msg.setGeometry(QtCore.QRect(860, 521, 421, 131))
        self.textBrowser_msg.setStyleSheet("background-color: rgb(77, 77, 77);")
        self.textBrowser_msg.setObjectName("textBrowser_msg")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(860, 499, 421, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(860, 360, 421, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(860, 430, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(860, 460, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(860, 400, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(860, 10, 421, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(855, 40, 431, 211))
        self.tableView.setStyleSheet("background-color: rgb(77, 77, 77);")
        self.tableView.setObjectName("tableView")
        header_stylesheet = "::section{ color: rgb(60, 63, 65); }"
        self.tableView.horizontalHeader().setStyleSheet(header_stylesheet)
        self.tableView.verticalHeader().setStyleSheet(header_stylesheet)
        self.button_add_task = QtWidgets.QPushButton(self.centralwidget)
        self.button_add_task.setGeometry(QtCore.QRect(860, 260, 191, 31))
        self.button_add_task.setStyleSheet("background-color: rgb(77, 77, 77);")
        self.button_add_task.setObjectName("button_add_task")
        self.button_add_task.clicked.connect(self.open_add_task)
        self.button_del_task = QtWidgets.QPushButton(self.centralwidget)
        self.button_del_task.setGeometry(QtCore.QRect(1090, 260, 191, 31))
        self.button_del_task.setStyleSheet("background-color: rgb(77, 77, 77);")
        self.button_del_task.setObjectName("button_del_task")
        self.button_del_task.clicked.connect(self.delete_row)
        self.button_random_task = QtWidgets.QPushButton(self.centralwidget)
        self.button_random_task.setGeometry(QtCore.QRect(860, 300, 191, 31))
        self.button_random_task.setStyleSheet("background-color: rgb(77, 77, 77);")
        self.button_random_task.setObjectName("button_random_task")
        self.button_random_task.clicked.connect(self.open_random_tasks)
        self.button_random_task.clicked.connect(self.update_table)
        self.button_del_all_task = QtWidgets.QPushButton(self.centralwidget)
        self.button_del_all_task.setGeometry(QtCore.QRect(1090, 300, 191, 31))
        self.button_del_all_task.setStyleSheet("background-color: rgb(77, 77, 77);")
        self.button_del_all_task.setObjectName("button_del_all_task")
        self.button_del_all_task.clicked.connect(self.delete_all)
        self.textBrowser_tasks = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_tasks.setGeometry(QtCore.QRect(1080, 400, 201, 21))
        self.textBrowser_tasks.setStyleSheet("background-color: rgb(77, 77, 77);")
        self.textBrowser_tasks.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_tasks.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textBrowser_tasks.setObjectName("textBrowser_tasks")
        self.textBrowser_time = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_time.setGeometry(QtCore.QRect(1080, 430, 201, 21))
        self.textBrowser_time.setStyleSheet("background-color: rgb(77, 77, 77);")
        self.textBrowser_time.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_time.setObjectName("textBrowser_time")
        self.textBrowser_use = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_use.setGeometry(QtCore.QRect(1080, 460, 201, 21))
        self.textBrowser_use.setStyleSheet("background-color: rgb(77, 77, 77);")
        self.textBrowser_use.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_use.setObjectName("textBrowser_use")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1310, 26))
        self.menubar.setStyleSheet("color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(85, 170, 255);")
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setStyleSheet("")
        self.menuFile.setObjectName("menuFile")
        self.menuTasks = QtWidgets.QMenu(self.menubar)
        self.menuTasks.setObjectName("menuTasks")
        self.menuShow = QtWidgets.QMenu(self.menubar)
        self.menuShow.setObjectName("menuShow")
        self.menuNode = QtWidgets.QMenu(self.menuShow)
        self.menuNode.setObjectName("menuNode")
        self.menuInfos = QtWidgets.QMenu(self.menubar)
        self.menuInfos.setObjectName("menuInfos")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionNew.triggered.connect(self.new_noc)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpen.triggered.connect(self.import_noc)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave.triggered.connect(self.export_noc)
        self.actionQuitter = QtWidgets.QAction(MainWindow)
        self.actionQuitter.setObjectName("actionQuitter")
        self.actionImport = QtWidgets.QAction(MainWindow)
        self.actionImport.setObjectName("actionImport")
        self.actionImport.triggered.connect(self.import_task)
        self.actionImport.triggered.connect(self.update_table)
        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.actionExport.triggered.connect(self.export_task)
        self.actionLicense = QtWidgets.QAction(MainWindow)
        self.actionLicense.setObjectName("actionLicense")
        self.actionLicense.triggered.connect(self.display_license)
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionHelp.triggered.connect(self.open_help)
        self.actionLatency = QtWidgets.QAction(MainWindow)
        self.actionLatency.setObjectName("actionLatency")
        self.actionLatency.triggered.connect(self.display_latency)
        self.actionId = QtWidgets.QAction(MainWindow)
        self.actionId.setObjectName("actionId")
        self.actionId.triggered.connect(self.display_id)
        self.actionUse = QtWidgets.QAction(MainWindow)
        self.actionUse.setObjectName("actionUse")
        self.actionUse.triggered.connect(self.display_use)
        self.actionMask = QtWidgets.QAction(MainWindow)
        self.actionMask.setObjectName("actionMask")
        self.actionMask.triggered.connect(self.display_hide)
        self.actionFigsize = QtWidgets.QAction(MainWindow)
        self.actionFigsize.setObjectName("actionFigsize")
        self.actionFigsize.triggered.connect(self.open_change_figsize)

        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuitter)
        self.menuTasks.addAction(self.actionImport)
        self.menuTasks.addAction(self.actionExport)
        self.menuNode.addAction(self.actionId)
        self.menuNode.addAction(self.actionUse)
        self.menuNode.addAction(self.actionMask)
        self.menuShow.addAction(self.actionFigsize)
        self.menuShow.addAction(self.menuNode.menuAction())
        self.menuShow.addAction(self.actionLatency)
        self.menuInfos.addAction(self.actionLicense)
        self.menuInfos.addAction(self.actionHelp)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTasks.menuAction())
        self.menubar.addAction(self.menuShow.menuAction())
        self.menubar.addAction(self.menuInfos.menuAction())

        self.retranslateUi(MainWindow)
        self.actionQuitter.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Simulateur NoC by Samy AYYADA & Antoine BERTRAND"))
        self.button_generate.setText(_translate("MainWindow", "Rafraîchir"))
        self.button_add_node.setText(_translate("MainWindow", "Ajouter un nœud"))
        self.button_add_connection.setText(_translate("MainWindow", "Ajouter une connexion"))
        self.button_show_info.setText(_translate("MainWindow", "Afficher"))
        self.button_del_node.setText(_translate("MainWindow", "Supprimer un nœud"))
        self.button_del_connection.setText(_translate("MainWindow", "Supprimer une connexion"))
        self.button_random_soc.setText(_translate("MainWindow", "NoC Aléatoire"))
        self.label.setText(_translate("MainWindow", "Informations du nœud "))
        self.button_simulate.setText(_translate("MainWindow", "Simuler"))
        self.button_raz.setText(_translate("MainWindow", "RàZ"))
        self.label_2.setText(_translate("MainWindow", "Messages du simulateur"))
        self.label_3.setText(_translate("MainWindow", "----------------- Résultats de la simulation --------------------------"))
        self.label_4.setText(_translate("MainWindow", "Temps de traîtement :"))
        self.label_5.setText(_translate("MainWindow", "Taux d\'utilisation du NoC :"))
        self.label_6.setText(_translate("MainWindow", "Nombre de tâches traîtées :"))
        self.label_7.setText(_translate("MainWindow", "----------------------- Liste de tâches --------------------------"))
        self.button_add_task.setText(_translate("MainWindow", "Ajouter"))
        self.button_del_task.setText(_translate("MainWindow", "Supprimer"))
        self.button_random_task.setText(_translate("MainWindow", "Liste aléatoire de tâches"))
        self.button_del_all_task.setText(_translate("MainWindow", "Tout supprimer"))
        self.menuFile.setTitle(_translate("MainWindow", "Fichier"))
        self.menuTasks.setTitle(_translate("MainWindow", "Tâches"))
        self.menuShow.setTitle(_translate("MainWindow", "Afficher"))
        self.menuNode.setTitle(_translate("MainWindow", "Afficher/masquer étiquettes"))
        self.menuInfos.setTitle(_translate("MainWindow", "Infos"))
        self.actionNew.setText(_translate("MainWindow", "Nouveau NoC"))
        self.actionOpen.setText(_translate("MainWindow", "Ouvrir NoC"))
        self.actionSave.setText(_translate("MainWindow", "Sauvegarder NoC"))
        self.actionQuitter.setText(_translate("MainWindow", "Quitter"))
        self.actionImport.setText(_translate("MainWindow", "Importer tâches"))
        self.actionExport.setText(_translate("MainWindow", "Exporter tâches"))
        self.actionLicense.setText(_translate("MainWindow", "Licence"))
        self.actionHelp.setText(_translate("MainWindow", "Aides"))
        self.actionLatency.setText(_translate("MainWindow", "Afficher/masquer latence"))
        self.actionId.setText(_translate("MainWindow", "ID"))
        self.actionUse.setText(_translate("MainWindow", "Légende"))
        self.actionMask.setText(_translate("MainWindow", "Masquer"))
        self.actionFigsize.setText(_translate("Mainwindow", "Changer la taille du graphe"))


        self.graphe_widget = FigureCanvas(plt.Figure())
        layout = QtWidgets.QVBoxLayout(self.container)
        layout.addWidget(self.graphe_widget)
        self.plot_graph()
        self.update_table()

    def update_table(self):
        """
        Mets à jour la liste de tâches
        """
        global task_list
        model = QtGui.QStandardItemModel()
        model.setHorizontalHeaderLabels(["Source", "Destination", "Taille donnée"])
        for task in task_list:
            items = []
            items.append(QtGui.QStandardItem(str(task.start_node_id)))
            items.append(QtGui.QStandardItem(str(task.end_node_id)))
            size = len(task.data)//8
            if size == 0 or size == 1:
                strg = "octet"
            else:
                strg = "octets"
            items.append(QtGui.QStandardItem(str(size)+" "+strg))
            model.appendRow(items)

        self.tableView.setModel(model)

    def plot_graph(self):
        """
        Affiche ou mets à jour l'affichage du graphe.
        """
        global noc, figsize
        graph = noc.to_networkx_graph()
        fig, ax = plt.subplots(figsize=figsize)

        # Création des objets Line2D pour les symboles de légende
        memory_line = mlines.Line2D([], [], color='white', marker='o', markersize=8, markeredgecolor='black',
                                    label='Noeud de mémoire')
        calculation_line = mlines.Line2D([], [], color='white', marker='s', markersize=8, markeredgecolor='black',
                                         label='Noeud de calcul')

        # Création de la légende avec les symboles correspondants
        if show_use :
            legend = ax.legend(handles=[memory_line, calculation_line], loc='upper right', bbox_to_anchor=(1.18, 1.0), fontsize='medium')

            # Ajout d'un cadre autour de la légende
            legend.get_frame().set_linewidth(0.5)
            legend.get_frame().set_edgecolor('black')


        node_types = nx.get_node_attributes(graph, 'type')
        node_sizes_dict = nx.get_node_attributes(graph, 'size')
        node_sizes = [v for k, v in sorted(node_sizes_dict.items())]
        node_uses = {node_id: round(noc.get_node(node_id).use()) for node_id in graph.nodes}
        weights = nx.get_edge_attributes(graph, 'weight')

        # On crée un gradient de couleur (du vert au rouge)
        cmap = plt.cm.get_cmap('RdYlGn_r')

        # Création de la colorbar (légende du gradient de couleur)
        if show_use:
            sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=0, vmax=100))
            sm.set_array([])
            fig.colorbar(sm, orientation='vertical', label='Utilisation du noeud (%)', shrink=0.5, ax=ax)

        pos = nx.spring_layout(graph, seed=42)

        calc_nodes = [node for node in graph.nodes if node_types[node] == 'C']
        calc_pos = {node: pos[node] for node in calc_nodes}
        calc_sizes = [node_sizes_dict[node] for node in calc_nodes]
        calc_colors = [cmap(node_uses[node] / 100) for node in calc_nodes]
        nx.draw_networkx_nodes(graph, calc_pos, nodelist=calc_nodes, node_color=calc_colors, node_size=calc_sizes,
                               ax=ax,
                               node_shape='s')

        mem_nodes = [node for node in graph.nodes if node_types[node] == 'M']
        mem_pos = {node: pos[node] for node in mem_nodes}
        mem_sizes = [node_sizes_dict[node] for node in mem_nodes]
        mem_colors = [cmap(node_uses[node] / 100) for node in mem_nodes]
        nx.draw_networkx_nodes(graph, mem_pos, nodelist=mem_nodes, node_color=mem_colors, node_size=mem_sizes, ax=ax,
                               node_shape='o')

        if show_id:
            nx.draw_networkx_labels(graph, pos, ax=ax)
        if show_use:
            nx.draw_networkx_labels(graph, pos, ax=ax)
        nx.draw_networkx_edges(graph, pos, edge_color='black', ax=ax)
        if show_latency:
            nx.draw_networkx_edge_labels(graph, pos, edge_labels=weights, font_color="black", ax=ax)
        ax.axis("off")
        plt.close()
        self.graphe_widget.figure = fig
        self.graphe_widget.draw()
        plt.close()

    def delete_row(self):
        global task_list
        selection_model = self.tableView.selectionModel()
        try:
            selected_indexes = selection_model.selectedIndexes()

            if len(selected_indexes) == 0:
                error_box = QMessageBox()
                error_box.setIcon(QMessageBox.Warning)
                error_box.setWindowTitle("Erreur")
                error_box.setText("Veuillez sélectionner la ou les tâches à supprimer.")
                error_box.exec_()
                return

            indices_to_remove = []
            message_box = QMessageBox()
            message_box.setIcon(QMessageBox.Warning)
            message_box.setWindowTitle("Avertissement")

            if len(selected_indexes) > 1:
                indices_text = ', '.join(str(index.row() + 1) for index in selected_indexes)
                message_box.setText(f"Êtes-vous sûr de vouloir supprimer les tâches {indices_text} ?")
            else:
                index_text = str(selected_indexes[0].row() + 1)
                message_box.setText(f"Êtes-vous sûr de vouloir supprimer la tâche {index_text} ?")

            message_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            button_result = message_box.exec_()

            if button_result == QMessageBox.No:
                return

            indices_to_remove = [index.row() for index in selected_indexes]
            updated_list = [element for index, element in enumerate(task_list) if index not in indices_to_remove]

            for row in indices_to_remove:
                print(f"La tâche {row + 1} a été supprimée.")

            task_list = updated_list
            self.update_table()
        except Exception as e:
            error_box = QMessageBox()
            error_box.setIcon(QMessageBox.Critical)
            error_box.setWindowTitle("Erreur")
            error_box.setText(f"Une erreur s'est produite : {str(e)}")
            error_box.exec_()

    def delete_all(self):
        global task_list

        if not task_list:
            return

        message_box = QtWidgets.QMessageBox()
        message_box.setIcon(QtWidgets.QMessageBox.Warning)
        message_box.setWindowTitle("Avertissement")
        message_box.setText("Êtes-vous sûr de vouloir supprimer toutes les tâches ?")
        message_box.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        button_result = message_box.exec_()

        if button_result == QtWidgets.QMessageBox.Yes:
            task_list = []
            self.update_table()

    def simulate(self):
        global task_list
        for i, task in enumerate(task_list):
            try:
                task.fill(noc)
                task.exec(noc)
            except:
                task.clear()
                print(f"la tâche {i} n'a pas pu être réalisée")

        self.write_simulation_report("simulation_report.txt")

    def show_time(self):
        """
        Affiche le temps d'exécution des requêtes.
        """
        global task_list
        time = 0
        for task in task_list:
            if task.time != None:
                time += task.time
        self.textBrowser_time.clear()
        self.textBrowser_time.append(f"{time} unités de temps")

    def show_use(self):
        """
        Affiche le pourcentage d'utilisation du NoC (mémoire utilisée par rapport à la mémoire totale).
        :return:
        """
        global noc
        use = 0
        all_nodes = list(noc.memory_nodes.values()) + list(noc.calcul_nodes.values())
        if len(all_nodes)==0: return # S'il n'y a pas de noeuds, ne pas calculer l'utilisation
        for node in all_nodes:
            use += node.use()
        self.textBrowser_use.clear()
        self.textBrowser_use.append(f"{round(use/len(all_nodes), 1)}%")

    def show_treated_task(self):
        """
        Affiche le nombre de tâches traitées sur le nombre total de tâches.
        """
        global task_list
        treated = 0
        for task in task_list:
            if task.time != None:
                treated += 1
        self.textBrowser_tasks.clear()
        self.textBrowser_tasks.append(f"{treated}/{len(task_list)}")

    def raz(self):
        global noc, task_list, treated, use, time
        treated, use, time = 0, 0, 0
        for task in task_list:
            task.clear()
        self.textBrowser_tasks.clear()
        self.textBrowser_use.clear()
        self.textBrowser_time.clear()
        self.textBrowser_msg.clear()
        noc.clean()

    def write_simulation_report(self, file_path):
        global task_list, noc

        # Date et heure actuelle
        current_datetime = datetime.datetime.now()

        # Calcul de l'utilisation du NoC
        use = 0
        all_nodes = list(noc.memory_nodes.values()) + list(noc.calcul_nodes.values())
        for node in all_nodes:
            use += node.use()
        if len(all_nodes)!=0: use=use/len(all_nodes)

        with open(file_path, 'w') as file:
            file.write("-------------------------------------------- Rapport de la simulation --------------------------------------------\n\n")

            # Informations générales
            file.write("Informations générales\n")
            file.write("Date et heure : {}\n".format(current_datetime.strftime("%Y-%m-%d %H:%M:%S")))
            file.write("Nombre total de tâches : {}\n".format(len(task_list)))
            file.write("Utilisation du NoC : {}%\n".format(round(use, 1)))
            file.write("Temps total de traitement : {} unités de temps\n".format(
                sum([task.time if task.time is not None else 0 for task in task_list])))
            file.write("\n")

            # Liste des nœuds avec leurs caractéristiques principales
            file.write("Liste des nœuds\n")
            file.write("ID |   Type   | Taille (mémoire ou cache) | Temps de calcul | Plage protégée | Utilisation (%)\n")
            nodes = {**noc.memory_nodes,**noc.calcul_nodes}
            sorted_nodes = sorted(nodes.items(), key=lambda x: x[0])
            for node_id, node in sorted_nodes:
                if node.type == 'C':
                    node_type = "Calcul"
                    node_size = node.cache_size
                    node_calc = node.computation_time
                    node_protected = 'Aucune'
                else:
                    node_type = "Mémoire"
                    node_size = node.capacity
                    node_calc = '/'
                    node_protected = node.protected_range
                    if node_protected==None: node_protected='Aucune'
                node_use = round(node.use(), 1)
                file.write("{:^2} | {:^8} | {:^25} | {:^15} | {:^14} | {:^13}%\n"
                           .format(node_id, node_type, node_size,node_calc, str(node_protected),node_use))
            file.write("\n")

            # Tâches traitées
            file.write("\n ----- Tâches traitées ----\n")
            treated_tasks = [task for task in task_list if task.time is not None]
            file.write("Nombre de tâches traitées : {}\n".format(len(treated_tasks)))
            file.write("Liste des tâches traitées :\n")
            for i, task in enumerate(treated_tasks, 1):
                file.write("Tâche {} : \n".format(i))
                file.write("  - Source : {}\n".format(task.start_node_id))
                file.write("  - Destination : {}\n".format(task.end_node_id))
                file.write("  - Taille de la donnée : {} octets\n".format(len(task.data)))
                file.write("  - Temps de traitement : {} unités de temps\n".format(task.time))
                file.write("\n")

            # Tâches non traitées
            file.write("\n ----- Tâches non traitées ----- \n")
            failed_tasks = [task for task in task_list if task.time is None]
            file.write("Nombre de tâches non traitées : {}\n".format(len(failed_tasks)))
            file.write("Liste des tâches non traitées :\n")
            for i, task in enumerate(failed_tasks, 1):
                file.write("Tâche {} : \n".format(i))
                file.write("  - Source : {}\n".format(task.start_node_id))
                file.write("  - Destination : {}\n".format(task.end_node_id))
                file.write("  - Taille de la donnée : {} octets\n".format(len(task.data)))
                file.write("\n")

            file.write("\n--- FIN DU RAPPORT ---")

        print("Le rapport de simulation a été écrit dans le fichier : {}".format(file_path))

    def display_id(self):
        global show_id, show_use
        show_id = True
        show_use = False

    def display_use(self):
        global show_id, show_use
        show_id = False
        show_use = True

    def display_hide(self):
        global show_id, show_use
        show_id = False
        show_use = False

    def display_latency(self):
        global show_latency
        show_latency = not show_latency

    def import_task(self):
        global task_list, task_is_modified

        if task_is_modified and len(task_list)>0:
            message_box = QMessageBox()
            message_box.setIcon(QMessageBox.Warning)
            message_box.setWindowTitle("Avertissement")
            message_box.setText(
                "La liste de tâches actuelle n'a pas été enregistrée. Voulez-vous continuer et perdre les modifications?")
            message_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            button_result = message_box.exec_()
            if button_result == QMessageBox.No:
                return None

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filename, _ = QFileDialog.getOpenFileName(None, "Ouvrir le fichier tâches", "", "Fichiers Tâches (*.pkl)",
                                                  options=options)
        if filename:
            with open(filename, 'rb') as file:
                task_list = pickle.load(file)
                task_is_modified=False
            self.update_table()
            print(f"Ouverture des tâches contenues dans le fichier {filename}")

    def export_task(self):
        global task_list, task_is_modified
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filename, _ = QFileDialog.getSaveFileName(None, "Sauvegarder la liste de tâches", "", "Fichiers Tâches (*.pkl)",
                                                  options=options)
        if filename:
            with open(filename, 'wb') as file:
                pickle.dump(task_list, file)
            task_is_modified=False
            self.raz()
        print(f"La liste de tâches a été sauvegardée dans le fichier {filename}")

    def new_noc(self):
        global noc,noc_is_modified
        if noc_is_modified:  # Vérifiez si le NoC actuel a été modifié et non enregistré
            message_box = QMessageBox()
            message_box.setIcon(QMessageBox.Warning)
            message_box.setWindowTitle("Avertissement")
            message_box.setText(
                "Le NoC actuel n'a pas été enregistré. Voulez-vous continuer et perdre les modifications?")
            message_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            button_result = message_box.exec_()
            if button_result == QMessageBox.No:
                return None  # Annule l'ouverture du fichier NoC
        noc.clear()

    def import_noc(self):
        global noc, noc_is_modified

        if noc_is_modified:  # Vérifiez si le NoC actuel a été modifié et non enregistré
            message_box = QMessageBox()
            message_box.setIcon(QMessageBox.Warning)
            message_box.setWindowTitle("Avertissement")
            message_box.setText(
                "Le NoC actuel n'a pas été enregistré. Voulez-vous continuer et perdre les modifications?")
            message_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            button_result = message_box.exec_()
            if button_result == QMessageBox.No:
                return None  # Annule l'ouverture du fichier NoC

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filename, _ = QFileDialog.getOpenFileName(None, "Ouvrir le fichier NoC", "", "Fichiers NoC (*.pkl)",
                                                  options=options)
        if filename:
            with open(filename, 'rb') as file:
                noc = pickle.load(file)
                noc_is_modified = False
                self.raz()
            print(f"Ouverture du NoC contenu dans le fichier {filename}")

    def export_noc(self):
        global noc_is_modified
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filename, _ = QFileDialog.getSaveFileName(None, "Sauvegarder le NoC", "", "Fichiers NoC (*.pkl)",
                                                  options=options)
        if filename:
            with open(filename, 'wb') as file:
                pickle.dump(noc, file)
            noc_is_modified=False
            print(f"Le NoC a bien été enregistré dans le fichier {filename}")

    def open_add_node(self):
        self.second_window = QtWidgets.QDialog()
        self.ui = Ui_add_node()
        self.ui.setupUi(self.second_window)
        self.second_window.exec_()

    def open_del_node(self):
        self.second_window = QtWidgets.QDialog()
        self.ui = Ui_del_node()
        self.ui.setupUi(self.second_window)
        self.second_window.exec_()

    def open_del_connection(self):
        self.second_window = QtWidgets.QDialog()
        self.ui = Ui_del_connection()
        self.ui.setupUi(self.second_window)
        self.second_window.exec_()

    def open_add_connection(self):
        self.second_window = QtWidgets.QDialog()
        self.ui = Ui_add_connection()
        self.ui.setupUi(self.second_window)
        self.second_window.exec_()

    def open_info(self):
        global selected_node
        try:
            self.second_window = QtWidgets.QDialog()
            self.ui = Ui_info()
            selected_node = self.spinBox.value()
            self.ui.setupUi(self.second_window)
            self.second_window.exec_()
        except:
            print(f"Le nœud {selected_node} n'existe pas dans le NoC. \nVeuillez vérifier votre saisie et réessayer.")

    def open_add_task(self):
        self.second_window = QtWidgets.QDialog()
        self.ui = Ui_add_task()
        self.ui.setupUi(self.second_window)
        self.second_window.exec_()
        self.update_table()

    def open_random_tasks(self):
        self.second_window = QtWidgets.QDialog()
        self.ui = Ui_random_tasks()
        self.ui.setupUi(self.second_window)
        self.second_window.exec_()
        self.update_table()

    def open_random_noc(self):
        self.second_window = QtWidgets.QDialog()
        self.ui = Ui_random_noc()
        self.ui.setupUi(self.second_window)
        self.second_window.exec_()

    def open_change_figsize(self):
        self.second_window = QtWidgets.QDialog()
        self.ui = Ui_fig_size()
        self.ui.setupUi(self.second_window)
        self.second_window.exec_()
        self.plot_graph()

    def open_help(self):
        url = QUrl("help.html")
        QDesktopServices.openUrl(url)

    def display_license(self):
        # Ouvrir le fichier et lire le contenu
        with open('license.txt', 'r', encoding='utf-8') as file:
            data = file.read()

        # Créer une nouvelle fenêtre
        self.license_window = QtWidgets.QDialog(self.centralwidget)
        self.license_window.setWindowTitle("Licence")
        self.license_window.resize(800, 600)  # définir la taille de la fenêtre

        # Ajouter un QTextBrowser à la fenêtre et y afficher le contenu du fichier
        self.text_browser = QtWidgets.QTextBrowser(self.license_window)
        self.text_browser.setGeometry(QtCore.QRect(10, 10, 780, 580))  # définir la taille et la position
        self.text_browser.setText(data)  # afficher le texte

        # Afficher la fenêtre
        self.license_window.show()


class StdoutRedirector(io.TextIOBase):
    def __init__(self, qtextbrowser):
        super().__init__()
        self.qtextbrowser = qtextbrowser

    def write(self, s):
        self.qtextbrowser.insertPlainText(s)



if __name__ == "__main__":
    # Variables utilisées par l'interface
    figsize = (16, 12)
    selected_node = 0
    noc = NoC()
    noc_is_modified=True
    task_is_modified=True
    noc_save = NoC()
    show_id = True
    show_latency = True
    show_use = False
    task_list = []
    task_list_save = []


    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.stdout = StdoutRedirector(ui.textBrowser_msg)
    sys.exit(app.exec_()) #Mettre en commentaire pour debugger
