import RPi.GPIO as gpio
from time import sleep

from .audio_manager import AudioManager

__author__ = ("Evan Gillespie",)

class App(object):
	"""
	"""

	def __init__(self):
		self.am = AudioManager()

		gpio.setmode(gpio.BCM)

		gpio.setup(23, gpio.OUT)
		gpio.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	
	def run(self):
		"""
		run the main program loop
		"""
		
		while True:
			gpio.output(23, gpio.input(4))
			sleep(0.1)