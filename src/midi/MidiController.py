import logging
import threading

from rtmidi.midiutil import open_midiinput

log = logging.getLogger('midiin_poll')
logging.basicConfig(level=logging.DEBUG)


class MidiController:
    def __init__(self, midiClock, denonHc4500Controller, enableDJM = False, djmController = None):
        self._running = True
        self.__initialize(enableDJM)
        self.midiClock = midiClock
        self.denonHc4500Controller = denonHc4500Controller
        self.enableDJM = enableDJM
        self.djmController = djmController

    def __initialize(self, enableDJM):
        self.midiin, port_name = open_midiinput("Traktor Virtual Output")
        print("Midi device: %s" % port_name)

        if enableDJM:
            self.djm850_midiiin, port_name_djm = open_midiinput("USB MIDI")
            print("Midi device: %s" % port_name_djm)

        self.midiin.ignore_types(False, False, False)

    def stop(self):
        self._running = False

    def start(self):
        self.midiin.set_callback(self.run)

        if self.enableDJM is not False:
            self.djm850_midiiin.set_callback(self.djm_callback)

    def set_effect(self, effect):
        self.midiClock.set_effect(effect)

    def djm_callback(self, msg, arg):
        if msg:
            payload, deltatime = msg
            command = payload[0]

            if command == 0xB0:
                self.djmController.process_control(payload)

    def run(self, msg, arg):
        if msg:
            payload, deltatime = msg
            command = payload[0]

            if command == 248 and deltatime != 0 or command == 254:
                self.midiClock.process(msg, deltatime)

            elif command == 0xB0 or command == 0xB1:
                deck = command - 0xB0
                self.denonHc4500Controller.process(payload, deck)
            else:
                logging.info("Received MIDI %s", command)
