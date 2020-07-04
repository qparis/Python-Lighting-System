import random

from effects.AbstractEffect import AbstractEffect
from effects.modifiers.between import between
from scenes.PurpleLed import PurpleLed as Purple
from scenes.RedLed import RedLed as Red
from scenes.White import White


class PinkMix(AbstractEffect):
    def __init__(self, dmxUsb):
        super().__init__(dmxUsb)
        red = Red().scene()
        purple = Purple().scene()
        white = White().scene()

        self.candidates = self._generate(white, red) + self._generate(red, purple) + self._generate(purple, red)

    def _generate(self, color1, color2):
        scene = []
        for i in range(0, 5, 1):
            scene += between(color2, color1, (i + 1) / 5)
        return scene

    def next_scene(self, i):
        return [self.candidates[random.randint(0, len(self.candidates) - 1)]]

    def multiplier(self):
        return 1
