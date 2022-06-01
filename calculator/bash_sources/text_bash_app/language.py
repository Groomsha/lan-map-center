#!/usr/bin/env python3
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

Description: App for calculating masks and subnets

Ihor Cheberiak (c) 2021
https://www.linkedin.com/in/ihor-cheberiak/
"""

import json
from typing import Dict

from settings import Settings


class Language:
	def __init__(self) -> None:
		self.settings = Settings()

		self.language_path = f"language/{self.settings.current_language}.json"
		self.__language_dict = {}

	@property
	def update(self) -> Dict:
		with open(self.language_path, "r") as j:
			self.__language_dict = json.load(j)

		return self.__language_dict
