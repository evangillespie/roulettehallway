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
		# init message
		gpio.output(23, gpio.HIGH)
		sleep(0.5)
		gpio.output(23, gpio.LOW)
		sleep(0.5)
		gpio.output(23, gpio.HIGH)
		sleep(0.5)
		gpio.output(23, gpio.LOW)
		sleep(0.5)

		# infinite program loop
		while True:
			for index, door_pin in enumerate(pins['doors']):
				if not gpio.input(door_pin):
					self.am.play(index)

			sleep(0.1)
			

		# TODO: add an exit buttom
		gpio.cleanup()