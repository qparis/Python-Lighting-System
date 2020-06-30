from effects.AbstractEffect import AbstractEffect
from scenes.Yellow import Yellow
from scenes.Red import Red


class YellowRed(AbstractEffect):
    def next_scene(self, i):
        if i % 2 == 0:
            sceneFactory = Yellow()
        else:
            sceneFactory = Red()

        return sceneFactory.scene()