from effects.AbstractEffect import AbstractEffect
from scenes.Blue import Blue
from scenes.Purple import Purple


class BluePurple(AbstractEffect):
    def next_scene(self, i):
        if i % 2 == 0:
            sceneFactory = Blue()
        else:
            sceneFactory = Purple()

        return sceneFactory.scene()