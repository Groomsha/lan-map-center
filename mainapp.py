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

from sources.settings import Settings
from sources.sqlevent.sqllite3_connect import SQLLite3Connect
from sources.service.language_event_window import LanguageEventWindow
from sources.controller.main_window.main_window_controller import MainWindowsController


class MainApp:
    def __init__(self):
        self.settings_app = Settings()
        self.data_sql_app = SQLLite3Connect()
        self.language_app = LanguageEventWindow(self.settings_app)

        self.qt_main_app = None
        self.application = None

    def run_app(self):
        self.qt_main_app = QtWidgets.QApplication(sys.argv)
        self.data_sql_app.connect_sql(self.settings_app.db_name)

        self.application = MainWindowsController(self.language_app, self.data_sql_app, self.settings_app)
        self.application.show()

        sys.exit(self.qt_main_app.exec_())


if __name__ == "__main__":
    app = MainApp()
    app.run_app()
