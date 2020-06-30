from effects.AbstractEffect import AbstractEffect


class AlternateColor(AbstractEffect):
    def next_scene(self, i):
        return [{
            1: 255,
            2: 255 * (i % 2),
            3: 255 * (i % 3 % 2),
            4: 255 * (i % 5 % 2),
            5: 0,
            6: 255,
            7: 255 * (i % 7 % 3 % 2),
            8: 255 * (i % 11 % 5 % 2),
            9: 255 * (i % 13 % 2),
            10: 0,
            11: 255 * (i % 17 % 3 % 2),
            13: 255 * (i % 19 % 5 % 2),
            14: 255 * (i % 23 % 7 % 2)
        }]
