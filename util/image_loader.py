import os
from config import IMAGE_PATH
from PIL import ImageTk

def load_image(image_path=IMAGE_PATH['PLACEHOLDER']):
	try:
		image = ImageTk.PhotoImage(file=image_path)
	except:
		if image_path != IMAGE_PATH['PLACEHOLDER']:
			image = ImageTk.PhotoImage(file=IMAGE_PATH['PLACEHOLDER']) 
	return image