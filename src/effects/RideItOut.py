from effects.AbstractEffect import AbstractEffect
from effects.modifiers.withFlash import withFlash
from scenes.Blackout import Blackout
from scenes.Blue import Blue
from scenes.Cyan import Cyan
from scenes.Green import Green
from scenes.Purple import Purple
from scenes.Red import Red
from scenes.White import White
from scenes.WhiteStrobeLow import WhiteStrobeLow
from scenes.Yellow import Yellow


class RideItOut(AbstractEffect):
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
        flash = withFlash(Blackout().scene())

        chainStrobe = [
            blackout, white,
            blackout, white,
            blackout, blackout,
            blackout, white,
            blackout, white,
            blackout, blackout,
            flash, blackout,
            blackout, blackout,
            flash, white,
            blackout, white,
            blackout, blackout,
            blackout, white,
            blackout, white,
            blackout, blackout,
            flash, blackout,
            blackout, blackout,
            flash,
            white, blackout,
            white, blackout,
            blackout, blackout,
            white, blackout,
            white, blackout,
            blackout,
            flash, white,
            white, white,
            white, white,
            white,
            white, blackout,
            blackout, blackout,
            red, blackout,
            red, blackout,
            blackout, blackout
        ]
        chainStrobe +=chainStrobe

        chain = [blackout]

        if i < len(chainStrobe):
            return chainStrobe[i % (len(chainStrobe))]
        else:
            return chain[(i - len(chainStrobe)) % (len(chain))]

    def multiplier(self):
        return 2
