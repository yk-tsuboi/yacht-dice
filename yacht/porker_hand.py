from abc import ABC, abstractmethod

import numpy as np


class PorkerHand(ABC):
    @staticmethod
    def _check(dices):
        if len(dices) != 5:
            raise RuntimeError('length of sequence is not 5')

        if not all([isinstance(i, int) for i in dices]):
            raise TypeError('component of list must be integer')

    @abstractmethod
    def score(self, dices):
        return


class _NumberHand(PorkerHand):
    def _score(self, dices, dice_number):
        self._check(dices)
        dices = np.array(dices)
        match_dice = np.count_nonzero(dices == dice_number)
        return match_dice * dice_number


class _DuplicateHand(PorkerHand):
    def _score(self, dices, lower_limit):
        self._check(dices)
        dices = np.array(dices)

        uniq, counts = np.unique(dices, return_counts=True)
        if max(counts) >= lower_limit:
            return sum(dices)
        else:
            return 0


class _StraightHand(PorkerHand):
    def _score(self, dices, candidate):
        self._check(dices)
        unique = np.unique(dices)
        unique.sort()
        for cand in candidate:
            if all([c in unique for c in cand]):
                return self.SCORE_OF_HAND
        return 0


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


class Choice(PorkerHand):
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


class FullHouse(PorkerHand):
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
    CANDIDATE = ([1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6])

    def __init__(self):
        self.name = 'S. Straight'

    def score(self, dices):
        return self._score(dices, self.CANDIDATE)


class LongStraight(_StraightHand):
    SCORE_OF_HAND = 30
    CANDIDATE = ([1, 2, 3, 4, 5], [2, 3, 4, 5, 6])

    def __init__(self):
        self.name = 'L. Straight'

    def score(self, dices):
        return self._score(dices, self.CANDIDATE)


class Yacht(_DuplicateHand):
    def __init__(self):
        self.name = 'Yacht'

    def score(self, dices):
        return self._score(dices, 5)
