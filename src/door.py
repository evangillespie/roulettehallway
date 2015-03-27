import RPi.GPIO as gpio
from random import choice, randint

from .config import pins, audio_door_map
import audio_manager as am


__author__ = ("Evan Gillespie",)


class Door(object):
	"""
	object to handle the actions for a single door
	"""
	
	def __init__(self, door_number):

		self.door_number = door_number
		self.pin = pins["doors"][door_number]
		self.state = "closed"

		self.audio_indexes = audio_door_map[door_number]


	def is_open(self):
		"""
		check if the door is open by looking at the switch pin

		:return: boolean if the door is open
		"""
		if not gpio.input(self.pin):
			return True

		return False

	def open(self):
		"""
		actions performed when the door is opened
		"""
		# @TODO: get the actions to perform from the config and do some action
		
		if self.state == "closed":
			self.state = "open"
			self._play_sound()
			self._perform_actions()
			print "DOOR %s is open" % self.door_number


	def close(self):
		"""
		actions performed when the door is closed
		"""
		if self.state == "open":
			self.state = "closed"
			print "Just closed door %s" % self.door_number


	def _play_sound(self):
		"""
		play a random sound associated with this door
		"""
		am.play(choice(self.audio_indexes))


	def _perform_actions(self):
		"""
		perform any actions other than playing sound if they exist for this door
		"""
		pass
