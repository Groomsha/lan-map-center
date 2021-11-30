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

from PyQt5 import QtCore

from sources.service.close_event_window import CloseEventWindow as Close
from sources.controller.new_device_window.save_data_new_device import SaveDataNewDevice
from sources.controller.new_device_window.widgets_control_new_device import WidgetsControlNewDevice


class ButtonNewDevice:
	def __init__(self, new_device_gui) -> None:
		self.nd_window = new_device_gui

		self.nd_control = WidgetsControlNewDevice(self)
		self.save_data = SaveDataNewDevice(self.nd_window)

	def button_add_interface(self):
		object_box_interface = self.nd_control.search_current_interfase(self.nd_window.gui_new_device)

		# Create new Interface
		interface_pos_y = object_box_interface.y()
		self.nd_window.gui_new_device.createNewInterface(interface_pos_y + 100)
		self.nd_control.show_hidden_button_del(self.nd_window.gui_new_device, False)

		# Button move new Interface
		btn_add_pos_y = self.nd_window.gui_new_device.pushButtonAdd.y()
		self.nd_window.gui_new_device.pushButtonAdd.setGeometry(QtCore.QRect(450, btn_add_pos_y + 100, 31, 23))

		# Move Scroll Area
		widget_content_min_hei = self.nd_window.gui_new_device.widgetContentsNewDevice.minimumHeight()
		self.nd_window.gui_new_device.widgetContentsNewDevice.setMinimumSize(QtCore.QSize(0, widget_content_min_hei + 100))

	def button_delete_interface(self, current_object):
		# Delete new Interface
		current_object.deleteLater()
		self.nd_window.gui_new_device.interfaseList.pop(-1)
		self.nd_control.show_hidden_button_del(self.nd_window.gui_new_device, True)

		# Button remove new Interface
		btn_add_pos_y = self.nd_window.gui_new_device.pushButtonAdd.y()
		self.nd_window.gui_new_device.pushButtonAdd.setGeometry(QtCore.QRect(450, btn_add_pos_y - 100, 31, 23))

		# Remove Scroll Area
		widget_content_min_hei = self.nd_window.gui_new_device.widgetContentsNewDevice.minimumHeight()
		self.nd_window.gui_new_device.widgetContentsNewDevice.setMinimumSize(QtCore.QSize(0, widget_content_min_hei - 100))

	def button_box_event(self, command):
		if command == 'Save':
			self.save_data.connect_sql.save_data_sql()  # Test str.
		if command == 'Close':
			Close(self.nd_window)
