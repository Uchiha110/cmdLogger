import sys
from datetime import datetime

from commands import *
from GUI.cmdDLgui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.receivingAndOutputtingText)

    def receivingAndOutputtingText(self):
        command = self.ui.lineEdit.text()
        listCommand = command.split()

        if listCommand[0] == "help":
            if timeInfoCheck() == 'True':
                self.ui.textBrowser.append(f"\n[{datetime.now()}]\nI help you!!!")
            elif timeInfoCheck() == 'False':
                self.ui.textBrowser.append(f"\nI help you!!!")
            else:
                self.ui.textBrowser.append("\nError")

        elif listCommand[0] == "cls":
            self.ui.textBrowser.clear()

        elif listCommand[0] == "systemNode":
            if timeInfoCheck() == 'True':
                self.ui.textBrowser.append(f"\n[{datetime.now()}]\n{system_node()}")
            elif timeInfoCheck() == 'False':
                self.ui.textBrowser.append(f"\n{system_node()}")
            else:
                self.ui.textBrowser.append("\nError")

        elif listCommand[0] == "systemUserIp":
            if timeInfoCheck() == 'True':
                self.ui.textBrowser.append(f"\n[{datetime.now()}]\n{system_user_ip()}")
            elif timeInfoCheck() == 'False':
                self.ui.textBrowser.append(f"\n{system_user_ip()}")
            else:
                self.ui.textBrowser.append("\nError")

        elif listCommand[0] == "systemPlatform":
            if timeInfoCheck() == 'True':
                self.ui.textBrowser.append(f"\n[{datetime.now()}]\n{system_platform()}")
            elif timeInfoCheck() == 'False':
                self.ui.textBrowser.append(f"\n{system_platform()}")
            else:
                self.ui.textBrowser.append("\nError")

        elif listCommand[0] == "systemProcessor":
            if timeInfoCheck() == 'True':
                self.ui.textBrowser.append(f"\n[{datetime.now()}]\n{system_processor()}")
            elif timeInfoCheck() == 'False':
                self.ui.textBrowser.append(f"\n{system_processor()}")
            else:
                self.ui.textBrowser.append("\nError")

        elif listCommand[0] == 'timeInfo':
            if timeInfoCheck() == 'True':
                self.ui.textBrowser.append(f"\n[{datetime.now()}]\n{timeInfo(listCommand[1])}")
            elif timeInfoCheck() == 'False':
                self.ui.textBrowser.append(f"\n{timeInfo(listCommand[1])}")
            else:
                self.ui.textBrowser.append("\nError")

        elif listCommand[0] == "getCpu":
            if timeInfoCheck() == 'True':
                self.ui.textBrowser.append(f"\n[{datetime.now()}]\n{getCpu()}%")
            elif timeInfoCheck() == 'False':
                self.ui.textBrowser.append(f"\n{getCpu()}%")
            else:
                self.ui.textBrowser.append("\nError")

        elif listCommand[0] == "getScreenshot":
            if timeInfoCheck() == 'True':
                self.ui.textBrowser.append(f"\n[{datetime.now()}]\n{getScreenshot(listCommand[1], listCommand[2])}")
            elif timeInfoCheck() == 'False':
                self.ui.textBrowser.append(f"\n{getScreenshot(listCommand[1], listCommand[2])}")
            else:
                self.ui.textBrowser.append("\nError")

        elif listCommand[0] == "delateScreenshot":
            if timeInfoCheck() == 'True':
                self.ui.textBrowser.append(f"\n[{datetime.now()}]\n{delateScreenshot(listCommand[1], listCommand[2])}")
            elif timeInfoCheck() == 'False':
                self.ui.textBrowser.append(f"\n{delateScreenshot(listCommand[1], listCommand[2])}")
            else:
                self.ui.textBrowser.append("\nError")

        elif listCommand[0] == "closeProg":
            if timeInfoCheck() == 'True':
                self.ui.textBrowser.append(f"\n[{datetime.now()}]\n{closeProg()}")
            elif timeInfoCheck() == 'False':
                self.ui.textBrowser.append(f"\n{closeProg()}")
            else:
                self.ui.textBrowser.append("\nError")

        elif listCommand[0] == "shutdownPc":
            if timeInfoCheck() == 'True':
                self.ui.textBrowser.append(f"\n[{datetime.now()}]\n{shutdownPc()}")
            elif timeInfoCheck() == 'False':
                self.ui.textBrowser.append(f"\n{shutdownPc()}")
            else:
                self.ui.textBrowser.append("\nError")

        elif listCommand[0] == "rebootPc":
            if timeInfoCheck() == 'True':
                self.ui.textBrowser.append(f"\n[{datetime.now()}]\n{rebootPc()}")
            elif timeInfoCheck() == 'False':
                self.ui.textBrowser.append(f"\n{rebootPc()}")
            else:
                self.ui.textBrowser.append("\nError")

        elif listCommand[0] == "sleepPc":
            if timeInfoCheck() == 'True':
                self.ui.textBrowser.append(f"\n[{datetime.now()}]\n{sleepPc()}")
            elif timeInfoCheck() == 'False':
                self.ui.textBrowser.append(f"\n{sleepPc()}")
            else:
                self.ui.textBrowser.append("\nError")
        else:
            if timeInfoCheck() == 'True':
                self.ui.textBrowser.append(f"""\n[{datetime.now()}]\n"{command}" is not internal or external\ncommand, executable program, or batch file.""")
            elif timeInfoCheck() == 'False':
                self.ui.textBrowser.append(f"""\n"{command}" is not internal or external\ncommand, executable program, or batch file.""")
            else:
                self.ui.textBrowser.append("\nError")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
