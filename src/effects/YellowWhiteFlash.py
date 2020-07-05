from effects.AbstractEffect import AbstractEffect
from effects.modifiers.withFlash import withFlash
from scenes.Yellow import Yellow


class YellowWhiteFlash(AbstractEffect):
    def next_scene(self, i):
        return withFlash(Yellow().scene())

