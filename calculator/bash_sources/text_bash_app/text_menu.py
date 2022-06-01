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

from typing import Dict
from bash_sources.text_bash_app.text_console import TextConsole


class TextMenu:
	def __init__(self, language, settings) -> None:
		self.settings = settings
		self.lang = language

		self.console = TextConsole()

	def creation_text(self, menu_type: str) -> Dict:
		self.settings.current_menu = menu_type

		if menu_type == "main":
			return {
				"1": self.lang.language_dict['cell_01'],
				"2": self.lang.language_dict['cell_02'],
				"3": self.lang.language_dict['cell_03'],
				"Q": self.lang.language_dict['cell_05']
			}
		elif menu_type == "ipv4":
			return {
				"s": self.lang.language_dict['cell_09'],
				"d": self.lang.language_dict['cell_10'],
				"p": self.lang.language_dict['cell_11'],
				"l": self.lang.language_dict['cell_12'],
				"o": self.lang.language_dict['cell_13'],
				"R": self.lang.language_dict['cell_04'],
				"Q": self.lang.language_dict['cell_05']
			}
		elif menu_type == "ipv6":
			return {
				"R": self.lang.language_dict['cell_04'],
				"Q": self.lang.language_dict['cell_05']
			}
		elif menu_type == "language":
			return {
				"7": self.lang.language_dict['cell_06'],
				"8": self.lang.language_dict['cell_07'],
				"9": self.lang.language_dict['cell_14'],
				"0": self.lang.language_dict['cell_08'],
				"R": self.lang.language_dict['cell_04'],
				"Q": self.lang.language_dict['cell_05']
			}

	def creation_menu(self, menu_type: str) -> str:
		self.lang.update()
		self.console.clear()

		string_menu: str = ""
		if menu_type == "main":
			string_menu = f"IP Calculator {self.settings.version_app}\n"

		for key, value in self.creation_text(menu_type).items():
			string_menu += f"\n{key} - {value}"

		string_menu += "\n"
		return string_menu
