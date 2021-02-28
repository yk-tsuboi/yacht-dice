from typing import Any, Dict, Sequence
import random
from porker_hand import Aces, Deuces, Threes, Fours, Fives, Sixes, \
    Choice, FourOfAKind, FullHouse, ShortStraight, LongStraight, Yacht
import os


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

    def total_score(self):
        return sum(self.board.values())

    def __str__(self) -> str:
        view_string = '{:<16}{:>4}\n'.format('HAND', 'SCORE')
        for hand in self.hands:
            if hand in self.board:
                score_to_show = str(self.board[hand])
            else:
                score_to_show = '_'
            view_string += f"{hand.name:<16}{score_to_show:>4}\n"
        view_string += "{:<16}{:>4}\n".format('TOTAL', self.total_score())
        return view_string


def roll_dices():
    return [random.randint(1, 5) for _ in range(5)]


if __name__ == '__main__':
    os.system('cls')
    HANDS = [Aces(), Deuces(), Threes(), Fours(), Fives(), Sixes(),
             Choice(), FourOfAKind(), FullHouse(), ShortStraight(),
             LongStraight(), Yacht()]
    board = ScoreBoard(HANDS)
    while True:
        print(board)
        unfilled_hands = [hand for hand in HANDS if hand not in board.board]
        if len(unfilled_hands) == 0:
            print(f'Your total score is {board.total_score()}')
            exit()
        print('Roll Dices[Enter]', end='>')
        input()
        dices = roll_dices()
        print(f'Dices:{dices}')
        print(f'Possible Hands:')
        possible_hands = [(hand, hand.score(dices))
                          for hand in unfilled_hands]
        for i, hand in enumerate(possible_hands):
            print(f'  [{i}]  {hand[0].name:<16}{hand[1]:>4}')
        while True:
            print('Choose one hand[input number]', end='>')
            try:
                idx = int(input())
                hand_to_set = possible_hands[idx]
                break
            except:
                continue
        board.set_score(hand_to_set[0], hand_to_set[1])
        os.system('cls')
