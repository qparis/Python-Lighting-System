from effects.AbstractEffect import AbstractEffect
from scenes.White import White as WhiteScene


class White(AbstractEffect):
    def next_scene(self, i):
        return WhiteScene().scene()
