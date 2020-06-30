from effects.AbstractEffect import AbstractEffect
from scenes.Blue import Blue
from scenes.White import White


class BlueWhite(AbstractEffect):
    def next_scene(self, i):
        if i % 2 == 0:
            sceneFactory = Blue()
        else:
            sceneFactory = White()

        return sceneFactory.scene()