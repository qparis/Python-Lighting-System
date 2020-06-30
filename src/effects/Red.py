from effects.AbstractEffect import AbstractEffect
from scenes.Red import Red as RedScene


class Red(AbstractEffect):
    def next_scene(self, i):
        return RedScene().scene()
