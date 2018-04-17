#-*- coding: utf-8 -*-

import io
from PIL import Image
from aip import AipOcr
from configparser import ConfigParser

def ocr_img(img, config):

	APP_ID = config.get('baidu_api', 'APP_ID')
	API_KEY = config.get('baidu_api', 'API_KEY')
	SECRET_KEY = config.get('baidu_api', 'SECRET_KEY')

	client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

	global combine_region
	combine_region = config.get("region", "combine_region").replace(' ','').split(',')
	combine_region = list(map(int, combine_region))

	region_im = img.crop((combine_region[0], combine_region[1], combine_region[2], combine_region[3]))
	#region_im.show()

	img_byte_arr = io.BytesIO()
	region_im.save(img_byte_arr, format='PNG')
	image_data = img_byte_arr.getvalue()
	response = client.basicGeneral(image_data)
	words_result = response['words_result']

	texts = ''.join([x['words'] for x in words_result])
	#print(texts)
	return texts[:texts.index('A')-1]


if __name__ == '__main__':
	image = Image.open('./screenshot.png')

	config = ConfigParser()
	config.read('./config.conf', encoding='utf-8')

	question = ocr_img(image, config)
	print(question)