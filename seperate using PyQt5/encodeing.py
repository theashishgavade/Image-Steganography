from PyQt5 import QtCore, QtGui, QtWidgets
from stegano import encode, FileError, DataError, PasswordError

class Ui_EncodeWindow(object):
    def setupUi(self, EncodeWindow):
        EncodeWindow.setObjectName("EncodeWindow")
        EncodeWindow.resize(780, 475)
        self.centralwidget = QtWidgets.QWidget(EncodeWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setAutoDefault(True)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout.addWidget(self.plainTextEdit)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem5)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_3.addWidget(self.label_9)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_3.addWidget(self.lineEdit_2)
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_3.addWidget(self.checkBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem6)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_6.addWidget(self.label_11)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem7)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem8)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem9)
        EncodeWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(EncodeWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 811, 21))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        EncodeWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(EncodeWindow)
        self.statusbar.setObjectName("statusbar")
        EncodeWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(EncodeWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(EncodeWindow)
        QtCore.QMetaObject.connectSlotsByName(EncodeWindow)

        # Slots
        self.pushButton.clicked.connect(self.getFile)
        self.pushButton_2.clicked.connect(self.encode)
        self.checkBox.stateChanged.connect(lambda: self.lineEdit_2.setEchoMode(
            QtWidgets.QLineEdit.Normal) if self.checkBox.isChecked() else self.lineEdit_2.setEchoMode(
            QtWidgets.QLineEdit.Password))

        # Menu action
        self.actionAbout.triggered.connect(
            lambda: self.displayMsg('About', 'Created by: Ashish Gavade \nInstagram: @theashishgavade \nGitHub: https://github.com/theashishgavade/'))

    def retranslateUi(self, EncodeWindow):
        _translate = QtCore.QCoreApplication.translate
        EncodeWindow.setWindowTitle(_translate("EncodeWindow", "Steganography Software - Encode"))
        self.label_4.setText(_translate("EncodeWindow",
                                        "<html><head/><body><p><span style=\" font-weight:600;\">Step 1:</span></p></body></html>"))
        self.label_3.setText(_translate("EncodeWindow", "Input Image File:"))
        self.pushButton.setText(_translate("EncodeWindow", "Choose File"))
        self.label.setText(_translate("EncodeWindow",
                                      "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; color:#fc2803;\">Encode</span></p></body></html>"))
        self.label_2.setText(_translate("EncodeWindow",
                                        "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; color:#03fc5a;\">Decode</span></p></body></html>"))
        self.label_5.setText(_translate("EncodeWindow",
                                        "<html><head/><body><p><span style=\" font-weight:600;\">Step 2:</span></p></body></html>"))
        self.label_7.setText(_translate("EncodeWindow", "Enter text to hide:"))
        self.label_8.setText(_translate("EncodeWindow",
                                        "<html><head/><body><p><span style=\" font-weight:600;\">Step 3:</span></p></body></html>"))
        self.label_9.setText(_translate("EncodeWindow", "Enter Password:"))
        self.checkBox.setText(_translate("EncodeWindow", "Show Password"))
        self.pushButton_2.setText(_translate("EncodeWindow", "Encode and Save"))
        self.label_11.setText(_translate("EncodeWindow",
                                         "<html><head/><body><p><span style=\" font-weight:600;\">Step 4:</span></p></body></html>"))
        self.menuHelp.setTitle(_translate("EncodeWindow", "Help"))
        self.actionAbout.setText(_translate("EncodeWindow", "About"))

    # Function to display message/error/information
    def displayMsg(self, title, msg, ico_type=None):
        MsgBox = QtWidgets.QMessageBox()
        MsgBox.setText(msg)
        MsgBox.setWindowTitle(title)
        if ico_type == 'err':
            ico = QtWidgets.QMessageBox.Critical
        else:
            ico = QtWidgets.QMessageBox.Information
        MsgBox.setIcon(ico)
        MsgBox.exec()

    # Function to choose input file
    def getFile(self):
        file_path = QtWidgets.QFileDialog.getOpenFileName(None, 'Open file', '', "Image files (*.jpg *.png *.bmp)")[0]
        if file_path != '':
            self.lineEdit.setText(file_path)

    # Function to display save file dialog
    def saveFile(self):
        output_path = QtWidgets.QFileDialog.getSaveFileName(None, 'Save encoded file', '', "PNG File(*.png)")[0]
        return output_path

    # Function to encode data and save file
    def encode(self):
        input_path = self.lineEdit.text()
        text = self.plainTextEdit.toPlainText()
        password = self.lineEdit_2.text()
        if input_path == '':
            self.displayMsg('Error: No file chosen', 'You must select input image file!', 'err')
        elif text == '':
            self.displayMsg('Text is empty', 'Please enter some text to hide!')
        elif password == '':
            self.displayMsg('Error: No password given', 'Please enter a password!', 'err')
        else:
            output_path = self.saveFile()
            if output_path == '':
                self.displayMsg('Operation cancelled', 'Operation cancelled by user!')
            else:
                try:
                    loss = encode(input_path, text, output_path, password)
                except FileError as fe:
                    self.displayMsg('File Error', str(fe), 'err')
                except DataError as de:
                    self.displayMsg('Data Error', str(de), 'err')
                else:
                    self.displayMsg('Success', 'Encoded Successfully!\n\nImage Data Loss = {:.5f} %'.format(loss))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EncodeWindow = QtWidgets.QMainWindow()
    ui = Ui_EncodeWindow()
    ui.setupUi(EncodeWindow)
    EncodeWindow.show()
    sys.exit(app.exec_())


