from effects.AbstractEffect import AbstractEffect
from effects.modifiers.withColoredFlash import withColoredFlash
from scenes.Blue import Blue


class BlueFlash(AbstractEffect):
    def next_scene(self, i):
        return withColoredFlash(Blue().scene())
