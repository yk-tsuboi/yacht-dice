import unittest

from yacht.porker_hand import Aces, Deuces, Threes, Fours, Fives, Sixes, \
    Choice, FourOfAKind, FullHouse, ShortStraight, LongStraight, Yacht


class TestPorkerHand(unittest.TestCase):
    def test_aces(self):
        hand = Aces()
        self.assertEqual(hand.score([1, 2, 3, 4, 5]), 1)
        self.assertEqual(hand.score([1, 1, 3, 4, 5]), 2)
        self.assertEqual(hand.score([1, 1, 1, 4, 5]), 3)
        self.assertEqual(hand.score([1, 1, 1, 1, 5]), 4)
        self.assertEqual(hand.score([1, 1, 1, 1, 1]), 5)

    def test_deuces(self):
        hand = Deuces()
        self.assertEqual(hand.score([2, 1, 3, 4, 5]), 2)
        self.assertEqual(hand.score([2, 2, 3, 4, 5]), 4)
        self.assertEqual(hand.score([2, 2, 2, 4, 5]), 6)
        self.assertEqual(hand.score([2, 2, 2, 2, 5]), 8)
        self.assertEqual(hand.score([2, 2, 2, 2, 2]), 10)

    def test_threes(self):
        hand = Threes()
        self.assertEqual(hand.score([3, 1, 2, 4, 5]), 3)
        self.assertEqual(hand.score([3, 3, 1, 4, 5]), 6)
        self.assertEqual(hand.score([3, 3, 3, 4, 5]), 9)
        self.assertEqual(hand.score([3, 3, 3, 3, 5]), 12)
        self.assertEqual(hand.score([3, 3, 3, 3, 3]), 15)

    def test_fours(self):
        hand = Fours()
        self.assertEqual(hand.score([4, 1, 2, 3, 5]), 4)
        self.assertEqual(hand.score([4, 4, 1, 2, 5]), 8)
        self.assertEqual(hand.score([4, 4, 4, 1, 5]), 12)
        self.assertEqual(hand.score([4, 4, 4, 4, 5]), 16)
        self.assertEqual(hand.score([4, 4, 4, 4, 4]), 20)

    def test_fives(self):
        hand = Fives()
        self.assertEqual(hand.score([5, 1, 2, 3, 4]), 5)
        self.assertEqual(hand.score([5, 5, 1, 2, 3]), 10)
        self.assertEqual(hand.score([5, 5, 5, 1, 2]), 15)
        self.assertEqual(hand.score([5, 5, 5, 5, 1]), 20)
        self.assertEqual(hand.score([5, 5, 5, 5, 5]), 25)

    def test_sixes(self):
        hand = Sixes()
        self.assertEqual(hand.score([6, 1, 2, 3, 4]), 6)
        self.assertEqual(hand.score([6, 6, 1, 2, 3]), 12)
        self.assertEqual(hand.score([6, 6, 6, 1, 2]), 18)
        self.assertEqual(hand.score([6, 6, 6, 6, 1]), 24)
        self.assertEqual(hand.score([6, 6, 6, 6, 6]), 30)

    def test_choice(self):
        hand = Choice()
        self.assertEqual(hand.score([1, 2, 3, 4, 5]), 15)
        self.assertEqual(hand.score([3, 3, 3, 3, 3]), 15)

    def test_four_of_the_kind(self):
        hand = FourOfAKind()
        self.assertEqual(hand.score([1, 1, 1, 1, 5]), 9)
        self.assertEqual(hand.score([1, 1, 1, 2, 5]), 0)
        self.assertEqual(hand.score([1, 1, 2, 2, 5]), 0)
        self.assertEqual(hand.score([1, 1, 1, 1, 1]), 5)

    def test_full_house(self):
        hand = FullHouse()
        self.assertEqual(hand.score([1, 1, 2, 2, 2]), 8)
        self.assertEqual(hand.score([1, 1, 1, 2, 2]), 7)
        self.assertEqual(hand.score([1, 1, 2, 2, 3]), 0)

    def test_s_straight(self):
        hand = ShortStraight()
        self.assertEqual(hand.score([1, 2, 3, 4, 5]), hand.SCORE_OF_HAND)
        self.assertEqual(hand.score([1, 2, 3, 4, 6]), hand.SCORE_OF_HAND)
        self.assertEqual(hand.score([1, 1, 2, 2, 3]), 0)
        self.assertEqual(hand.score([1, 3, 2, 2, 4]), hand.SCORE_OF_HAND)

    def test_l_straight(self):
        hand = LongStraight()
        self.assertEqual(hand.score([1, 2, 3, 4, 5]), hand.SCORE_OF_HAND)
        self.assertEqual(hand.score([1, 2, 3, 4, 6]), 0)
        self.assertEqual(hand.score([1, 1, 2, 2, 3]), 0)
        self.assertEqual(hand.score([1, 3, 2, 2, 4]), 0)
        self.assertEqual(hand.score([2, 3, 4, 5, 6]), hand.SCORE_OF_HAND)

    def test_yacht(self):
        hand = Yacht()
        self.assertEqual(hand.score([1, 1, 1, 1, 2]), 0)
        self.assertEqual(hand.score([1, 1, 1, 1, 1]), 5)
        self.assertEqual(hand.score([6, 6, 6, 6, 6]), 30)


if __name__ == '__main__':
    unittest.main()
