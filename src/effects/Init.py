from effects.AbstractEffect import AbstractEffect
from effects.modifiers.between import between
from scenes.Blackout import Blackout
from scenes.Cyan import Cyan
from scenes.RedLed import RedLed as Red
from scenes.Green import Green
from scenes.Blue import Blue
from scenes.PurpleLed import PurpleLed as Purple
from scenes.YellowLed import YellowLed as Yellow


class Init(AbstractEffect):
    def next_scene(self, i):
        red = Red().scene()
        green = Green().scene()
        cyan = Cyan().scene()
        blue = Blue().scene()
        purple = Purple().scene()
        yellow = Yellow().scene()

        if i == 0:
            return green

        if i == 1:
            return cyan

        if i == 2:
            return blue

        if i == 3:
            return purple

        if i == 4:
            return red

        if i == 5:
            return yellow

        return Blackout().scene()

    def multiplier(self):
        return 1