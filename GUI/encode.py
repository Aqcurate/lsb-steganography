# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'encode.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(511, 402)
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
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.encode_bits_spin = QtWidgets.QSpinBox(dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.encode_bits_spin.setFont(font)
        self.encode_bits_spin.setMinimum(1)
        self.encode_bits_spin.setMaximum(8)
        self.encode_bits_spin.setProperty("value", 2)
        self.encode_bits_spin.setObjectName("encode_bits_spin")
        self.horizontalLayout.addWidget(self.encode_bits_spin)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.line = QtWidgets.QFrame(dialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.cover_img_btn = QtWidgets.QPushButton(dialog)
        self.cover_img_btn.setObjectName("cover_img_btn")
        self.horizontalLayout_3.addWidget(self.cover_img_btn)
        self.secret_img_btn = QtWidgets.QPushButton(dialog)
        self.secret_img_btn.setObjectName("secret_img_btn")
        self.horizontalLayout_3.addWidget(self.secret_img_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem)
        self.line_2 = QtWidgets.QFrame(dialog)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.encode_cancel_btn = QtWidgets.QPushButton(dialog)
        self.encode_cancel_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.encode_cancel_btn.setObjectName("encode_cancel_btn")
        self.horizontalLayout_2.addWidget(self.encode_cancel_btn)
        self.encode_submit_btn = QtWidgets.QPushButton(dialog)
        self.encode_submit_btn.setObjectName("encode_submit_btn")
        self.horizontalLayout_2.addWidget(self.encode_submit_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "Encoding"))
        self.label.setText(_translate("dialog", "Image encoding"))
        self.label_2.setText(_translate("dialog", "Select Number of bits (recommended 2):"))
        self.cover_img_btn.setText(_translate("dialog", "Select cover image"))
        self.secret_img_btn.setText(_translate("dialog", "Select secret image"))
        self.encode_cancel_btn.setText(_translate("dialog", "Cancel"))
        self.encode_submit_btn.setText(_translate("dialog", "Encode"))

