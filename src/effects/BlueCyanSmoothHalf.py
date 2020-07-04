from effects.AbstractEffect import AbstractEffect
from effects.BlueCyanSmooth import BlueCyanSmooth
from effects.modifiers.between import between
from scenes.Blue import Blue
from scenes.Cyan import Cyan


class BlueCyanSmoothHalf(BlueCyanSmooth):
    def multiplier(self):
        return 0.5 * BlueCyanSmooth.multiplier(self)