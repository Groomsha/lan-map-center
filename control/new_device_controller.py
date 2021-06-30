#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#

from PyQt5 import QtCore, QtGui, QtWidgets

from viewgui.new_device import GUI_FormNewDevice as FormNewDevice
from sources.window.close_event_window import CloseEventWindow as Close
from control.new_device_data_controller import NewDeviceDataController as Data


class NewDeviceController(QtWidgets.QFocusFrame):
    def __init__(self, sql, parent=None):
        super().__init__(parent)

        self.ui_new_device = FormNewDevice()
        self.ui_new_device.setupUi(self)
        self.setWindowModality(2)

        self.sql_connect = sql
        self.lastObjectbutton = None
        
        self.ui_new_device.pushButtonAdd.clicked.connect(lambda:self.buttonAddInterface())
        self.ui_new_device.buttonBoxNewDevice.accepted.connect(lambda:self.buttonBoxEvent('Seve'))
        self.ui_new_device.buttonBoxNewDevice.rejected.connect(lambda:self.buttonBoxEvent('Close'))
    
    def contentsQtWidgetsSersh(self):
        self.nambsInterface = len(self.ui_new_device.interfaseList)-1
        
        for i in self.ui_new_device.widgetContentsNewDevice.children():
            if i.objectName() == self.ui_new_device.interfaseList[self.nambsInterface]:
                return i

    def showHiddenButtonDel(self, chek):
        self.objectbutton = self.contentsQtWidgetsSersh()
        
        for i in self.objectbutton.children():
            if self.nambsInterface >= 2 and self.lastObjectbutton.objectName() == 'pushButtonDel_' + str(self.nambsInterface-1):
                self.lastObjectbutton.setHidden(True)

            if i.objectName() == 'pushButtonDel_' + str(self.nambsInterface):
                if chek == False:
                    i.clicked.connect(lambda:self.buttonDeleteInterface(self.objectbutton))

                self.lastObjectbutton = i
                i.setHidden(False)
    
    def buttonAddInterface(self):
        self.objectBoxInterface = self.contentsQtWidgetsSersh()
        
        # Create new Interface
        self.interfasePosY = self.objectBoxInterface.y()
        self.ui_new_device.createNewInterface(self.interfasePosY+100)
        self.showHiddenButtonDel(False)

        # Button move new Interface
        self.btnAddPosY = self.ui_new_device.pushButtonAdd.y()
        self.ui_new_device.pushButtonAdd.setGeometry(QtCore.QRect(450, self.btnAddPosY+100, 31, 23))

        # Move Scroll Area
        self.widgetContentMinHei = self.ui_new_device.widgetContentsNewDevice.minimumHeight()
        self.ui_new_device.widgetContentsNewDevice.setMinimumSize(QtCore.QSize(0, self.widgetContentMinHei+100))

    def buttonDeleteInterface(self, currentObject):
        # Delete new Interface
        currentObject.deleteLater()
        self.ui_new_device.interfaseList.pop(-1)
        self.showHiddenButtonDel(True)
        
        # Button remove new Interface
        self.btnAddPosY = self.ui_new_device.pushButtonAdd.y()
        self.ui_new_device.pushButtonAdd.setGeometry(QtCore.QRect(450, self.btnAddPosY-100, 31, 23))

        # Remove Scroll Area
        self.widgetContentMinHei = self.ui_new_device.widgetContentsNewDevice.minimumHeight()
        self.ui_new_device.widgetContentsNewDevice.setMinimumSize(QtCore.QSize(0, self.widgetContentMinHei-100))
    
    def buttonBoxEvent(self, command):
        if command == 'Seve':
            self.new_device_data = Data(self.ui_new_device)
            self.sql_connect.SQLSaveData()
        if command == 'Close':
            Close(self)
        