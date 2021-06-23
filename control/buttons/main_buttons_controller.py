
class MainButtonsController():
    def __init__(self, new_device):
        self.new_device_controller = new_device

    def button_new_device(self):
        self.new_device_controller.show()
            