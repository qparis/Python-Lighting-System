from effects.AbstractEffect import AbstractEffect
from effects.modifiers.between import between
from scenes.Blue import Blue
from scenes.Cyan import Cyan


class BlueCyanSmooth(AbstractEffect):
    def next_scene(self, i):
        blue = Blue().scene()
        cyan = Cyan().scene()

        scene = []
        if i % 2 == 0:
            for i in range(0, 10, 1):
                scene += between(cyan, blue, (i+1) / 10)

        else:
            for i in range(0, 10, 1):
                scene += between(blue, cyan, (i + 1) / 10)

        return scene

    def multiplier(self):
        return 1