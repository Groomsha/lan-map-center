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


class WidgetsControlNewDevice:
	def __init__(self, button) -> None:
		self.nd_button = button

		self.number_interface = None
		self.object_button = None
		self.last_object_button = None

	def search_current_interfase(self, new_device_gui):
		self.number_interface = len(new_device_gui.interfaseList)-1

		for i in new_device_gui.widgetContentsNewDevice.children():
			if i.objectName() == new_device_gui.interfaseList[self.number_interface]:
				return i

	def show_hidden_button_del(self, new_device_gui, chek: bool):
		self.object_button = self.search_current_interfase(new_device_gui)

		for i in self.object_button.children():
			current_object_name = f'pushButtonDel_{str(self.number_interface - 1)}'

			if self.number_interface >= 2 and self.last_object_button.objectName() == current_object_name:
				self.last_object_button.setHidden(True)

			if i.objectName() == f'pushButtonDel_{str(self.number_interface)}':
				if not chek:
					i.clicked.connect(lambda: self.nd_button.button_delete_interface(self.object_button))

				self.last_object_button = i
				self.last_object_button.setHidden(False)
