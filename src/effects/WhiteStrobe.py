from effects.AbstractEffect import AbstractEffect
from scenes.WhiteStrobe import WhiteStrobe as WhiteStrobeScene


class WhiteStrobe(AbstractEffect):
    def next_scene(self, i):
        return WhiteStrobeScene().scene()
