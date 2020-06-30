import logging
import threading

from rtmidi.midiutil import open_midiinput

log = logging.getLogger('midiin_poll')
logging.basicConfig(level=logging.DEBUG)


class MidiController:
    def __init__(self, midiClock, denonHc4500Controller):
        self._running = True
        self.__initialize()
        self.midiClock = midiClock
        self.denonHc4500Controller = denonHc4500Controller

    def __initialize(self):
        self.midiin, port_name = open_midiinput(1)
        print("Midi device: %s" % port_name)
        self.midiin.ignore_types(False, False, False)

    def stop(self):
        self._running = False

    def start(self):
        self.midiin.set_callback(self.run)

    def set_multiplier(self, multiplier):
        self.midiClock.set_multiplier(multiplier)

    def set_effect(self, effect):
        self.midiClock.set_effect(effect)

    def run(self, msg, argument):
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
