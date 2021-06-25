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

import sqlite3

from sources.sqlevent.base_class_sql import BaseSQLClass


class SQLLite3Connect(BaseSQLClass):
    def __init__(self) -> None:
        super().__init__()

    def SQLConnect(self, name_db):
        self.connection = sqlite3.Connection(name_db)

        return super().SQLConnect(name_db)
    
    def SQLSaveData(self):
        self.connection.commit()
        print('Save New Device')

        return super().SQLSaveData()
    
    def SQLClose(self):
        self.connection.close()

        return super().SQLClose()
    