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


class NewDeviceDataController():
    def __init__(self, ui) -> None:
        self.form_nd = ui

        self.box_nd = BoxNewDevice(self.form_nd)
        self.box_iz = BoxInterfaceZero(self.form_nd)
        self.box_iz = BoxInterfaceAdd(self.form_nd)


class BoxNewDevice():
    def __init__(self, ui) -> None:
        self.form_nd = ui
    
    def getDataBoxND(self):
        self.data_box_ND = {
            'Vendor': self.form_nd.comboBoxVendor.currentText(),
            'Type': self.form_nd.comboBoxType.currentText(),
            'Name': self.form_nd.lineEditName.text()
        }

        return self.data_box_ND
    

class BoxInterfaceZero():
    def __init__(self, ui) -> None:
        self.form_nd = ui
    
    def getInterfaceZeroND(self):
        self.data_interface_zero_ND = {
            'Interface_0': self.form_nd.comboBoxInterface_0.currentText(),
            'InterOne_0': self.form_nd.comboBoxInterOne_0.currentText(),
            'InterTwo_0': self.form_nd.comboBoxInterTwo_0.currentText(),
            'InterThree_0': self.form_nd.comboBoxInterThree_0.currentText(),
            'Pv4_0': self.form_nd.lineEditIPv4_0.text(),
            'Mask_0': self.form_nd.lineEditMask_0.text(),
            'IPv6_0': self.form_nd.lineEditIPv6_0.text(),
            'tPrefix_0': self.form_nd.lineEditPrefix_0.text()
        }

        return self.data_interface_zero_ND

class BoxInterfaceAdd():
    def __init__(self, ui) -> None:
        self.form_nd = ui
    
    def getInterfaceAddND(self):
        pass