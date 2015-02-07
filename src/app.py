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
	
	def run(self):
		"""
		run the main program loop
		"""
		status = True
		while True:
			status = not status
			gpio.output(23, status)
			sleep(1)