#-*- coding: utf-8 -*-

import wda
import webbrowser
import urllib.parse
from PIL import Image
from configparser import ConfigParser

from ocr import ocr_img

def search(question):
	webbrowser.open('https://baidu.com/s?wd='+urllib.parse.quote(question))


if __name__ == '__main__':
	c = wda.Client()

	config = ConfigParser()
	config.read('./config.conf', encoding='utf-8')

	print('回车继续，输入 x 回车结束\n')
	while True:
		c.screenshot('screenshot.png')
		img = Image.open('./screenshot.png')

		question = ocr_img(img, config)
		print(question)
		#print(choices)

		search(question)

		nxt = input()
		if nxt == 'x':
			break


	