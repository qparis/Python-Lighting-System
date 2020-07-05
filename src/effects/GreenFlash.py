from effects.AbstractEffect import AbstractEffect
from effects.modifiers.withColoredFlash import withColoredFlash
from scenes.Green import Green


class GreenFlash(AbstractEffect):
    def next_scene(self, i):
        return withColoredFlash(Green().scene())
