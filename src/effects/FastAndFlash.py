from effects.AbstractEffect import AbstractEffect
from scenes.Blue import Blue
from scenes.Green import Green
from scenes.Yellow import Yellow


class FastAndFlash(AbstractEffect):
    def next_scene(self, i):
        # 4 temps :
        # 1 Bleu
        # 2 Bleu + Flash
        # 3 Vert
        # 4 Vert + flash

        def withFlash(effect):
            wait = [{
                "type": "wait",
                "duration": 0.05
            }]

            return Yellow().scene() + wait + effect

        if i % 4 == 0:
            return Blue().scene()
        if i % 4 == 1:
            return withFlash(Blue().scene())
        if i % 4 == 2:
            return Green().scene()
        if i % 4 == 3:
            return withFlash(Green().scene())


