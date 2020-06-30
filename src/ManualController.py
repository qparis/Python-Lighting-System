
class ManualController:
    def __init__(self, midiClock, set_current_effect):
        self.midiClock = midiClock
        self.set_current_effect = set_current_effect

    def run(self):
        while True:
            command = input(">>> ")
            try:
                parsed_command = command.split(" ")

                if parsed_command[0] == "m":
                    self.midiClock.set_mutliplier(float(parsed_command[1]))

                if parsed_command[0] == "e":
                    effect = parsed_command[1]
                    self.set_current_effect(effect)

                if parsed_command[0] == "sync":
                    self.midiClock.sync()
            except:
                print("Error!")
