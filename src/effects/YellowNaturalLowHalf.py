from effects.AbstractEffect import AbstractEffect
from effects.YellowNaturalLow import YellowNaturalLow
from effects.modifiers.between import between


class YellowNaturalLowHalf(YellowNaturalLow):
    def multiplier(self):
        return 1/2