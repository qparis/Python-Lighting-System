from effects.AbstractEffect import AbstractEffect
from effects.AlternateColorLedOnly import AlternateColorLedOnly
from effects.modifiers.withColoredFlash import withColoredFlash


class AlternateColorLedOnlyDiscreteFlash(AlternateColorLedOnly):
    def next_scene(self, i):
        return withColoredFlash(AlternateColorLedOnly.next_scene(self, i), 0.50)
