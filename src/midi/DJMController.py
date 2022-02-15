class DJMController:
    def __init__(self):
        self.state = {}
        self.update_control_callback = None

    control_map = {
        11: "FADER"
    }

    def set_update_control_callback(self, update_control_callback):
        self.update_control_callback = update_control_callback

    def process_control(self, payload):
        control = payload[1]
        if control in DJMController.control_map:
            command_name = DJMController.control_map[control]
            self.state[command_name] = payload[2]

            if self.update_control_callback is not None:
                self.update_control_callback(self.state)
