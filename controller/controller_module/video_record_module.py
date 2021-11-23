from typing import Optional

import cv2


class _VideoCapture:
    _img: object

    def __init__(self, frame_name="Image"):
        self._frame_name = frame_name
        self._cap = cv2.VideoCapture(0)  # capture from 1st lens (id0) of device
        # 1280x720
        self._cap.set(3, 1280)
        self._cap.set(4, 720)

    def get_img(self):
        self._img = self._cap.read()[1]
        return self._img

    def show(self):
        cv2.imshow(self._frame_name, self._img)
        cv2.waitKey(1)

    def close(self) -> Optional[bool]:
        if cv2.getWindowProperty(self._frame_name, cv2.WND_PROP_VISIBLE) < 1:
            cv2.destroyWindow(self._frame_name)
            return True


_instance: Optional[_VideoCapture] = None


def get_instance(frame_name="Image"):
    global _instance
    if not _instance:
        _instance = _VideoCapture(frame_name)
    return _instance
