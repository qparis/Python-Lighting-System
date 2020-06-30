from effects.AbstractEffect import AbstractEffect
from scenes.Blackout import Blackout
from scenes.White import White


class Flash(AbstractEffect):
    def next_scene(self, i):
        wait = [{
            "type": "wait",
            "duration": 0.05
        }]

        return White().scene() + wait + Blackout().scene()

