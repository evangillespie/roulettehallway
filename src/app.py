import RPi.GPIO as gpio
from time import sleep

from .config import pins
import audio_manager as am
from .door import Door

__author__ = ("Evan Gillespie",)

class App(object):
	"""
	"""

	def __init__(self):
		am.init()

		gpio.setmode(gpio.BCM)

		for pin in pins['doors']:
			gpio.setup(pin, gpio.IN, pull_up_down=gpio.PUD_UP)
		for name, pin in pins['outputs'].iteritems():
			gpio.setup(pin, gpio.OUT)

		self.doors = []
		for i in range(8):
			self.doors.append(Door(i))
	
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
			for door in self.doors:
				if door.is_open():
					door.open()
				else:
					door.close()

			sleep(0.1)
			

		# TODO: add an exit button
		gpio.cleanup()