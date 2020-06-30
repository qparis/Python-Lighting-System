from unittest import TestCase

from midi.DenonHC4500VirtualLCD import DenonHC4500VirtualLCD


class TestDenonHC4500VirtualLCD(TestCase):
    def test_fetch_char_position(self):
        denonHc = DenonHC4500VirtualLCD()
        self.assertEqual(1, denonHc.fetch_char_position(0x01))
        self.assertEqual(2, denonHc.fetch_char_position(0x02))
        self.assertEqual(3, denonHc.fetch_char_position(0x03))
        self.assertEqual(4, denonHc.fetch_char_position(0x04))
        self.assertEqual(5, denonHc.fetch_char_position(0x05))
        self.assertEqual(6, denonHc.fetch_char_position(0x07))
        self.assertEqual(7, denonHc.fetch_char_position(0x08))
        self.assertEqual(8, denonHc.fetch_char_position(0x09))
        self.assertEqual(9, denonHc.fetch_char_position(0x0A))
        self.assertEqual(10, denonHc.fetch_char_position(0x0B))
        self.assertEqual(11, denonHc.fetch_char_position(0x0C))
        self.assertEqual(12, denonHc.fetch_char_position(0x0D))

        self.assertEqual(1, denonHc.fetch_char_position(0x21))
        self.assertEqual(2, denonHc.fetch_char_position(0x22))
        self.assertEqual(3, denonHc.fetch_char_position(0x23))
        self.assertEqual(4, denonHc.fetch_char_position(0x24))
        self.assertEqual(5, denonHc.fetch_char_position(0x25))
        self.assertEqual(6, denonHc.fetch_char_position(0x27))
        self.assertEqual(7, denonHc.fetch_char_position(0x28))
        self.assertEqual(8, denonHc.fetch_char_position(0x29))
        self.assertEqual(9, denonHc.fetch_char_position(0x2A))
        self.assertEqual(10, denonHc.fetch_char_position(0x2B))
        self.assertEqual(11, denonHc.fetch_char_position(0x2C))
        self.assertEqual(12, denonHc.fetch_char_position(0x2D))


