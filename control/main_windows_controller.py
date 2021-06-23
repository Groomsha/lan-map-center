from PyQt5 import QtCore, QtGui, QtWidgets

from viewgui.main_windows import GUI_MainWindow as MainWindow
from control.buttons.main_buttons_controller import MainButtonsController


class MainWindowsController(QtWidgets.QMainWindow):
    def __init__(self, new_device, parent=None):
        super().__init__(parent)
        
        self.ui_main_windows = MainWindow()
        self.ui_main_windows.setupUi(self)

        self.new_device_controller = new_device
        
        self.push_buttons()
    
    def push_buttons(self):
        self.buttons = MainButtonsController(self.new_device_controller)
        
        self.ui_main_windows.pushButton_2.clicked.connect(lambda:self.buttons.button_new_device())
        #self.ui_main_windows.pushButton_3.clicked.connect(lambda:self.buttons.button_new_device("new"))
        #self.ui_main_windows.pushButton_4.clicked.connect(lambda:self.buttons.button_new_device("new"))
        self.ui_main_windows.pushButton_5.setDisabled(True)
