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

from typing import Optional, Dict


class SaveDataNewDevice:
    def __init__(self, new_device_gui) -> None:
        self.nd_window = new_device_gui
        self.connect_sql = new_device_gui.connect_sql

        self.box_nd = BoxNewDeviceAdd(self.nd_window)
        self.box_iz = BoxInterfaceAdd(self.nd_window)


class BoxNewDeviceAdd:
    def __init__(self, new_device_gui) -> None:
        self.form_nd = new_device_gui

        self.data_box_ND: Optional = None

    def get_data_box_nd(self) -> Dict:
        self.data_box_ND = {
            'Vendor': self.form_nd.comboBoxVendor.currentText(),
            'Type': self.form_nd.comboBoxType.currentText(),
            'Name': self.form_nd.lineEditName.text()
        }

        return self.data_box_ND


class BoxInterfaceAdd:
    def __init__(self, new_device_gui) -> None:
        self.form_nd = new_device_gui
        self.list_nd = new_device_gui.gui_new_device.interfaseList

        self.data_interface_ND: Dict = {}

    def get_interface_add_nd(self) -> Dict:
        for group in self.list_nd:
            if group == 'groupBoxInterface_0':
                self.data_interface_ND['Interface_0'] = self.form_nd.comboBoxInterface_0.currentText()
                self.data_interface_ND['InterOne_0'] = self.form_nd.comboBoxInterOne_0.currentText(),
                self.data_interface_ND['InterTwo_0'] = self.form_nd.comboBoxInterTwo_0.currentText(),
                self.data_interface_ND['InterThree_0'] = self.form_nd.comboBoxInterThree_0.currentText(),
                self.data_interface_ND['Pv4_0'] = self.form_nd.lineEditIPv4_0.text(),
                self.data_interface_ND['Mask_0'] = self.form_nd.lineEditMask_0.text(),
                self.data_interface_ND['IPv6_0'] = self.form_nd.lineEditIPv6_0.text(),
                self.data_interface_ND['Prefix_0'] = self.form_nd.lineEditPrefix_0.text()
            elif group != 'groupBoxInterface_0':
                for widget in self.form_nd.widgetContentsNewDevice.children():
                    if widget.objectName() == f'groupBoxInterface_{group[18:]}':

                        for child in widget.children():
                            if child.objectName() == f'comboBoxInterface_{group[18:]}':
                                self.data_interface_ND[f'Interface_{group[18:]}'] = child.currentText()
                            elif child.objectName() == f'comboBoxInterOne_{group[18:]}':
                                self.data_interface_ND[f'InterOne_{group[18:]}'] = child.currentText()
                            elif child.objectName() == f'comboBoxInterTwo_{group[18:]}':
                                self.data_interface_ND[f'InterTwo_{group[18:]}'] = child.currentText()
                            elif child.objectName() == f'comboBoxInterThree_{group[18:]}':
                                self.data_interface_ND[f'InterThree_{group[18:]}'] = child.currentText()
                            elif child.objectName() == f'lineEditIPv4_{group[18:]}':
                                self.data_interface_ND[f'Pv4_{group[18:]}'] = child.text()
                            elif child.objectName() == f'lineEditMask_{group[18:]}':
                                self.data_interface_ND[f'Mask_{group[18:]}'] = child.text()
                            elif child.objectName() == f'lineEditIPv6_{group[18:]}':
                                self.data_interface_ND[f'IPv6_{group[18:]}'] = child.text()
                            elif child.objectName() == f'lineEditPrefix_{group[18:]}':
                                self.data_interface_ND[f'Prefix_{group[18:]}'] = child.text()

        return self.data_interface_ND
