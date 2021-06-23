import sys

from PyQt5 import QtCore, QtGui, QtWidgets

from control.main_windows_controller import MainWindowsController
from control.new_device_controller import NewDeviceController

from sources.language import *


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    main_language = LanguageProgram()

    new_device_controller = NewDeviceController()
    main_controller = MainWindowsController(new_device_controller)

    main_controller.show()
    sys.exit(app.exec_())
