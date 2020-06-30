from effects.AbstractEffect import AbstractEffect
from scenes.Blue import Blue
from scenes.Cyan import Cyan
from scenes.Red import Red
from scenes.Yellow import Yellow


class CyanYellow(AbstractEffect):
    def next_scene(self, i):
        if i % 2 == 0:
            sceneFactory = Yellow()
        else:
            sceneFactory = Cyan()

        return sceneFactory.scene()
