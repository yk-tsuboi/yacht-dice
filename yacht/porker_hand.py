import numpy as np


class _PorkerHand:
    @staticmethod
    def _check(dices):
        if len(dices) != 5:
            raise RuntimeError('length of sequence is not 5')

        if not all([isinstance(i, int) for i in dices]):
            raise TypeError('component of list must be integer')

    def score(self, dices):
        return


class _NumberHand(_PorkerHand):
    def _score(self, dices, dice_number):
        self._check(dices)
        dices = np.array(dices)
        match_dice = np.count_nonzero(dices == dice_number)
        return match_dice * dice_number


class _DuplicateHand(_PorkerHand):
    def _score(self, dices, lower_limit):
        self._check(dices)
        dices = np.array(dices)

        uniq, counts = np.unique(dices, return_counts=True)
        if max(counts) >= lower_limit:
            return sum(dices)
        else:
            return 0


class _StraightHand(_PorkerHand):
    def _preprocess(self, dices):
        self._check(dices)
        dices = np.array(dices).sort()
        return dices


class Aces(_NumberHand):
    def __init__(self):
        self.name = 'Ace'

    def score(self, dices):
        return self._score(dices, 1)


class Deuces(_NumberHand):
    def __init__(self):
        self.name = 'Deuces'

    def score(self, dices):
        return self._score(dices, 2)


class Threes(_NumberHand):
    def __init__(self):
        self.name = 'Threes'

    def score(self, dices):
        return self._score(dices, 3)


class Fours(_NumberHand):
    def __init__(self):
        self.name = 'Fours'

    def score(self, dices):
        return self._score(dices, 4)


class Fives(_NumberHand):
    def __init__(self):
        self.name = 'Fives'

    def score(self, dices):
        return self._score(dices, 5)


class Sixes(_NumberHand):
    def __init__(self):
        self.name = 'Sixes'

    def score(self, dices):
        return self._score(dices, 6)


class Choice(_PorkerHand):
    def __init__(self):
        self.name = 'Choice'

    def score(self, dices):
        self._check(dices)
        return sum(dices)


class FourOfAKind(_DuplicateHand):
    def __init__(self):
        self.name = '4 of a kind'

    def score(self, dices):
        return self._score(dices, 4)


class FullHouse(_PorkerHand):
    def __init__(self):
        self.name = 'Full House'

    def score(self, dices):
        self._check(dices)
        dices = np.array(dices)
        uniq, count = np.unique(dices, return_counts=True)

        sorted_count = sorted(count)
        if not (sorted_count[0] == 2 and sorted_count[1] == 3):
            return 0
        else:
            ret = 0
            for u, c in zip(uniq, count):
                ret += u * c
            return ret


class ShortStraight(_StraightHand):
    SCORE_OF_HAND = 15

    def __init__(self):
        self.name = 'S. Straight'

    def score(self, dices):
        dices = self._preprocess(dices)
        if dices[:4] == np.array([1, 2, 3, 4]) or \
                dices[:4] == np.array([2, 3, 4, 5]) or \
                dices[1:] == np.array([3, 4, 5, 6]):
            return ShortStraight.SCORE_OF_HAND
        else:
            return 0


class LongStraight(_StraightHand):
    SCORE_OF_HAND = 20

    def __init__(self):
        self.name = 'L. Straight'

    def score(self, dices):
        dices = self._preprocess(dices)
        if dices == np.array([1, 2, 3, 4, 5]) or \
                dices == np.array([2, 3, 4, 5, 6]):
            return LongStraight.SCORE_OF_HAND
        else:
            return 0


class Yacht(_DuplicateHand):
    def __init__(self):
        self.name = 'Yacht'

    def score(self, dices):
        return self._score(dices, 5)
