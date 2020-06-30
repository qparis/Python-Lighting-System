from effects.AbstractEffect import AbstractEffect
from scenes.Blue import Blue
from scenes.Green import Green


class BlueGreen(AbstractEffect):
    def next_scene(self, i):
        if i % 2 == 0:
            sceneFactory = Blue()
        else:
            sceneFactory = Green()

        return sceneFactory.scene()