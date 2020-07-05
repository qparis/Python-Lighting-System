from effects.AbstractEffect import AbstractEffect
from effects.modifiers.withColoredFlash import withColoredFlash
from scenes.Red import Red
from scenes.Yellow import Yellow


class YellowFlash(AbstractEffect):
    def next_scene(self, i):
        return withColoredFlash(Yellow().scene())
