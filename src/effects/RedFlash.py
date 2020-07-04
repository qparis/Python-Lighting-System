from effects.AbstractEffect import AbstractEffect
from effects.modifiers.between import between
from scenes.Blackout import Blackout
from scenes.Red import Red

class RedFlash(AbstractEffect):
    def next_scene(self, i):
        wait = [{
            "type": "wait",
            "duration": 0.05
        }]

        return Red().scene() + wait + between(Blackout().scene(), Red().scene(), 0.75)

