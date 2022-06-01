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


class PoolAssigned:
	def __init__(self) -> None:
		self.console = TextConsole()

		self.legacy_addressing: Dict = {"Class A": "0.0.0.0/8 to 127.0.0.0/8",
										"Class B": "128.0.0.0/16 to 191.255.0.0/16",
										"Class C": "192.0.0.0/24 to 223.255.255.0/24",
										"Class D": "224.0.0.0/8 to 239.0.0.0/8",
										"Class E": "240.0.0.0/8 to 255.0.0.0"}

		self.private_addressing: Dict = {"One": "10.0.0.0/8 to 10.255.255.255/8",
										 "Two": "172.16.0.0/16 to 172.31.255.255/16",
										 "Three": "192.168.0.0/24 to 192.168.255.255/24"}

		self.other_addressing: Dict = {"Loopback": "127.0.0.0/8 to 127.255.255.255/8",
									   "link-local": "169.254.0.0/16 to 169.254.255.254/16",
									   "Test-Net": "192.0.2.0/24 to 192.0.2.255/24",
									   "Experimental": "240.0.0.0 to 255.255.255.255",
									   "Multicast": "224.0.0.0 to 239.255.255.255",
									   "Reserved": "224.0.0.0 to 224.0.0.255"}

	def preparation_pool(self, networks_type: str) -> str:
		self.console.clear()

		networks_dict: Dict = {}
		string_data: str = ""

		if networks_type == "legacy":
			networks_dict = self.legacy_addressing
		elif networks_type == "private":
			networks_dict = self.private_addressing
		elif networks_type == "other":
			networks_dict = self.other_addressing

		for key, value in networks_dict.items():
			string_data += f"\n{key} - {value}"

		return string_data

	def creation_body(self, body_type: str) -> None:
		print(self.preparation_pool(body_type))
