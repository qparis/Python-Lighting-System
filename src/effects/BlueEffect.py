from effects.AbstractEffect import AbstractEffect
from scenes.Blue import Blue
from scenes.White import White


class BlueEffect(AbstractEffect):
    def next_scene(self, i):
        wait = [{
            "type": "wait",
            "duration": 0.05
        }]

        return White().scene() + wait + Blue().scene()

