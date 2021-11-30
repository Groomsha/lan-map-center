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

from PyQt5 import QtCore, QtWidgets

from sources.viewgui.table_new_device.ui_table_new_device import UI_TableNewDevice
from sources.service.close_event_window import CloseEventWindow as Close
from sources.controller.new_device_window.new_device_data_controller import NewDeviceDataController as Data


class NewDeviceController(QtWidgets.QFocusFrame):
    def __init__(self, main_window, parent=None):
        super().__init__(parent)

        self.new_device_data = None
        self.object_button = None
        self.number_interface = None
        self.last_object_button = None
        self.object_box_interface = None
        self.interface_pos_y = None
        self.btn_add_pos_y = None
        self.widget_content_min_hei = None
        self.connect_sql = main_window.connect_sql
        self.language_app = main_window.language_app

        self.ui_new_device = UI_TableNewDevice()
        self.ui_new_device.setupUi(self)
        self.setWindowModality(2)
        
        self.push_button_controller()

    def push_button_controller(self):
        self.ui_new_device.pushButtonAdd.clicked.connect(lambda: self.button_add_interface())
        self.ui_new_device.buttonBoxNewDevice.accepted.connect(lambda: self.button_box_event('Save'))
        self.ui_new_device.buttonBoxNewDevice.rejected.connect(lambda: self.button_box_event('Close'))
    
    def contents_qt_widgets_search(self):
        self.number_interface = len(self.ui_new_device.interfaseList)-1
        
        for i in self.ui_new_device.widgetContentsNewDevice.children():
            if i.objectName() == self.ui_new_device.interfaseList[self.number_interface]:
                return i

    def show_hidden_button_del(self, chek: bool):
        self.object_button = self.contents_qt_widgets_search()
        
        for i in self.object_button.children():
            if self.number_interface >= 2 and self.last_object_button.objectName() == 'pushButtonDel_' + str(self.number_interface-1):
                self.last_object_button.setHidden(True)

            if i.objectName() == 'pushButtonDel_' + str(self.number_interface):
                if not chek:
                    i.clicked.connect(lambda: self.button_delete_interface(self.object_button))

                self.last_object_button = i
                i.setHidden(False)
    
    def button_add_interface(self):
        self.object_box_interface = self.contents_qt_widgets_search()
        
        # Create new Interface
        self.interface_pos_y = self.object_box_interface.y()
        self.ui_new_device.createNewInterface(self.interface_pos_y+100)
        self.show_hidden_button_del(False)

        # Button move new Interface
        self.btn_add_pos_y = self.ui_new_device.pushButtonAdd.y()
        self.ui_new_device.pushButtonAdd.setGeometry(QtCore.QRect(450, self.btn_add_pos_y+100, 31, 23))

        # Move Scroll Area
        self.widget_content_min_hei = self.ui_new_device.widgetContentsNewDevice.minimumHeight()
        self.ui_new_device.widgetContentsNewDevice.setMinimumSize(QtCore.QSize(0, self.widget_content_min_hei+100))

    def button_delete_interface(self, current_object):
        # Delete new Interface
        current_object.deleteLater()
        self.ui_new_device.interfaseList.pop(-1)
        self.show_hidden_button_del(True)
        
        # Button remove new Interface
        self.btn_add_pos_y = self.ui_new_device.pushButtonAdd.y()
        self.ui_new_device.pushButtonAdd.setGeometry(QtCore.QRect(450, self.btn_add_pos_y-100, 31, 23))

        # Remove Scroll Area
        self.widget_content_min_hei = self.ui_new_device.widgetContentsNewDevice.minimumHeight()
        self.ui_new_device.widgetContentsNewDevice.setMinimumSize(QtCore.QSize(0, self.widget_content_min_hei-100))
    
    def button_box_event(self, command):
        if command == 'Save':
            self.new_device_data = Data(self.ui_new_device)
            self.connect_sql.save_data_sql()
        if command == 'Close':
            Close(self)
        