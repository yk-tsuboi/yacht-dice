from typing import Any, Dict, Sequence
import random
from porker_hand import Aces, Deuces, Threes, Fours, Fives, Sixes, \
    Choice, FourOfAKind, FullHouse, ShortStraight, LongStraight, Yacht


class ScoreBoard:
    '''ScoreBoard class
    '''

    def __init__(self, hands):
        self.board: Dict[Any, int] = {}
        self.hands: Sequence[Any] = hands

    def set_score(self, hand: Any, score: int):
        if hand not in self.hands:
            raise ValueError
        if hand in self.board:
            raise ValueError
        self.board[hand] = score

    def __str__(self) -> str:
        view_string = '役        点数\n'
        for hand in self.hands:
            if hand in self.board:
                score_to_show = self.board[hand]
            else:
                score_to_show = 0
            view_string += f"{hand.name:_<10}{score_to_show:_>4}\n"
        total_score = sum(self.board.values())
        view_string += f"合計        {total_score:_>4}\n"
        return view_string


def roll_dices():
    return [random.randint(1, 5) for _ in range(5)]


if __name__ == '__main__':
    HANDS = [Aces(), Deuces(), Threes(), Fours(), Fives(), Sixes(),
             Choice(), FourOfAKind(), FullHouse(), ShortStraight(),
             LongStraight(), Yacht()]
    board = ScoreBoard(HANDS)
    while True:
        print(board)
        print('Roll Dices[Enter]', end='>')
        input()
        dices = roll_dices()
        print(f'Dices:{dices}')
        print(f'Possible Hands:')
        for hand in HANDS:
            print(hand, end='')
            print(hand.score(dices))
        possible_hands = [(hand, hand.score(dices))
                          for hand in HANDS if hand.score(dices) > 0]
        for i, hand in enumerate(possible_hands):
            print(f'    [{i}]  {hand[0].name:_<10}{hand[1]:_>4}')
        while True:
            print('Choose one hand[input number]', end='>')
            try:
                idx = int(input())
                hand_to_set = possible_hands[idx]
                break
            except:
                continue
        board.set_score(hand_to_set[0], hand_to_set[1])
