from effects.AbstractEffect import AbstractEffect
from effects.modifiers.between import between
from scenes.Blackout import Blackout
from scenes.WhiteStrobe import WhiteStrobe


class WhiteStrobeFlash(AbstractEffect):
    def next_scene(self, i):
        wait = [{
            "type": "wait",
            "duration": 0.05
        }]

        return WhiteStrobe().scene() + wait + between(Blackout().scene(), WhiteStrobe().scene(), 0.75)

