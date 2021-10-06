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

from PyQt5 import QtCore, QtWidgets

from sources.viewgui.ui_form_new_device import Ui_FormNewDevice as FormNewDevice


class UI_TableNewDevice(FormNewDevice):
    def __init__(self) -> None:
        super().__init__()
        
        self.interfaseList = ['groupBoxInterface_0']
        self._translate = QtCore.QCoreApplication.translate

    def createNewInterface(self, x_pos):
        intNamb = '_' + str(len(self.interfaseList))
        
        self.groupBoxInterface = QtWidgets.QGroupBox(self.widgetContentsNewDevice)
        self.groupBoxInterface.setGeometry(QtCore.QRect(0, x_pos, 491, 101))
        self.groupBoxInterface.setObjectName("groupBoxInterface" + intNamb)
        self.labelIPv4 = QtWidgets.QLabel(self.groupBoxInterface)
        self.labelIPv4.setGeometry(QtCore.QRect(160, 20, 31, 16))
        self.labelIPv4.setObjectName("labelIPv4" + intNamb)
        self.labelIPv6 = QtWidgets.QLabel(self.groupBoxInterface)
        self.labelIPv6.setGeometry(QtCore.QRect(160, 50, 31, 16))
        self.labelIPv6.setObjectName("labelIPv6" + intNamb)
        self.labelMask = QtWidgets.QLabel(self.groupBoxInterface)
        self.labelMask.setGeometry(QtCore.QRect(330, 20, 31, 16))
        self.labelMask.setObjectName("labelMask" + intNamb)
        self.labelPrefix = QtWidgets.QLabel(self.groupBoxInterface)
        self.labelPrefix.setGeometry(QtCore.QRect(330, 50, 31, 16))
        self.labelPrefix.setObjectName("labelPrefix" + intNamb)
        
        self.comboBoxInterface = QtWidgets.QComboBox(self.groupBoxInterface)
        self.comboBoxInterface.setGeometry(QtCore.QRect(10, 20, 141, 22))
        self.comboBoxInterface.setObjectName("comboBoxInterface" + intNamb)
        self.comboBoxInterface.addItem("")
        self.comboBoxInterface.addItem("")
        self.comboBoxInterface.addItem("")
        self.comboBoxInterface.addItem("")
        self.comboBoxInterface.addItem("")
        self.comboBoxInterface.addItem("")
        self.comboBoxInterface.addItem("")

        self.comboBoxInterOne = QtWidgets.QComboBox(self.groupBoxInterface)
        self.comboBoxInterOne.setGeometry(QtCore.QRect(10, 50, 41, 22))
        self.comboBoxInterOne.setObjectName("comboBoxInterOne" + intNamb)
        self.comboBoxInterOne.addItem("")
        self.comboBoxInterOne.addItem("")
        self.comboBoxInterOne.addItem("")
        self.comboBoxInterOne.addItem("")
        self.comboBoxInterOne.addItem("")
        self.comboBoxInterOne.addItem("")
        self.comboBoxInterOne.addItem("")
        self.comboBoxInterOne.addItem("")
        self.comboBoxInterOne.addItem("")
        self.comboBoxInterOne.addItem("")

        self.comboBoxInterTwo = QtWidgets.QComboBox(self.groupBoxInterface)
        self.comboBoxInterTwo.setGeometry(QtCore.QRect(60, 50, 41, 22))
        self.comboBoxInterTwo.setObjectName("comboBoxInterTwo" + intNamb)
        self.comboBoxInterTwo.addItem("")
        self.comboBoxInterTwo.addItem("")
        self.comboBoxInterTwo.addItem("")
        self.comboBoxInterTwo.addItem("")
        self.comboBoxInterTwo.addItem("")
        self.comboBoxInterTwo.addItem("")
        self.comboBoxInterTwo.addItem("")
        self.comboBoxInterTwo.addItem("")
        self.comboBoxInterTwo.addItem("")
        self.comboBoxInterTwo.addItem("")

        self.comboBoxInterThree = QtWidgets.QComboBox(self.groupBoxInterface)
        self.comboBoxInterThree.setGeometry(QtCore.QRect(110, 50, 41, 22))
        self.comboBoxInterThree.setObjectName("comboBoxInterThree" + intNamb)
        self.comboBoxInterThree.addItem("")
        self.comboBoxInterThree.addItem("")
        self.comboBoxInterThree.addItem("")
        self.comboBoxInterThree.addItem("")
        self.comboBoxInterThree.addItem("")
        self.comboBoxInterThree.addItem("")
        self.comboBoxInterThree.addItem("")
        self.comboBoxInterThree.addItem("")
        self.comboBoxInterThree.addItem("")
        self.comboBoxInterThree.addItem("")
        self.comboBoxInterThree.addItem("")
        self.comboBoxInterThree.addItem("")
        self.comboBoxInterThree.addItem("")
        self.comboBoxInterThree.addItem("")
        self.comboBoxInterThree.addItem("")
        self.comboBoxInterThree.addItem("")
        self.comboBoxInterThree.addItem("")
        self.comboBoxInterThree.addItem("")
        self.comboBoxInterThree.addItem("")
        self.comboBoxInterThree.addItem("")
        self.comboBoxInterThree.addItem("")
        self.comboBoxInterThree.addItem("")
        self.comboBoxInterThree.addItem("")
        self.comboBoxInterThree.addItem("")
        self.comboBoxInterThree.addItem("")
        self.comboBoxInterThree.addItem("")
        self.comboBoxInterThree.addItem("")
        self.comboBoxInterThree.addItem("")
        self.comboBoxInterThree.addItem("")
        self.comboBoxInterThree.addItem("")
        self.comboBoxInterThree.addItem("")
        self.comboBoxInterThree.addItem("")
        self.comboBoxInterThree.addItem("")
        self.comboBoxInterThree.addItem("")
        self.comboBoxInterThree.addItem("")
        self.comboBoxInterThree.addItem("")
        self.comboBoxInterThree.addItem("")
        self.comboBoxInterThree.addItem("")
        self.comboBoxInterThree.addItem("")
        self.comboBoxInterThree.addItem("")
        self.comboBoxInterThree.addItem("")
        self.comboBoxInterThree.addItem("")
        self.comboBoxInterThree.addItem("")
        self.comboBoxInterThree.addItem("")
        self.comboBoxInterThree.addItem("")
        self.comboBoxInterThree.addItem("")
        self.comboBoxInterThree.addItem("")
        self.comboBoxInterThree.addItem("")
        self.comboBoxInterThree.addItem("")

        self.lineEditIPv4 = QtWidgets.QLineEdit(self.groupBoxInterface)
        self.lineEditIPv4.setGeometry(QtCore.QRect(190, 20, 131, 20))
        self.lineEditIPv4.setMaxLength(15)
        self.lineEditIPv4.setObjectName("lineEditIPv4" + intNamb)
        self.lineEditIPv6 = QtWidgets.QLineEdit(self.groupBoxInterface)
        self.lineEditIPv6.setGeometry(QtCore.QRect(190, 50, 131, 20))
        self.lineEditIPv6.setMaxLength(64)
        self.lineEditIPv6.setObjectName("lineEditIPv6" + intNamb)
        self.lineEditMask = QtWidgets.QLineEdit(self.groupBoxInterface)
        self.lineEditMask.setGeometry(QtCore.QRect(360, 20, 121, 20))
        self.lineEditMask.setMaxLength(15)
        self.lineEditMask.setObjectName("lineEditMask" + intNamb)
        self.lineEditPrefix = QtWidgets.QLineEdit(self.groupBoxInterface)
        self.lineEditPrefix.setGeometry(QtCore.QRect(360, 50, 80, 20))
        self.lineEditPrefix.setMaxLength(3)
        self.lineEditPrefix.setObjectName("lineEditPrefix" + intNamb)
        
        self.pushButtonDel = QtWidgets.QPushButton(self.groupBoxInterface)
        self.pushButtonDel.setGeometry(QtCore.QRect(450, 70, 31, 23))
        self.pushButtonDel.setObjectName("pushButtonDel" + intNamb)
        self.pushButtonDel.setHidden(True)
        
        self.interfaseList.append('groupBoxInterface' + intNamb)
        
        self.retranslateCreateNewInterface()
        self.groupBoxInterface.setVisible(True)

    def retranslateCreateNewInterface(self):
        self.groupBoxInterface.setTitle(self._translate("FormNewDevice", "Interface-" + str(len(self.interfaseList)-1)))

        self.labelIPv4.setText(self._translate("FormNewDevice", "IPv4"))
        self.labelIPv6.setText(self._translate("FormNewDevice", "IPv6"))
        self.labelMask.setText(self._translate("FormNewDevice", "Mask"))
        self.labelPrefix.setText(self._translate("FormNewDevice", "Prefix"))

        self.comboBoxInterface.setItemText(0, self._translate("FormNewDevice", "Ethernet 10 Mb/s"))
        self.comboBoxInterface.setItemText(1, self._translate("FormNewDevice", "Ethernet 100 Mb/s"))
        self.comboBoxInterface.setItemText(2, self._translate("FormNewDevice", "Ethernet 1 Gb/s"))
        self.comboBoxInterface.setItemText(3, self._translate("FormNewDevice", "Ethernet 10 Gb/s"))
        self.comboBoxInterface.setItemText(4, self._translate("FormNewDevice", "VLAN (Switch)"))
        self.comboBoxInterface.setItemText(5, self._translate("FormNewDevice", "Serial"))
        self.comboBoxInterface.setItemText(6, self._translate("FormNewDevice", "SFP"))

        self.comboBoxInterOne.setItemText(0, self._translate("FormNewDevice", "0"))
        self.comboBoxInterOne.setItemText(1, self._translate("FormNewDevice", "1"))
        self.comboBoxInterOne.setItemText(2, self._translate("FormNewDevice", "2"))
        self.comboBoxInterOne.setItemText(3, self._translate("FormNewDevice", "3"))
        self.comboBoxInterOne.setItemText(4, self._translate("FormNewDevice", "4"))
        self.comboBoxInterOne.setItemText(5, self._translate("FormNewDevice", "5"))
        self.comboBoxInterOne.setItemText(6, self._translate("FormNewDevice", "6"))
        self.comboBoxInterOne.setItemText(7, self._translate("FormNewDevice", "7"))
        self.comboBoxInterOne.setItemText(8, self._translate("FormNewDevice", "8"))
        self.comboBoxInterOne.setItemText(9, self._translate("FormNewDevice", "9"))

        self.comboBoxInterTwo.setItemText(0, self._translate("FormNewDevice", "0"))
        self.comboBoxInterTwo.setItemText(1, self._translate("FormNewDevice", "1"))
        self.comboBoxInterTwo.setItemText(2, self._translate("FormNewDevice", "2"))
        self.comboBoxInterTwo.setItemText(3, self._translate("FormNewDevice", "3"))
        self.comboBoxInterTwo.setItemText(4, self._translate("FormNewDevice", "4"))
        self.comboBoxInterTwo.setItemText(5, self._translate("FormNewDevice", "5"))
        self.comboBoxInterTwo.setItemText(6, self._translate("FormNewDevice", "6"))
        self.comboBoxInterTwo.setItemText(7, self._translate("FormNewDevice", "7"))
        self.comboBoxInterTwo.setItemText(8, self._translate("FormNewDevice", "8"))
        self.comboBoxInterTwo.setItemText(9, self._translate("FormNewDevice", "9"))

        self.comboBoxInterThree.setItemText(0, self._translate("FormNewDevice", "0"))
        self.comboBoxInterThree.setItemText(1, self._translate("FormNewDevice", "1"))
        self.comboBoxInterThree.setItemText(2, self._translate("FormNewDevice", "2"))
        self.comboBoxInterThree.setItemText(3, self._translate("FormNewDevice", "3"))
        self.comboBoxInterThree.setItemText(4, self._translate("FormNewDevice", "4"))
        self.comboBoxInterThree.setItemText(5, self._translate("FormNewDevice", "5"))
        self.comboBoxInterThree.setItemText(6, self._translate("FormNewDevice", "6"))
        self.comboBoxInterThree.setItemText(7, self._translate("FormNewDevice", "7"))
        self.comboBoxInterThree.setItemText(8, self._translate("FormNewDevice", "8"))
        self.comboBoxInterThree.setItemText(9, self._translate("FormNewDevice", "9"))
        self.comboBoxInterThree.setItemText(10, self._translate("FormNewDevice", "10"))
        self.comboBoxInterThree.setItemText(11, self._translate("FormNewDevice", "11"))
        self.comboBoxInterThree.setItemText(12, self._translate("FormNewDevice", "12"))
        self.comboBoxInterThree.setItemText(13, self._translate("FormNewDevice", "13"))
        self.comboBoxInterThree.setItemText(14, self._translate("FormNewDevice", "14"))
        self.comboBoxInterThree.setItemText(15, self._translate("FormNewDevice", "15"))
        self.comboBoxInterThree.setItemText(16, self._translate("FormNewDevice", "16"))
        self.comboBoxInterThree.setItemText(17, self._translate("FormNewDevice", "17"))
        self.comboBoxInterThree.setItemText(18, self._translate("FormNewDevice", "18"))
        self.comboBoxInterThree.setItemText(19, self._translate("FormNewDevice", "19"))
        self.comboBoxInterThree.setItemText(20, self._translate("FormNewDevice", "20"))
        self.comboBoxInterThree.setItemText(21, self._translate("FormNewDevice", "21"))
        self.comboBoxInterThree.setItemText(22, self._translate("FormNewDevice", "22"))
        self.comboBoxInterThree.setItemText(23, self._translate("FormNewDevice", "23"))
        self.comboBoxInterThree.setItemText(24, self._translate("FormNewDevice", "24"))
        self.comboBoxInterThree.setItemText(25, self._translate("FormNewDevice", "25"))
        self.comboBoxInterThree.setItemText(26, self._translate("FormNewDevice", "26"))
        self.comboBoxInterThree.setItemText(27, self._translate("FormNewDevice", "27"))
        self.comboBoxInterThree.setItemText(28, self._translate("FormNewDevice", "28"))
        self.comboBoxInterThree.setItemText(29, self._translate("FormNewDevice", "29"))
        self.comboBoxInterThree.setItemText(30, self._translate("FormNewDevice", "30"))
        self.comboBoxInterThree.setItemText(31, self._translate("FormNewDevice", "31"))
        self.comboBoxInterThree.setItemText(32, self._translate("FormNewDevice", "32"))
        self.comboBoxInterThree.setItemText(33, self._translate("FormNewDevice", "33"))
        self.comboBoxInterThree.setItemText(34, self._translate("FormNewDevice", "34"))
        self.comboBoxInterThree.setItemText(35, self._translate("FormNewDevice", "35"))
        self.comboBoxInterThree.setItemText(36, self._translate("FormNewDevice", "36"))
        self.comboBoxInterThree.setItemText(37, self._translate("FormNewDevice", "37"))
        self.comboBoxInterThree.setItemText(38, self._translate("FormNewDevice", "38"))
        self.comboBoxInterThree.setItemText(39, self._translate("FormNewDevice", "39"))
        self.comboBoxInterThree.setItemText(40, self._translate("FormNewDevice", "40"))
        self.comboBoxInterThree.setItemText(41, self._translate("FormNewDevice", "41"))
        self.comboBoxInterThree.setItemText(42, self._translate("FormNewDevice", "42"))
        self.comboBoxInterThree.setItemText(43, self._translate("FormNewDevice", "43"))
        self.comboBoxInterThree.setItemText(44, self._translate("FormNewDevice", "44"))
        self.comboBoxInterThree.setItemText(45, self._translate("FormNewDevice", "45"))
        self.comboBoxInterThree.setItemText(46, self._translate("FormNewDevice", "46"))
        self.comboBoxInterThree.setItemText(47, self._translate("FormNewDevice", "47"))
        self.comboBoxInterThree.setItemText(48, self._translate("FormNewDevice", "48"))

        self.pushButtonDel.setText(self._translate("FormNewDevice", "-"))

        