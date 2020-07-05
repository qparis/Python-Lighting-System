from effects.AbstractEffect import AbstractEffect
from scenes.Blackout import Blackout
from scenes.Cyan import Cyan
from scenes.RedLed import RedLed as Red
from scenes.Green import Green
from scenes.Blue import Blue
from scenes.PurpleLed import PurpleLed as Purple
from scenes.White import White
from scenes.YellowLed import YellowLed as Yellow


class RainbowHot(AbstractEffect):
    def next_scene(self, i):
        red = Red().scene()
        green = Green().scene()
        white = White().scene()
        yellow = Yellow().scene()

        if i % 4 == 0:
            return green

        if i % 4 == 1:
            return red

        if i % 4 == 2:
            return yellow

        if i % 4 == 3:
            return white

        return Blackout().scene()

    def multiplier(self):
        return 1