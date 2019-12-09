# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/qcode.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogShowQrCode(object):
    def setupUi(self, DialogShowQrCode):
        DialogShowQrCode.setObjectName("DialogShowQrCode")
        DialogShowQrCode.resize(480, 320)
        self.buttonBox = QtWidgets.QDialogButtonBox(DialogShowQrCode)
        self.buttonBox.setGeometry(QtCore.QRect(326, 268, 150, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.buttonBox.setFont(font)
        self.buttonBox.setStyleSheet("background-color: lightgrey;\n"
"font: 24pt \"Arial\";")
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.top_right_logo = QtWidgets.QLabel(DialogShowQrCode)
        self.top_right_logo.setGeometry(QtCore.QRect(430, 2, 40, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.top_right_logo.sizePolicy().hasHeightForWidth())
        self.top_right_logo.setSizePolicy(sizePolicy)
        self.top_right_logo.setText("")
        self.top_right_logo.setPixmap(QtGui.QPixmap(":/RaspiBlitz/images/RaspiBlitz_Logo_Berry.png"))
        self.top_right_logo.setScaledContents(True)
        self.top_right_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.top_right_logo.setObjectName("top_right_logo")
        self.frame = QtWidgets.QFrame(DialogShowQrCode)
        self.frame.setGeometry(QtCore.QRect(0, 0, 320, 320))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.qcode = QtWidgets.QLabel(self.frame)
        self.qcode.setGeometry(QtCore.QRect(1, 1, 318, 318))
        self.qcode.setStyleSheet("background-color: white")
        self.qcode.setText("")
        self.qcode.setPixmap(QtGui.QPixmap(":/RaspiBlitz/images/RaspiBlitz_Logo_Stacked.png"))
        self.qcode.setScaledContents(True)
        self.qcode.setAlignment(QtCore.Qt.AlignCenter)
        self.qcode.setObjectName("qcode")
        self.label = QtWidgets.QLabel(DialogShowQrCode)
        self.label.setGeometry(QtCore.QRect(330, 4, 88, 60))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/RaspiBlitz/images/RaspiBlitz_Logo_Stacked.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(DialogShowQrCode)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(320, 70, 161, 191))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.horizontalLayoutWidget)
        self.verticalLayout.setContentsMargins(6, 0, 6, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.line = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.memo_key = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.memo_key.setFont(font)
        self.memo_key.setScaledContents(False)
        self.memo_key.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.memo_key.setWordWrap(True)
        self.memo_key.setObjectName("memo_key")
        self.verticalLayout.addWidget(self.memo_key)
        self.memo_value = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.memo_value.setFont(font)
        self.memo_value.setScaledContents(False)
        self.memo_value.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.memo_value.setWordWrap(True)
        self.memo_value.setObjectName("memo_value")
        self.verticalLayout.addWidget(self.memo_value)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.status_key = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.status_key.setFont(font)
        self.status_key.setScaledContents(False)
        self.status_key.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.status_key.setWordWrap(True)
        self.status_key.setObjectName("status_key")
        self.horizontalLayout.addWidget(self.status_key)
        self.status_value = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.status_value.setFont(font)
        self.status_value.setScaledContents(False)
        self.status_value.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.status_value.setWordWrap(True)
        self.status_value.setObjectName("status_value")
        self.horizontalLayout.addWidget(self.status_value)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.inv_amt_key = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.inv_amt_key.setFont(font)
        self.inv_amt_key.setObjectName("inv_amt_key")
        self.verticalLayout.addWidget(self.inv_amt_key)
        self.inv_amt_value = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.inv_amt_value.setFont(font)
        self.inv_amt_value.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.inv_amt_value.setObjectName("inv_amt_value")
        self.verticalLayout.addWidget(self.inv_amt_value)
        self.amt_paid_key = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.amt_paid_key.setFont(font)
        self.amt_paid_key.setObjectName("amt_paid_key")
        self.verticalLayout.addWidget(self.amt_paid_key)
        self.amt_paid_value = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.amt_paid_value.setFont(font)
        self.amt_paid_value.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.amt_paid_value.setObjectName("amt_paid_value")
        self.verticalLayout.addWidget(self.amt_paid_value)
        self.spinner = QtWidgets.QWidget(DialogShowQrCode)
        self.spinner.setGeometry(QtCore.QRect(440, 0, 40, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinner.sizePolicy().hasHeightForWidth())
        self.spinner.setSizePolicy(sizePolicy)
        self.spinner.setObjectName("spinner")
        self.spinner.raise_()
        self.buttonBox.raise_()
        self.top_right_logo.raise_()
        self.frame.raise_()
        self.label.raise_()
        self.horizontalLayoutWidget.raise_()

        self.retranslateUi(DialogShowQrCode)
        self.buttonBox.accepted.connect(DialogShowQrCode.accept)
        QtCore.QMetaObject.connectSlotsByName(DialogShowQrCode)

    def retranslateUi(self, DialogShowQrCode):
        _translate = QtCore.QCoreApplication.translate
        DialogShowQrCode.setWindowTitle(_translate("DialogShowQrCode", "Dialog"))
        self.memo_key.setText(_translate("DialogShowQrCode", "Memo"))
        self.memo_value.setText(_translate("DialogShowQrCode", "RB-Vivid-Badger"))
        self.status_key.setText(_translate("DialogShowQrCode", "Status"))
        self.status_value.setText(_translate("DialogShowQrCode", "Open/Paid"))
        self.inv_amt_key.setText(_translate("DialogShowQrCode", "Invoice Amount"))
        self.inv_amt_value.setText(_translate("DialogShowQrCode", "123456798"))
        self.amt_paid_key.setText(_translate("DialogShowQrCode", "Amount Paid"))
        self.amt_paid_value.setText(_translate("DialogShowQrCode", "N/A"))

from . import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogShowQrCode = QtWidgets.QDialog()
    ui = Ui_DialogShowQrCode()
    ui.setupUi(DialogShowQrCode)
    DialogShowQrCode.show()
    sys.exit(app.exec_())

