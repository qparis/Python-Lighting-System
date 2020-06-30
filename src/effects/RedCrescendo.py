from effects.AbstractEffect import AbstractEffect


class RedCrescendo(AbstractEffect):
    def next_scene(self, i):
        division = (i % 4) / 4
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
