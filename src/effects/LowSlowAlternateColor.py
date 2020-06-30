from effects.AbstractEffect import AbstractEffect


class LowSlowAlternateColor(AbstractEffect):
    def next_scene(self, i):
        return [{
            1: 64,
            2: 64 * (i % 2),
            3: 64 * (i % 3 % 2),
            4: 64 * (i % 5 % 2),
            5: 0,
            6: 64,
            7: 64 * (i % 7 % 3 % 2),
            8: 64 * (i % 11 % 5 % 2),
            9: 64 * (i % 13 % 2),
            10: 0,
            11: 64 * (i % 17 % 3 % 2),
            13: 64 * (i % 19 % 5 % 2),
            14: 64 * (i % 23 % 7 % 2)
        }]
