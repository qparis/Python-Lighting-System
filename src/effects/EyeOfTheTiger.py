from effects.AbstractEffect import AbstractEffect
from scenes.Blackout import Blackout
from scenes.Cyan import Cyan
from scenes.RedLed import RedLed as Red
from scenes.Green import Green
from scenes.Blue import Blue
from scenes.PurpleLed import PurpleLed as Purple
from scenes.White import White
from scenes.WhiteStrobeLow import WhiteStrobeLow
from scenes.YellowLed import YellowLed as Yellow


class EyeOfTheTiger(AbstractEffect):
    def next_scene(self, i):
        red = Red().scene()
        green = Green().scene()
        cyan = Cyan().scene()
        blue = Blue().scene()
        purple = Purple().scene()
        yellow = Yellow().scene()
        blackout = Blackout().scene()
        white = White().scene()
        strobe = WhiteStrobeLow().scene()

        chainStrobe = [white,
                       strobe, strobe,
                       blue, white, red,
                       strobe, strobe, strobe,
                       blue, white, red,
                       strobe, strobe, strobe,
                       blue, white, red,
                       blackout, blackout, blackout,
                       blackout, blackout, blackout,
                       ]

        chain = [white,
                 blackout, blackout,
                 blue, white, red,
                 blackout, blackout, blackout, blackout,
                 blue, white, red,
                 blackout, blackout,
                 blue, white, red,
                 blackout, blackout, blackout,
                 blackout, blackout, blackout
                 ]

        if i < len(chainStrobe):
            return chainStrobe[i % (len(chainStrobe))]
        else:
            return chain[(i - len(chainStrobe)) % (len(chain))]

    def multiplier(self):
        return 1.5
