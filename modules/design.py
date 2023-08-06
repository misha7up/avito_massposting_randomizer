# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(270, 314)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.tedit_prefix = QtWidgets.QTextEdit(parent=Dialog)
        self.tedit_prefix.setGeometry(QtCore.QRect(45, 38, 181, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tedit_prefix.sizePolicy().hasHeightForWidth())
        self.tedit_prefix.setSizePolicy(sizePolicy)
        self.tedit_prefix.setAcceptDrops(True)
        self.tedit_prefix.setObjectName("tedit_prefix")
        self.spin_photo_count = QtWidgets.QSpinBox(parent=Dialog)
        self.spin_photo_count.setGeometry(QtCore.QRect(109, 90, 51, 24))
        self.spin_photo_count.setAcceptDrops(True)
        self.spin_photo_count.setMinimum(1)
        self.spin_photo_count.setMaximum(20)
        self.spin_photo_count.setProperty("value", 10)
        self.spin_photo_count.setObjectName("spin_photo_count")
        self.spin_combo_count = QtWidgets.QSpinBox(parent=Dialog)
        self.spin_combo_count.setGeometry(QtCore.QRect(107, 140, 61, 24))
        self.spin_combo_count.setAcceptDrops(True)
        self.spin_combo_count.setMinimum(1)
        self.spin_combo_count.setMaximum(1000)
        self.spin_combo_count.setProperty("value", 125)
        self.spin_combo_count.setObjectName("spin_combo_count")
        self.btn_save_to_file = QtWidgets.QPushButton(parent=Dialog)
        self.btn_save_to_file.setGeometry(QtCore.QRect(38, 230, 191, 32))
        self.btn_save_to_file.setObjectName("btn_save_to_file")
        self.tedit_freezed_numbers = QtWidgets.QTextEdit(parent=Dialog)
        self.tedit_freezed_numbers.setGeometry(QtCore.QRect(45, 195, 181, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tedit_freezed_numbers.sizePolicy().hasHeightForWidth())
        self.tedit_freezed_numbers.setSizePolicy(sizePolicy)
        self.tedit_freezed_numbers.setAcceptDrops(True)
        self.tedit_freezed_numbers.setObjectName("tedit_freezed_numbers")
        self.lbl_prefix = QtWidgets.QLabel(parent=Dialog)
        self.lbl_prefix.setGeometry(QtCore.QRect(54, 15, 171, 16))
        self.lbl_prefix.setObjectName("lbl_prefix")
        self.lbl_photo_count = QtWidgets.QLabel(parent=Dialog)
        self.lbl_photo_count.setGeometry(QtCore.QRect(61, 70, 161, 16))
        self.lbl_photo_count.setObjectName("lbl_photo_count")
        self.lbl_combo_count = QtWidgets.QLabel(parent=Dialog)
        self.lbl_combo_count.setGeometry(QtCore.QRect(60, 120, 171, 16))
        self.lbl_combo_count.setObjectName("lbl_combo_count")
        self.lbl_freezed_numbers = QtWidgets.QLabel(parent=Dialog)
        self.lbl_freezed_numbers.setGeometry(QtCore.QRect(72, 170, 131, 16))
        self.lbl_freezed_numbers.setObjectName("lbl_freezed_numbers")
        self.checkBox = QtWidgets.QCheckBox(parent=Dialog)
        self.checkBox.setGeometry(QtCore.QRect(45, 270, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox.setFont(font)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "AVGenerator by @misha7up"))
        self.tedit_prefix.setPlaceholderText(_translate("Dialog", "Например: лес/дом"))
        self.btn_save_to_file.setText(_translate("Dialog", "Сгенерировать в файл"))
        self.tedit_freezed_numbers.setPlaceholderText(_translate("Dialog", "Например: 1, 3"))
        self.lbl_prefix.setText(_translate("Dialog", "Префикс (название пути)"))
        self.lbl_photo_count.setText(_translate("Dialog", "Количество фотографий"))
        self.lbl_combo_count.setText(_translate("Dialog", "Количество комбинаций"))
        self.lbl_freezed_numbers.setText(_translate("Dialog", "Заморозить цифры"))
        self.checkBox.setText(_translate("Dialog", "Открыть файл после генерации"))
