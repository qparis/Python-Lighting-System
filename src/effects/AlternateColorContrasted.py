import random

from effects.AbstractEffect import AbstractEffect


class AlternateColorContrasted(AbstractEffect):
    def next_scene(self, i):
        def generateLowValue():
            return random.randint(0, 32)

        def generateHighValue():
            return random.randint(200, 255)

        def generateLedMap():
            possibilities = [
                [1, 0, 0], [0, 1, 0], [0, 0, 1],
                [1, 1, 0], [0, 1, 1], [1, 0, 1]
            ]
            return possibilities[random.randint(0, len(possibilities) - 1)]

        def generateLedPlan():
            def mapper(v):
                if v == 1:
                    return generateHighValue()
                else:
                    return generateLowValue()

            return [mapper(v) for v in generateLedMap()]

        led1 = generateLedPlan()
        led2 = generateLedPlan()

        return [{
            1: 255,
            2: led1[0],
            3: led1[1],
            4: led1[2],
            5: 0,
            6: 255,
            7: led2[0],
            8: led2[1],
            9: led2[2],
            10: 0,
            11: 0,
            13: 0,
            14: 0
        }]
