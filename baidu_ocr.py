from aip import AipOcr
import json

""" 你的 APPID AK SK """
APP_ID = '你的APP_ID'
API_KEY = '你的API_KEY'
SECRET_KEY = '你的SECRET_KEY'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def get_question(path):
    image = get_file_content(path)
    res = client.basicGeneral(image)
    words = res['words_result']
    lines = [item['words'] for item in words]
    question = ''.join(lines)
    if question[1] == '.':
        question = question[2:]
    elif question[2] == '.':
        question = question[3:]
    return question.replace('?', '  ')