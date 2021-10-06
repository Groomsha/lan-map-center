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

import sys

from PyQt5 import QtWidgets

from sources.language.language_program_en import LanguageProgramEN
from sources.sqlevent.sqllite3_connect import SQLLite3Connect
from sources.control.main_windows_controller import MainWindowsController


class MainApp:
    def __init__(self):
        self.language = LanguageProgramEN()
        self.data_sql = SQLLite3Connect()

        self.application = QtWidgets.QApplication(sys.argv)
        self.main_controller = MainWindowsController(self.language, self.data_sql)

    def run_app(self):
        self.data_sql.connect_sql('hardware.db')

        self.main_controller.show()

        sys.exit(self.application.exec_())


if __name__ == "__main__":
    app = MainApp()
    app.run_app()
