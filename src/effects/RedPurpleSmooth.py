from effects.AbstractEffect import AbstractEffect
from effects.modifiers.between import between
from scenes.RedLed import RedLed as Red
from scenes.PurpleLed import PurpleLed as Purple


class RedPurpleSmooth(AbstractEffect):
    def next_scene(self, i):
        red = Red().scene()
        purple = Purple().scene()

        scene = []
        if i % 2 == 0:
            for i in range(0, 10, 1):
                scene += between(purple, red, (i+1) / 10)

        else:
            for i in range(0, 10, 1):
                scene += between(red, purple, (i + 1) / 10)

        return scene

    def multiplier(self):
        return 1