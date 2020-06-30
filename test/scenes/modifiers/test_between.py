from unittest import TestCase

from effects.modifiers.between import between


class Test(TestCase):
    def test_between(self):
        self.assertEqual(50, between([{1: 0}], [{1: 100}], 0.5)[0][1])
