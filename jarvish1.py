
import sys
from PyQt5.Qtwidgets import Qwidget
from PyQt5.Qtwidgets import QApplication
from PyQt5.Qtwidgets import QTGui

from mainGUI import ui_mainGUIfile

class mainFile(Qwidget):
    def __int__(self):
        super(mainFile,self).__init__()
        print("Main File")
        self.mainUI=UI_mainGUIfile()
        self.mainUI.setupUi(self)

        self.mainUI.movie=QTGui.movie("")
        self.mainUI.label

        self.mainUI.pushButton_3.clicked.connect(self,close)


if __name__=='__main__':
    app=QApplication(sys.argv)
    ui=mainFile()
    ui.show()
    sys.exit(app.exec_())


from loginWindowsGUI import Ui_Form
class loginWindows(Qwidget):



