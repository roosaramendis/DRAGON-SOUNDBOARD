# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\mendis\Documents\GitHub\DRAGON-VOICEMODE\voice mode settings.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 480)
        self.enablenitify = QtWidgets.QCheckBox(Dialog)
        self.enablenitify.setGeometry(QtCore.QRect(40, 40, 341, 17))
        self.enablenitify.setObjectName("enablenitify")
        self.enableoverlay = QtWidgets.QCheckBox(Dialog)
        self.enableoverlay.setGeometry(QtCore.QRect(40, 90, 421, 20))
        self.enableoverlay.setObjectName("enableoverlay")
        self.info = QtWidgets.QPushButton(Dialog)
        self.info.setGeometry(QtCore.QRect(30, 450, 75, 23))
        self.info.setObjectName("info")
        self.add_overlay_programs = QtWidgets.QPushButton(Dialog)
        self.add_overlay_programs.setEnabled(True)
        self.add_overlay_programs.setGeometry(QtCore.QRect(40, 130, 131, 23))
        self.add_overlay_programs.setObjectName("add_overlay_programs")
        self.listView = QtWidgets.QListView(Dialog)
        self.listView.setGeometry(QtCore.QRect(40, 190, 561, 161))
        self.listView.setObjectName("listView")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 160, 551, 21))
        self.label.setObjectName("label")
        self.removeselcetedapp = QtWidgets.QPushButton(Dialog)
        self.removeselcetedapp.setGeometry(QtCore.QRect(490, 360, 111, 23))
        self.removeselcetedapp.setObjectName("removeselcetedapp")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.enablenitify.setText(_translate("Dialog", "enable notifications"))
        self.enableoverlay.setText(_translate("Dialog", "enable game overlay"))
        self.info.setText(_translate("Dialog", "Info"))
        self.add_overlay_programs.setText(_translate("Dialog", "Add OverLay Programs"))
        self.label.setText(_translate("Dialog", "....................................................Overlay enabled programs...................................................."))
        self.removeselcetedapp.setText(_translate("Dialog", "Remove Selected"))
