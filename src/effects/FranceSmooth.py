from effects.AbstractEffect import AbstractEffect
from effects.modifiers.between import between
from scenes.Blue import Blue
from scenes.RedLed import RedLed as Red
from scenes.White import White


class FranceSmooth(AbstractEffect):
    def _generate(self, color1, color2):
        scene = []
        for i in range(0, 10, 1):
            scene += between(color2, color1, (i + 1) / 10)
        return scene

    def next_scene(self, i):
        red = Red().scene()
        white = White().scene()
        blue = Blue().scene()


        if i % 3 == 0:
            return self._generate(blue, white)

        if i % 3 == 1:
            return self._generate(white, red)

        if i % 3 == 2:
            return self._generate(red, blue)



    def multiplier(self):
        return 1