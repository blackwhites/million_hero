import os
import msvcrt
from PIL import Image
import webbrowser

from baidu_ocr import get_question

step = 20
num = 1
in_file = '{}.png'.format(num)
question_file = '{}_{}.png'.format(num, num)

def capture_screen(directory="."):
    os.system("adb shell screencap -p /sdcard/{0}".format(in_file))
    os.system("adb pull /sdcard/{0} {1}".format(in_file, os.path.join(directory, in_file)))

def get_y_end():
    im = Image.open(in_file)
    im_pixel=im.load()
    w, h = im.size
    y = 100
    for i in range(y, h):
        pix = im_pixel[w / 2, i]
        if pix[0] > 225 and pix[1] > 230 and pix[2] > 235 and pix[0] < 235 and pix[1] < 240 and pix[2] < 245:
            return i

def get_y_start():
    im = Image.open(in_file)
    im_pixel=im.load()
    w, h = im.size
    y = 50
    count = 0
    for i in range(y, h, step):
        pix = im_pixel[w / 2, i]
        # print(pix)
        if pix[0] > 250 and pix[1] > 250 and pix[2] > 250:
            count += 1
            if count == 2:
                # print(pix)
                return i - step

def get_question_img():
    image = Image.open(in_file)
    w = image.size[0]
    start_x = 5
    start_y = 150 #get_y_start()
    end_y = 500
    # end_y = get_y_end()
    region = image.crop((start_x, start_y, w - start_x, end_y))
    region.save(question_file)

if __name__ == '__main__':
    while True:
        print('输入任意字符开始检索：')
        msvcrt.getch()
        capture_screen()
        get_question_img()
        question = get_question(question_file)
        webbrowser.open("https://www.baidu.com/s?wd=" + question)
        num += 1
        in_file = '{}.png'.format(num)
        question_file = '{}_{}.png'.format(num, num)

