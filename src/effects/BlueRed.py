from effects.AbstractEffect import AbstractEffect
from scenes.Blue import Blue
from scenes.Red import Red


class BlueRed(AbstractEffect):
    def next_scene(self, i):
        if i % 2 == 0:
            sceneFactory = Blue()
        else:
            sceneFactory = Red()

        return sceneFactory.scene()