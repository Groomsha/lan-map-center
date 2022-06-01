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
from actions_app.ipv4_actions import PoolAssigned
from bash_sources.input_bash_app.key_input_menu import KeyInputMenu


class KeyInputIPv4:
	def __init__(self, key_menu: KeyInputMenu, settings: Settings) -> None:
		self.settings = settings
		self.menu_reb = key_menu

		self.pool = PoolAssigned()

	def handling_ipv4(self, key_input) -> None:
		self.menu_reb.type_menu = self.menu_reb.menu.creation_menu("ipv4")

		if key_input == "l" or key_input == "L":
			self.pool.creation_body("legacy")
		elif key_input == "p" or key_input == "P":
			self.pool.creation_body("private")
		elif key_input == "o" or key_input == "O":
			self.pool.creation_body("other")
		elif key_input == "s" or key_input == "S":
			pass
		elif key_input == "d" or key_input == "D":
			pass
