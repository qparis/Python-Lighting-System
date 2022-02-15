import abc
import time


class AbstractEffect(metaclass=abc.ABCMeta):
    def __init__(self, dmxUsb):
        self.dmxUsb = dmxUsb
        self.i = 0

    @abc.abstractmethod
    def next_scene(self, i):
        pass

    def multiplier(self):
        return None

    def wait(self):
        self.dmxUsb.wait_dmx()

    def apply(self):
        for light_application in self.next_scene(self.i):
            if "type" in light_application:
                if light_application["type"] is "wait":
                    time.sleep(light_application["duration"])
            else:
                channelVals = bytearray([0] * 513)
                for channel in light_application:
                    channelVals[channel] = int(min(255, max(0, light_application[channel])))
                self.dmxUsb.send_dmx(channelVals)

        self.i += 1
