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

"""
Project Name: 'lan-map'
Version: 0.1

Description: Network map creation application

Ihor Cheberiak (c) 2021
https://www.linkedin.com/in/ihor-cheberiak/
"""

from sources.viewgui.main_windows import GUI_MainWindow as MainWindow
from sources.control.base_class_controller import BaseControllerClass
from sources.control.new_device_controller import NewDeviceController


class MainWindowsController(BaseControllerClass):
    def __init__(self, language, sql, parent=None):
        super().__init__(parent)
        
        self.ui_main_windows = MainWindow()
        self.ui_main_windows.setupUi(self)

        self.sql_connect = sql

        self.ui_main_windows.pushButton_2.clicked.connect(lambda: self.buttonNewDevice())
        self.ui_main_windows.pushButton_3.clicked.connect(lambda: self.buttonEditDevice())
        self.ui_main_windows.pushButton_4.clicked.connect(lambda: self.buttonDeleteDevice())
        self.ui_main_windows.pushButton_5.clicked.connect(lambda: self.buttonNetworkMap())

    def buttonNewDevice(self):
        self.new_device_controller = NewDeviceController(self.sql_connect)
        self.new_device_controller.show()

    def buttonEditDevice(self):
        self.ui_main_windows.pushButton_3.setDisabled(True)

    def buttonDeleteDevice(self):
        self.ui_main_windows.pushButton_4.setDisabled(True)

    def buttonNetworkMap(self):
        self.ui_main_windows.pushButton_5.setDisabled(True)
