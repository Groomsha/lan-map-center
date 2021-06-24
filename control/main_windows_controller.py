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

from viewgui.main_windows import GUI_MainWindow as MainWindow
from control.base_class_controller import BaseControllerClass
from control.new_device_controller import NewDeviceController
from sources.window.close_event_window import CloseEventWindow as Close


class MainWindowsController(BaseControllerClass):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.ui_main_windows = MainWindow()
        self.ui_main_windows.setupUi(self)

        self.ui_main_windows.pushButton_2.clicked.connect(lambda:self.buttonNewDevice())
        self.ui_main_windows.pushButton_3.clicked.connect(lambda:self.buttonEditDevice())
        self.ui_main_windows.pushButton_4.clicked.connect(lambda:self.buttonDeleteDevice())
        self.ui_main_windows.pushButton_5.clicked.connect(lambda:self.buttonNetworkMap())

    def buttonNewDevice(self):
        self.new_device_controller = NewDeviceController()
        self.new_device_controller.show()

        self.new_device_controller.ui_new_device.buttonBoxNewDevice.accepted.connect(lambda:self.buttonBoxEvent('Seve'))
        self.new_device_controller.ui_new_device.buttonBoxNewDevice.rejected.connect(lambda:self.buttonBoxEvent('Close'))

    def buttonEditDevice(self):
        self.ui_main_windows.pushButton_3.setDisabled(True)

    def buttonDeleteDevice(self):
        self.ui_main_windows.pushButton_4.setDisabled(True)

    def buttonNetworkMap(self):
        self.ui_main_windows.pushButton_5.setDisabled(True)

    def buttonBoxEvent(self, command):
        if command == 'Seve':
            print('Save New Device')
        if command == 'Close':
            Close(self.new_device_controller)

