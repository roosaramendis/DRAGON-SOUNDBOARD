# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\mendis\Documents\GitHub\DRAGON-VOICEMODE\add programs for overlay ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_addprogramsforoverlay(object):
    def setupUi(self, addprogramsforoverlay):
        addprogramsforoverlay.setObjectName("addprogramsforoverlay")
        addprogramsforoverlay.resize(846, 322)
        self.listView = QtWidgets.QListView(addprogramsforoverlay)
        self.listView.setGeometry(QtCore.QRect(20, 70, 801, 201))
        self.listView.setObjectName("listView")
        self.lineEdit = QtWidgets.QLineEdit(addprogramsforoverlay)
        self.lineEdit.setGeometry(QtCore.QRect(20, 30, 661, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(addprogramsforoverlay)
        self.label.setGeometry(QtCore.QRect(710, 30, 111, 16))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(addprogramsforoverlay)
        self.pushButton.setGeometry(QtCore.QRect(704, 280, 121, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(addprogramsforoverlay)
        QtCore.QMetaObject.connectSlotsByName(addprogramsforoverlay)

    def retranslateUi(self, addprogramsforoverlay):
        _translate = QtCore.QCoreApplication.translate
        addprogramsforoverlay.setWindowTitle(_translate("addprogramsforoverlay", "add programs for overlay"))
        self.label.setText(_translate("addprogramsforoverlay", "Search"))
        self.pushButton.setText(_translate("addprogramsforoverlay", "add"))
