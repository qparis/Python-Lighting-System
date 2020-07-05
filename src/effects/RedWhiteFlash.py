from effects.AbstractEffect import AbstractEffect
from effects.modifiers.between import between
from scenes.Blackout import Blackout
from scenes.Red import Red
from scenes.White import White

class RedWhiteFlash(AbstractEffect):
    def next_scene(self, i):
        wait = [{
            "type": "wait",
            "duration": 0.05
        }]

        return White().scene() + wait + between(Blackout().scene(), Red().scene(), 0.75)

