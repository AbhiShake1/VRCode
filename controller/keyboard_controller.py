import time
import controller.controller_module.video_record_module as video_rec

from cvzone.HandTrackingModule import HandDetector
from pynput import keyboard

from config import constants
from view.component.button import Button

keyboard = keyboard.Controller()
video = video_rec.get_instance()
detector = HandDetector(detectionCon=1)
button_list: list = []


def draw_buttons():
    def draw_first_row():
        text_values = ("Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P")
        x_coordinate = 370
        for text in text_values:
            btn = Button(text, (x_coordinate, 300))
            button_list.append(btn)
            btn.draw(img)
            x_coordinate += 60

    def draw_second_row():
        text_values = ("A", "S", "D", "F", "G", "H", "J", "K", "L")
        x_coordinate = 410
        for text in text_values:
            btn = Button(text, (x_coordinate, 360))
            button_list.append(btn)
            btn.draw(img)
            x_coordinate += 60

    def draw_third_row():
        text_values = ("Z", "X", "C", "V", "B", "N", "M")
        x_coordinate = 445
        for text in text_values:
            btn = Button(text, (x_coordinate, 420))
            button_list.append(btn)
            btn.draw(img)
            x_coordinate += 60

    draw_first_row()
    draw_second_row()
    draw_third_row()


last_pressed_time: int = time.time_ns()


def press_keyboard(text: str) -> None:
    global last_pressed_time
    current_time: int = time.time_ns()
    if current_time - last_pressed_time > 1000000000:
        keyboard.press(text)
        last_pressed_time = time.time_ns()


while True:
    img: HandDetector = video.get_img()
    detector.findHands(img, draw=False)
    lm_list, bbox_info = detector.findPosition(img, draw=False)

    draw_buttons()

    if lm_list:
        for button in button_list:
            x, y = button.get_position()
            w, h = button.get_size()

            # x, y coordinates of tip of index finger
            if (x < lm_list[8][0] < x + w) and (y < lm_list[8][1] < y + h):
                btn_size = button.get_size()
                Button(
                    button.get_text(),
                    button.get_position(),
                    btn_size
                ).draw(
                    img,
                    constants.accent_color_dark_hex
                )
                # distance between index finger and thumb
                distance, _, _ = detector.findDistance(8, 4, img, draw=False)
                if distance <= 145:
                    press_keyboard(button.get_text())
                    Button(
                        button.get_text(),
                        button.get_position(),
                        (btn_size[0] + (btn_size[1] // 7), btn_size[1] + (btn_size[0] // 7))
                    ).draw(
                        img,
                        constants.accent_color_secondary_hex
                    )

    video.show()
    if video.close():
        break
