from typing import Dict, Sequence
import random


class ScoreBoard:

    def __init__(self, hands):
        self.board: Dict[str, int] = {}
        self.hands: Sequence[str] = hands

    def set_score(self, hand: str, score: int):
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
            view_string += f"{hand:_<10}{score_to_show:_>4}\n"
        total_score = sum(self.board.values())
        view_string += f"合計        {total_score:_>4}\n"
        return view_string


def roll_dices():
    return [random.randint(1, 5) for _ in range(5)]


if __name__ == '__main__':
    HANDS = ['ヨット', 'ビッグストレート', 'スモールストレート', 'フォーナンバーズ', 'フルハウス',
             'チョイス', 'シックス', 'ファイブ', 'フォー', 'スリー', 'デュース', 'エース']
    board = ScoreBoard(HANDS)
    while True:
        print(board)
        print('Roll Dices[Enter]', end='>')
        input()
        dices = roll_dices()
        print(f'Dices:{dices}')
        print(f'Possible Hands:')
        possible_hands = [(hand, random.randint(10, 100))
                          for hand in ('スリー', 'デュース', 'エース')]
        for i, hand in enumerate(possible_hands):
            print(f'    [{i}]  {hand[0]:_<10}{hand[1]:_>4}')
        while True:
            print(f'Choose one hand[input number]', end='>')
            try:
                idx = int(input())
                hand_to_set = possible_hands[idx]
                break
            except:
                continue
        board.set_score(hand_to_set[0], hand_to_set[1])
