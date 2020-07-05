from effects.AlternateColorLedOnly import AlternateColorLedOnly
from effects.modifiers.withColoredFlash import withColoredFlash


class AlternateColorLedOnlyFlash(AlternateColorLedOnly):
    def next_scene(self, i):
        return withColoredFlash(AlternateColorLedOnly.next_scene(self, i))