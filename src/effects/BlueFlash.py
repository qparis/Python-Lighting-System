from effects.AbstractEffect import AbstractEffect
from effects.modifiers.between import between
from scenes.Blackout import Blackout
from scenes.Blue import Blue

class BlueFlash(AbstractEffect):
    def next_scene(self, i):
        wait = [{
            "type": "wait",
            "duration": 0.05
        }]

        return Blue().scene() + wait + between(Blackout().scene(), Blue().scene(), 0.75)

