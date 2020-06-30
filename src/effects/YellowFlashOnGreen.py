from effects.AbstractEffect import AbstractEffect
from scenes.Green import Green
from scenes.Yellow import Yellow


class YellowFlashOnGreen(AbstractEffect):
    def next_scene(self, i):
        wait = [{
            "type": "wait",
            "duration": 0.05
        }]

        return Yellow().scene() + wait + Green().scene()

