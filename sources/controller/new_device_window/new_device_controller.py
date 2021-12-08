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

from sources.viewgui.form_new_device.ui_table_new_device import UI_TableNewDevice
from sources.controller.new_device_window.button_new_device import ButtonNewDevice


class NewDeviceController(QtWidgets.QFocusFrame):
    def __init__(self, main_gui, parent=None):
        super().__init__(parent)

        self.connect_sql = main_gui.connect_sql
        self.language_app = main_gui.language_app
        self.settings = main_gui.settings_app

        self.gui_new_device = UI_TableNewDevice()
        self.gui_new_device.setupUi(self)
        self.setWindowModality(2)  # None

        self.btn_new_device = ButtonNewDevice(self)
        self.push_button_new_device()

    def push_button_new_device(self) -> None:
        self.gui_new_device.pushButtonAdd.clicked.connect(lambda: self.btn_new_device.button_add_interface())
        self.gui_new_device.buttonBoxNewDevice.accepted.connect(lambda: self.btn_new_device.button_box_event('Save'))
        self.gui_new_device.buttonBoxNewDevice.rejected.connect(lambda: self.btn_new_device.button_box_event('Close'))
        