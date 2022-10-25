import tkinter as tk
from PIL import ImageTk
import os

PLACEHOLDER_ICON = 'assets/icons/placeholder.png'
PLAY_ICON = 'assets/icons/play.png'
STOP_ICON = 'assets/icons/stop.png'
RESET_ICON = 'assets/icons/reset.png'
ADD_ICON = ''
DELETE_ICON = ''

def load_icon(image_path=PLACEHOLDER_ICON):
	icon = ImageTk.PhotoImage(file=image_path)
	return icon