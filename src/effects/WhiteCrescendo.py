from effects.AbstractEffect import AbstractEffect


class WhiteCrescendo(AbstractEffect):
    def next_scene(self, i):
        division = (i % 4) / 4
        return [{
            1: int(255 * division),  # Luminosité
            2: 255,  # Red
            3: 255,
            4: 255,
            5: 0,  # Strobe,
            6: int(255 * division),  # Luminosité Lampe 2
            7: 255,  # Red
            8: 255,
            9: 255,
            10: 0,  # Strobe,
            11: int(255 * division),
            12: int(255 * division),
            14: int(255 * division),

        }]
