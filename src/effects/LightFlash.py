from effects.AbstractEffect import AbstractEffect
from effects.modifiers.between import between
from scenes.Blackout import Blackout
from scenes.White import White


class LightFlash(AbstractEffect):
    def next_scene(self, i):
        wait = [{
            "type": "wait",
            "duration": 0.05
        }]

        return White().scene() + wait + between(Blackout().scene(), White().scene(), 0.75)

