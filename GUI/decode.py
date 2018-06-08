# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'decode.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(514, 577)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.decode_graphic = QtWidgets.QGraphicsView(dialog)
        self.decode_graphic.setObjectName("decode_graphic")
        self.verticalLayout.addWidget(self.decode_graphic)
        self.decode_slider = QtWidgets.QSlider(dialog)
        self.decode_slider.setMouseTracking(False)
        self.decode_slider.setMinimum(1)
        self.decode_slider.setMaximum(8)
        self.decode_slider.setSliderPosition(1)
        self.decode_slider.setOrientation(QtCore.Qt.Horizontal)
        self.decode_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.decode_slider.setTickInterval(1)
        self.decode_slider.setObjectName("decode_slider")
        self.verticalLayout.addWidget(self.decode_slider)
        self.line = QtWidgets.QFrame(dialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.decode_file_btn = QtWidgets.QPushButton(dialog)
        self.decode_file_btn.setObjectName("decode_file_btn")
        self.verticalLayout.addWidget(self.decode_file_btn)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.decode_exit_btn = QtWidgets.QPushButton(dialog)
        self.decode_exit_btn.setObjectName("decode_exit_btn")
        self.horizontalLayout.addWidget(self.decode_exit_btn)
        self.decode_save_btn = QtWidgets.QPushButton(dialog)
        self.decode_save_btn.setObjectName("decode_save_btn")
        self.horizontalLayout.addWidget(self.decode_save_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "Decoding"))
        self.label.setText(_translate("dialog", "Image decoding"))
        self.decode_file_btn.setText(_translate("dialog", "Select File"))
        self.decode_exit_btn.setText(_translate("dialog", "Exit"))
        self.decode_save_btn.setText(_translate("dialog", "Save"))

