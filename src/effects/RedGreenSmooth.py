from effects.AbstractEffect import AbstractEffect
from effects.modifiers.between import between
from scenes.RedLed import RedLed as Red
from scenes.Green import Green


class RedGreenSmooth(AbstractEffect):
    def next_scene(self, i):
        red = Red().scene()
        green = Green().scene()

        scene = []
        if i % 2 == 0:
            for i in range(0, 10, 1):
                scene += between(green, red, (i+1) / 10)

        else:
            for i in range(0, 10, 1):
                scene += between(red, green, (i + 1) / 10)

        return scene

    def multiplier(self):
        return 1