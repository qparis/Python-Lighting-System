from effects.AbstractEffect import AbstractEffect
from effects.modifiers.between import between
from scenes.Cyan import Cyan
from scenes.RedLed import RedLed as Red
from scenes.Green import Green
from scenes.Blue import Blue
from scenes.PurpleLed import PurpleLed as Purple
from scenes.YellowLed import YellowLed as Yellow


class RainbowSmooth(AbstractEffect):
    def _generate(self, color1, color2):
        scene = []
        for i in range(0, 10, 1):
            scene += between(color2, color1, (i + 1) / 10)
        return scene

    def next_scene(self, i):
        red = Red().scene()
        green = Green().scene()
        cyan = Cyan().scene()
        blue = Blue().scene()
        purple = Purple().scene()
        yellow = Yellow().scene()

        if i % 6 == 0:
            return self._generate(green, cyan)

        if i % 6 == 1:
            return self._generate(cyan, blue)

        if i % 6 == 2:
            return self._generate(blue, purple)

        if i % 6 == 3:
            return self._generate(purple, red)

        if i % 6 == 4:
            return self._generate(red, yellow)

        if i % 6 == 5:
            return self._generate(yellow, green)

    def multiplier(self):
        return 1