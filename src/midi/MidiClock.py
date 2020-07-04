import logging


class MidiClock:
    def __init__(self):
        self.multiplier = 1
        self.count = 0
        self.bpm = 0
        self._clock_callback = None
        self._sync_callback = None
        self._beat_callback = None
        self._nobeat_callback = None

    def clock_callback(self, _clock_callback):
        self._clock_callback = _clock_callback

    def sync_callback(self, _sync_callback):
        self._sync_callback = _sync_callback

    def beat_callback(self, _beat_callback):
        self._beat_callback = _beat_callback

    def nobeat_callback(self, _nobeat_callback):
        self._nobeat_callback = _nobeat_callback

    def set_effect(self, effect):
        self.beat_callback(effect.apply)
        self.nobeat_callback(effect.wait)
        if effect.multiplier() is not None:
            self.set_multiplier(effect.multiplier())
        else:
            self.set_multiplier(1)

    def set_multiplier(self, multiplier):
        print("Multiplier is %s " % multiplier)
        self.multiplier = multiplier
        self.sync()

    def sync(self):
        self.count = 0

    def process(self, msg, argument):
        payload, deltatime = msg
        command = payload[0]
        if command == 248 and deltatime != 0:
            bpm = 60 / (24 * deltatime)
            self.bpm = bpm
            if self._clock_callback is not None:
                self._clock_callback(bpm, deltatime)

            self.count += 1

            if self.count == 24 / self.multiplier:
                self.count = 0
                if self._beat_callback is not None:
                    self._beat_callback()
            else:
                if self._nobeat_callback is not None:
                    self._nobeat_callback()

        elif command == 252:
            if self._sync_callback is not None:
                self._sync_callback()
            self.sync()
