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
Version: 0.3

Description: Script for calculating masks and subnets

Ihor Cheberiak (c) 2021
https://www.linkedin.com/in/ihor-cheberiak/
"""

import sys

from settings import Settings
from bash_sources.text_bash_app.language import Language
from bash_sources.input_bash_app.key_input_menu import KeyInputMenu
from bash_sources.input_bash_app.key_input_ipv4 import KeyInputIPv4
from bash_sources.input_bash_app.key_input_language import KeyInputLanguage


class MainBashApplication:
    def __init__(self) -> None:
        self.settings = Settings()
        self.language = Language()

        self.key_menu = KeyInputMenu(self.language, self.settings)
        self.key_ipv4 = KeyInputIPv4(self.key_menu, self.settings)
        self.key_lang = KeyInputLanguage(self.key_menu, self.settings)

        while True:
            key_input = input(f"{self.key_menu.type_menu} \n{self.language.update['cell_00']}: ")

            if self.settings.current_menu == "main":
                self.key_menu.handling_menu(key_input)

            if self.settings.current_menu == "ipv4":
                self.key_ipv4.handling_ipv4(key_input)

            if self.settings.current_menu == "language":
                self.key_lang.handling_language(key_input)

            if key_input == "r" or key_input == "R":
                self.key_menu.type_menu = self.key_menu.menu.creation_menu("main")
            elif key_input == "q" or key_input == "Q":
                sys.exit()
