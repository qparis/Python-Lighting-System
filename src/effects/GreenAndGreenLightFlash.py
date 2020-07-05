from effects.AbstractEffect import AbstractEffect
from effects.modifiers.withFlash import withFlash
from scenes.Green import Green
from scenes.GreenLight import GreenLight


class GreenAndGreenLightFlash(AbstractEffect):
    def next_scene(self, i):
        return withFlash(Green().scene(), GreenLight().scene())


