import sys
import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageDraw, ImageFont

plt.rcParams['font.family'] = 'SimHei'

def cv2ImgAddText(img, text, left, top, textColor=(0, 255, 0), textSize=20):

    if (isinstance(img, np.ndarray)):

        img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

        draw = ImageDraw.Draw(img)

        fontText = ImageFont.truetype(        "simhei.ttf", textSize, encoding="utf-8")

        draw.text((left, top), text, textColor, font=fontText)

        return cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)

def fun(frame):

    if frame is None:
        sys.exit(1)

    image_gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    image_blurred = cv2.GaussianBlur(image_gray, (7, 7), 0)

    image_threshold1 = cv2.adaptiveThreshold(image_blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5,
                                             2)

    img_threshold1_blurred = cv2.GaussianBlur(image_threshold1, (5, 5), 0)

    _, img_threshold2 = cv2.threshold(img_threshold1_blurred, 200, 255, cv2.THRESH_BINARY)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

    img_opening = cv2.bitwise_not(cv2.morphologyEx(cv2.bitwise_not(img_threshold2), cv2.MORPH_OPEN, kernel))

    img_word = cv2ImgAddText(img_opening, "当他下飞机的那一刻，他辉煌的一生结束了", 50, 15, (0, 0, 0), 50)

    img_final = cv2.GaussianBlur(img_word, (3, 3), 0)

    cv2.imshow("zhang xue liang", img_final)


if __name__ == '__main__':

    cap = cv2.VideoCapture('少帅下飞机.mp4')

    while True:

        _, frame = cap.read()

        fun(frame)

        cv2.waitKey(10)

    cv2.destroyAllWindows()


