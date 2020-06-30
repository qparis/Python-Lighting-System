from effects.AbstractEffect import AbstractEffect


class AlternateColorLedOnly(AbstractEffect):
    def next_scene(self, i):
        return [{
            1: 255,
            2: 255 * (i % 2),
            3: 255 * (i % 3),
            4: 255 * (i % 5),
            5: 0,
            6: 255,
            7: 255 * (i % 7 % 3),
            8: 255 * (i % 11 % 5),
            9: 255 * (i % 13 % 2),
            10: 0,
            11: 0,
            13: 0,
            14: 0
        }]
