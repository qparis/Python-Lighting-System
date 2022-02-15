from effects.AbstractEffect import AbstractEffect
from effects.modifiers.between import between


class YellowNaturalLow(AbstractEffect):
    def next_scene(self, i):
        scene1 = [{
            1: 0, #  int(255 * division),  # Luminosité
            2: 255,  # Red
            3: 200,
            4: 0,
            5: 0,  # Strobe,
            6: 0, # int(255 * division),  # Luminosité Lampe 2
            7: 255,  # Red
            8: 200,
            9: 0,
            10: 0,  # Strobe,
            13: int(255 * 1/2),
            14: int(255 * 1/6)
        }]

        scene2 = [{
            1: 0,  # int(255 * division),  # Luminosité
            2: 255,  # Red
            3: 200,
            4: 0,
            5: 0,  # Strobe,
            6: 0,  # int(255 * division),  # Luminosité Lampe 2
            7: 255,  # Red
            8: 200,
            9: 0,
            10: 0,  # Strobe,
            13: int(255 * 1/6),
            14: int(255 * 1/2)
        }]

        #if i % 2 == 0:
        #    scene = scene1
        #else:
        #    scene = scene2

        #return scene
        scene = []
        if i % 2 == 0:
            for i in range(0, 10, 1):
                scene += between(scene1, scene2, (i+1) / 10)

        else:
            for i in range(0, 10, 1):
                scene += between(scene2, scene1, (i + 1) / 10)
        return scene

    def multiplier(self):
        return 1