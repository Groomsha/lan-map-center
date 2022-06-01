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
Project Name: 'ip-calculator'
Version: 0.1

Description: Script for calculating masks and subnets

Ihor Cheberiak (c) 2021
https://www.linkedin.com/in/ihor-cheberiak/
"""

from settings import Settings
from bash_sources.text_bash_app.text_menu import TextMenu
from bash_sources.text_bash_app.language import Language


class KeyInputMenu:
	def __init__(self, language: Language, settings: Settings) -> None:
		self.menu = TextMenu(language, settings)

		self.type_menu = self.menu.creation_menu("main")

	def handling_menu(self, key_input) -> None:
		if key_input == "1":
			self.type_menu = self.menu.creation_menu("ipv4")
		elif key_input == "2":
			self.type_menu = self.menu.creation_menu("ipv6")
		elif key_input == "3":
			self.type_menu = self.menu.creation_menu("language")
