from bowling_error import BowlingError
from frame import Frame


class BowlingGame:
    def __init__(self):
        self._frames = []
        self._bonus_throw = 0

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

        for index, frame in enumerate(self._frames):
            if frame.is_spare():
                if index == len(self._frames) - 1:
                    frame.set_bonus(self._bonus_throw)
                else:
                    frame.set_bonus(self._frames[index + 1].get_first_throw())
            if frame.is_strike():
                if self._frames[index + 1].is_strike():
                    frame.set_bonus(
                        self._frames[index + 1].get_first_throw()
                        + self._frames[index + 1].get_second_throw()
                        + self._frames[index + 2].get_first_throw()
                    )
                else:
                    frame.set_bonus(
                        self._frames[index + 1].get_first_throw()
                        + self._frames[index + 1].get_second_throw()
                    )
            score += frame.score()
        return score

    def set_first_bonus_throw(self, bonus_throw: int) -> None:
        self._bonus_throw = bonus_throw

    def set_second_bonus_throw(self, bonus_throw: int) -> None:
        pass
