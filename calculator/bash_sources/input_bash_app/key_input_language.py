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
from bash_sources.input_bash_app.key_input_menu import KeyInputMenu


class KeyInputLanguage:
	def __init__(self, key_menu: KeyInputMenu, settings: Settings) -> None:
		self.settings = settings
		self.menu_reb = key_menu

	def handling_language(self, key_input) -> None:
		if key_input == "7":
			self.settings.current_language = "en"
		elif key_input == "8":
			self.settings.current_language = "ua"
		elif key_input == "9":
			self.settings.current_language = "pl"
		elif key_input == "0":
			self.settings.current_language = "ru"

		self.menu_reb.type_menu = self.menu_reb.menu.creation_menu("language")
