from effects.AbstractEffect import AbstractEffect
from scenes.WhiteStrobeLow import WhiteStrobeLow as WhiteStrobeLowScene


class WhiteStrobeLow(AbstractEffect):
    def next_scene(self, i):
        return WhiteStrobeLowScene().scene()
