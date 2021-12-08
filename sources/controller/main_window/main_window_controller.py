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

from PyQt5 import QtWidgets

from sources.viewgui.app_main_window.ui_app_main_window import Ui_AppMainWindow
from sources.controller.main_window.button_main_window import ButtonMainWindow
from sources.controller.new_device_window.new_device_controller import NewDeviceController


class MainWindowsController(QtWidgets.QMainWindow, QtWidgets.QFocusFrame):
    def __init__(self, language, sql, settings, parent=None) -> None:
        super().__init__(parent)

        self.connect_sql = sql
        self.language_app = language
        self.settings_app = settings

        self.gui_main_windows = Ui_AppMainWindow()
        self.gui_main_windows.setupUi(self)

        self.gui_new_device_controller = NewDeviceController(self)

        self.btn_main_window = ButtonMainWindow(self)
        self.push_button_main_window()

    def push_button_main_window(self) -> None:
        self.gui_main_windows.pushButton_2.clicked.connect(lambda: self.btn_main_window.button_new_device())
        self.gui_main_windows.pushButton_3.clicked.connect(lambda: self.btn_main_window.button_edit_device())
        self.gui_main_windows.pushButton_4.clicked.connect(lambda: self.btn_main_window.button_delete_device())
        self.gui_main_windows.pushButton_5.clicked.connect(lambda: self.btn_main_window.button_network_map())
