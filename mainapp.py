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

import sys

from PyQt5 import QtWidgets

from sources.language.languageProgram import LanguageProgram
from sources.sqlevent.sqllite3_connect import SQLLite3Connect
from sources.control.main_windows_controller import MainWindowsController


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    main_sql = SQLLite3Connect()
    main_sql.SQLConnect('hardware.db')

    main_language = LanguageProgram()
    main_controller = MainWindowsController(main_sql)

    main_controller.show()
    sys.exit(app.exec_())
