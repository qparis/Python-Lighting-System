from effects.AbstractEffect import AbstractEffect
from scenes.Blue import Blue as BlueScene


class Blue(AbstractEffect):
    def next_scene(self, i):
        return BlueScene().scene()
