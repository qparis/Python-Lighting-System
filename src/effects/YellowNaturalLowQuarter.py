from effects.AbstractEffect import AbstractEffect
from effects.YellowNaturalLow import YellowNaturalLow
from effects.modifiers.between import between


class YellowNaturalLowQuarter(YellowNaturalLow):

    def multiplier(self):
        return 1/4