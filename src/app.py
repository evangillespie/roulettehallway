import RPi.GPIO as gpio
from time import sleep

from .config import pins
from .audio_manager import AudioManager

__author__ = ("Evan Gillespie",)

class App(object):
	"""
	"""

	def __init__(self):
		self.am = AudioManager()

		gpio.setmode(gpio.BCM)

		for pin in pins['doors']:
			gpio.setup(pin, gpio.IN, pull_up_down=gpio.PUD_UP)

		for name, pin in pins['outputs'].iteritems():
			gpio.setup(pin, gpio.OUT)
	
	def run(self):
		"""
		run the main program loop
		"""
		# infinite program loop
		while True:
			pass
			sleep (1)