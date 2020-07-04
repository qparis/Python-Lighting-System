from effects.AbstractEffect import AbstractEffect
from scenes.Cyan import Cyan
from scenes.Purple import Purple
from scenes.Yellow import Yellow


class CyanYellowPurple(AbstractEffect):
    def next_scene(self, i):
        if i % 3 == 0:
            sceneFactory = Yellow()
        elif i % 3 == 1:
            sceneFactory = Cyan()
        else:
            sceneFactory = Purple()

        return sceneFactory.scene()
