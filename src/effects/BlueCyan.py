from effects.AbstractEffect import AbstractEffect
from scenes.Blue import Blue
from scenes.Cyan import Cyan


class BlueCyan(AbstractEffect):
    def next_scene(self, i):
        if i % 2 == 0:
            sceneFactory = Blue()
        else:
            sceneFactory = Cyan()

        return sceneFactory.scene()