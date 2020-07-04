from effects.AbstractEffect import AbstractEffect
from effects.modifiers.between import between
from scenes.Green import Green
from scenes.GreenLight import GreenLight


class GreenSmooth(AbstractEffect):
    def next_scene(self, i):
        green = Green().scene()
        greenLight = GreenLight().scene()

        scene = []
        if i % 2 == 0:
            for i in range(0, 10, 1):
                scene += between(greenLight, green, (i+1) / 10)

        else:
            for i in range(0, 10, 1):
                scene += between(green, greenLight, (i + 1) / 10)

        return scene

    def multiplier(self):
        return 0.5