from bowling_error import BowlingError
from frame import Frame


class BowlingGame:
    def __init__(self):
        self._frames = []

    def add_frame(self, frame: Frame) -> None:
        if len(self._frames) > 9:
            raise BowlingError
        self._frames.append(frame)

    def get_frame_at(self, i: int) -> Frame:
        if i >= len(self._frames):
            raise BowlingError
        return self._frames[i]

    def calculate_score(self) -> int:
        score = 0
        is_spare = False
        is_strike = False

        for frame in self._frames:
            if is_strike:
                score += frame.get_first_throw() + frame.get_second_throw()
                is_strike = False
            if is_spare:
                score += score + frame.get_first_throw()
                is_spare = False
            if frame.is_spare():
                is_spare = True
            if frame.is_strike():
                is_strike = True
            score += frame.score()

        return score

    def set_first_bonus_throw(self, bonus_throw: int) -> None:
        pass

    def set_second_bonus_throw(self, bonus_throw: int) -> None:
        pass
