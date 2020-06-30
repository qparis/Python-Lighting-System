from effects.AbstractEffect import AbstractEffect


class Roll(AbstractEffect):
    def next_scene(self, i):
        rolls = [[1, 2, 3, 4], [6, 7, 8, 9], [11], [13], [14]]
        current_roll = rolls[i % len(rolls)]
        result = {}

        for i in range(20):
            result[i] = 255 if i in current_roll else 0

        return [result]