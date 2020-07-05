from effects.AbstractEffect import AbstractEffect
from scenes.Red import Red
from scenes.Yellow import Yellow


class YellowRedFlash(AbstractEffect):
    def next_scene(self, i):
        wait = [{
            "type": "wait",
            "duration": 0.05
        }]

        return Yellow().scene() + wait + Red().scene()

