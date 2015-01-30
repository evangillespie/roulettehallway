import pyglet
from time import sleep
from .audio_manager import AudioManager

__author__ = ("Evan Gillespie",)

class App(object):
	"""
	"""

	def __init__(self):
		self.am = AudioManager()

	def run(self):
		"""
		run the main program loop
		"""

		for i in range(self.am.get_num_clips()):
			self.am.play(i)
			sleep(0.5)

		sleep(10)