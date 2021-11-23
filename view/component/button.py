import cv2
from config import constants
from cvzone.HandTrackingModule import HandDetector


class Button:
    def __init__(self, text: str, pos: tuple[int, int], size: tuple[int, int] = (50, 50)):
        self._pos = pos
        self._text = text
        self._size = size

    def draw(self, img: HandDetector, color: tuple[int, int, int] = constants.accent_color_hex) -> None:
        x, y = self._pos
        w, h = self._size
        cv2.rectangle(
            img,
            self._pos,  # starting point
            (x+w, y+h),  # size
            color,  # color hex
            cv2.FILLED  # thickness
        )
        cv2.putText(
            img,
            self._text,
            ((x + 15), (y + 35)),  # origin
            cv2.FONT_HERSHEY_SIMPLEX,  # font
            1,  # font scale
            (255, 255, 255),  # color hex
            3  # thickness
        )

    def get_position(self) -> tuple[int, int]:
        return self._pos

    def get_size(self) -> tuple[int, int]:
        return self._size

    def get_text(self) -> str:
        return self._text
