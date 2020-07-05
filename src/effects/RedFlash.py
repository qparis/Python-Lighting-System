from effects.AbstractEffect import AbstractEffect
from effects.modifiers.withColoredFlash import withColoredFlash
from scenes.Red import Red


class RedFlash(AbstractEffect):
    def next_scene(self, i):
        return withColoredFlash(Red().scene())
