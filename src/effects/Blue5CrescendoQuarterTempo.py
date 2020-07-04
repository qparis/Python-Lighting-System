from effects.AbstractEffect import AbstractEffect


class Blue5CrescendoQuarterTempo(AbstractEffect):
    def next_scene(self, i):
        division = (i % 5) / 5
        return [{
            1: int(255 * division),  # Luminosité
            2: 0,  # Red
            3: 0,
            4: 255,
            5: 0,  # Strobe,
            6: int(255 * division),  # Luminosité Lampe 2
            7: 0,  # Red
            8: 0,
            9: 255,
            10: 0
        }]

    def multiplier(self):
        return 1/4
