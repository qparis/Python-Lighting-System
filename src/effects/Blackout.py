from effects.AbstractEffect import AbstractEffect
from scenes.Blackout import Blackout as BlackoutScene

class Blackout(AbstractEffect):
    def next_scene(self, i):
        return BlackoutScene().scene()