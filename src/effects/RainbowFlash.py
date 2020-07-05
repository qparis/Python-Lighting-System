from effects.AbstractEffect import AbstractEffect
from effects.modifiers.withColoredFlash import withColoredFlash
from scenes.Blackout import Blackout
from scenes.Cyan import Cyan
from scenes.RedLed import RedLed as Red
from scenes.Green import Green
from scenes.Blue import Blue
from scenes.PurpleLed import PurpleLed as Purple
from scenes.White import White
from scenes.YellowLed import YellowLed as Yellow


class RainbowFlash(AbstractEffect):
    def next_scene(self, i):
        red = Red().scene()
        green = Green().scene()
        cyan = Cyan().scene()
        blue = Blue().scene()
        purple = Purple().scene()
        yellow = Yellow().scene()

        scene = White().scene()
        if i % 6 == 0:
            scene = green

        if i % 6 == 1:
            scene = cyan

        if i % 6 == 2:
            scene = blue

        if i % 6 == 3:
            scene = purple

        if i % 6 == 4:
            scene = red

        if i % 6 == 5:
            scene = yellow

        return withColoredFlash(scene)

    def multiplier(self):
        return 1