from effects.AbstractEffect import AbstractEffect
from scenes.Blackout import Blackout
from scenes.White import White


class OnOff(AbstractEffect):
    def next_scene(self, i):
        if i % 2 == 1:
            sceneFactory = Blackout()
        else:
            sceneFactory = White()

        return sceneFactory.scene()