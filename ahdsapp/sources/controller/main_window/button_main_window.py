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


class ButtonMainWindow:
	def __init__(self, main_gui) -> None:
		self.main_window = main_gui

	def button_new_device(self) -> None:
		self.main_window.gui_new_device_controller.show()

	def button_edit_device(self) -> None:
		self.main_window.gui_main_windows.pushButton_3.setDisabled(True)

	def button_delete_device(self) -> None:
		self.main_window.gui_main_windows.pushButton_4.setDisabled(True)

	def button_network_map(self) -> None:
		self.main_window.gui_main_windows.pushButton_5.setDisabled(True)
