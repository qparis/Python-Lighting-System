from effects.AbstractEffect import AbstractEffect
from scenes.All import All
from scenes.Blackout import Blackout
from scenes.White import White


class OnOffFull(AbstractEffect):
    def next_scene(self, i):
        if i % 2 == 1:
            sceneFactory = Blackout()
        else:
            sceneFactory = All()

        return sceneFactory.scene()