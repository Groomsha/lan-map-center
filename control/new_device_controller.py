from PyQt5 import QtCore, QtGui, QtWidgets

from viewgui.new_device import GUI_FormNewDevice as FormNewDevice


class NewDeviceController(QtWidgets.QFocusFrame):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui_new_device = FormNewDevice()
        self.ui_new_device.setupUi(self)
        self.setWindowModality(2)

        self.lastObjectbutton = None
        self.ui_new_device.pushButtonAdd.clicked.connect(lambda:self.addInterface())
    
    def contentsQtWidgetsSersh(self):
        self.nambsInterface = len(self.ui_new_device.interfaseList)-1
        
        for i in self.ui_new_device.widgetContentsNewDevice.children():
            if i.objectName() == self.ui_new_device.interfaseList[self.nambsInterface]:
                return i

    def buttonDelShowHidden(self, chek):
        self.objectbutton = self.contentsQtWidgetsSersh()
        
        for i in self.objectbutton.children():
            if self.nambsInterface >= 2 and self.lastObjectbutton.objectName() == 'pushButtonDel_' + str(self.nambsInterface-1):
                self.lastObjectbutton.setHidden(True)

            if i.objectName() == 'pushButtonDel_' + str(self.nambsInterface):
                if chek == False:
                    i.clicked.connect(lambda:self.deleteInterface(self.objectbutton))

                self.lastObjectbutton = i
                i.setHidden(False)
    
    def addInterface(self):
        self.objectBoxInterface = self.contentsQtWidgetsSersh()
        
        # Create new Interface
        self.interfasePosY = self.objectBoxInterface.y()
        self.ui_new_device.createNewInterface(self.interfasePosY+100)
        self.buttonDelShowHidden(False)

        # Button move new Interface
        self.btnAddPosY = self.ui_new_device.pushButtonAdd.y()
        self.ui_new_device.pushButtonAdd.setGeometry(QtCore.QRect(450, self.btnAddPosY+100, 31, 23))

        # Move Scroll Area
        self.widgetContentMinHei = self.ui_new_device.widgetContentsNewDevice.minimumHeight()
        self.ui_new_device.widgetContentsNewDevice.setMinimumSize(QtCore.QSize(0, self.widgetContentMinHei+100))

    def deleteInterface(self, currentObject):
        # Delete new Interface
        currentObject.deleteLater()
        self.ui_new_device.interfaseList.pop(-1)
        self.buttonDelShowHidden(True)
        
        # Button remove new Interface
        self.btnAddPosY = self.ui_new_device.pushButtonAdd.y()
        self.ui_new_device.pushButtonAdd.setGeometry(QtCore.QRect(450, self.btnAddPosY-100, 31, 23))

        # Remove Scroll Area
        self.widgetContentMinHei = self.ui_new_device.widgetContentsNewDevice.minimumHeight()
        self.ui_new_device.widgetContentsNewDevice.setMinimumSize(QtCore.QSize(0, self.widgetContentMinHei-100))
        