import random

from effects.AbstractEffect import AbstractEffect


class RandomColor(AbstractEffect):
    def __init__(self, dmxUsb, saturate = True):
        AbstractEffect.__init__(self, dmxUsb)
        self.saturate = saturate

    def next_scene(self, i):
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)

        red2 = random.randint(0, 255)
        green2 = random.randint(0, 255)
        blue2 = random.randint(0, 255)

        lamp1 = random.randint(0, 255)
        lamp2 = random.randint(0, 255)
        lamp3 = random.randint(0, 255)


        if self.saturate is True:
            higher = max([red, green, blue, red2, green2, blue2, lamp1, lamp2, lamp3])
            lower = min([red, green, blue, red2, green2, blue2, lamp1, lamp2, lamp3])
            delta = higher - lower

            red = int(red / delta * 255)
            green = int(green / delta * 255)
            blue = int(blue / delta * 255)

            red2 = int(red2 / delta * 255)
            green2 = int(green2 / delta * 255)
            blue2 = int(blue2 / delta * 255)

            lamp1 = int(lamp1 / delta * 255)
            lamp2 = int(lamp2 / delta * 255)
            lamp3 = int(lamp3 / delta * 255)

        return [{
            1: 255,
            2: red,
            3: green,
            4: blue,
            5: 0,
            6: 255,
            7: red2,
            8: green2,
            9: blue2,
            10: 0,
            11: lamp1,
            13: lamp2,
            14: lamp3
        }]
