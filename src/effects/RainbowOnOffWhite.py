from effects.AbstractEffect import AbstractEffect
from scenes.Blackout import Blackout
from scenes.Cyan import Cyan
from scenes.RedLed import RedLed as Red
from scenes.Green import Green
from scenes.Blue import Blue
from scenes.PurpleLed import PurpleLed as Purple
from scenes.White import White
from scenes.YellowLed import YellowLed as Yellow


class RainbowOnOffWhite(AbstractEffect):
    def next_scene(self, i):
        red = Red().scene()
        green = Green().scene()
        cyan = Cyan().scene()
        blue = Blue().scene()
        purple = Purple().scene()
        yellow = Yellow().scene()

        if i % 12 == 0:
            return green

        if i % 12 == 2:
            return cyan

        if i % 12 == 4:
            return blue

        if i % 12 == 6:
            return purple

        if i % 12 == 8:
            return red

        if i % 12 == 10:
            return yellow

        if ((i + 1) / 2) % 2 == 0:
            return Blackout().scene()
        else:
            return White().scene()

    def multiplier(self):
        return 1