from effects.AbstractEffect import AbstractEffect


class OnOffSmooth(AbstractEffect):
    def next_scene(self, i):
        if i % 2 == 1:
            return [{
                1: 250 - i,
                2: 255,
                3: 255,
                4: 255,
                5: 0
            } for i in range(0, 255, 50)]
        else:
            return [{
                1: i,
                2: 255,
                3: 255,
                4: 255,
                5: 0
            } for i in range(0, 255, 50)]

    def multiplier(self):
        return 4