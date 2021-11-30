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
from sources.controller.new_device_window.widgets_control_new_device import WidgetsControlNewDevice


class ButtonNewDevice:
	def __init__(self, new_device_gui) -> None:
		self.new_device_window = new_device_gui

		self.btn_add_pos_y = None
		self.new_device_data = None
		self.interface_pos_y = None
		self.object_box_interface = None
		self.widget_content_min_hei = None

		self.nd_control = WidgetsControlNewDevice(self)

	def push_button_new_device(self):
		self.new_device_window.gui_new_device.pushButtonAdd.clicked.connect(lambda: self.button_add_interface())
		self.new_device_window.gui_new_device.buttonBoxNewDevice.accepted.connect(lambda: self.button_box_event('Save'))
		self.new_device_window.gui_new_device.buttonBoxNewDevice.rejected.connect(lambda: self.button_box_event('Close'))

	def button_add_interface(self):
		self.object_box_interface = self.nd_control.search_current_interfase(self.new_device_window.gui_new_device)

		# Create new Interface
		self.interface_pos_y = self.object_box_interface.y()
		self.new_device_window.gui_new_device.createNewInterface(self.interface_pos_y+100)
		self.nd_control.show_hidden_button_del(self.new_device_window.gui_new_device, False)

		# Button move new Interface
		self.btn_add_pos_y = self.new_device_window.gui_new_device.pushButtonAdd.y()
		self.new_device_window.gui_new_device.pushButtonAdd.setGeometry(QtCore.QRect(450, self.btn_add_pos_y+100, 31, 23))

		# Move Scroll Area
		self.widget_content_min_hei = self.new_device_window.gui_new_device.widgetContentsNewDevice.minimumHeight()
		self.new_device_window.gui_new_device.widgetContentsNewDevice.setMinimumSize(QtCore.QSize(0, self.widget_content_min_hei+100))

	def button_delete_interface(self, current_object):
		# Delete new Interface
		current_object.deleteLater()
		self.new_device_window.gui_new_device.interfaseList.pop(-1)
		self.nd_control.show_hidden_button_del(self.new_device_window.gui_new_device, True)

		# Button remove new Interface
		self.btn_add_pos_y = self.new_device_window.gui_new_device.pushButtonAdd.y()
		self.new_device_window.gui_new_device.pushButtonAdd.setGeometry(QtCore.QRect(450, self.btn_add_pos_y-100, 31, 23))

		# Remove Scroll Area
		self.widget_content_min_hei = self.new_device_window.gui_new_device.widgetContentsNewDevice.minimumHeight()
		self.new_device_window.gui_new_device.widgetContentsNewDevice.setMinimumSize(QtCore.QSize(0, self.widget_content_min_hei-100))

	def button_box_event(self, command):
		if command == 'Save':
			# self.new_device_data = Data(self.new_device_window.gui_new_device)
			self.new_device_window.connect_sql.save_data_sql()
		if command == 'Close':
			Close(self.new_device_window)
