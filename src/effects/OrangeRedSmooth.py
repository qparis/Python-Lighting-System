from effects.AbstractEffect import AbstractEffect
from effects.modifiers.between import between
from scenes.Orange import Orange
from scenes.Red import Red


class OrangeRedSmooth(AbstractEffect):
    def next_scene(self, i):
        orange = Orange().scene()
        red = Red().scene()

        scene = []
        if i % 2 == 0:
            for i in range(0, 10, 1):
                scene += between(red, orange, (i+1) / 10)

        else:
            for i in range(0, 10, 1):
                scene += between(orange, red, (i + 1) / 10)

        return scene

    def multiplier(self):
        return 0.5