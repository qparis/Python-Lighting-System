from effects.AbstractEffect import AbstractEffect


class RedLowHalf(AbstractEffect):
    def next_scene(self, i):
        if i % 2 == 0:
            division = 1
        else:
            division = 1/2

        return [{
            1: int(255 * division),  # Luminosité
            2: 255,  # Red
            3: 0,
            4: 0,
            5: 0,  # Strobe,
            6: int(255 * division),  # Luminosité Lampe 2
            7: 255,  # Red
            8: 0,
            9: 0,
            10: 0,  # Strobe,
            11: int(255 * division)
        }]

    def multiplier(self):
        return 1/2