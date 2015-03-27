
from random import randint

from .config import pins

__author__ = ("Evan Gillespie",)


class Door(object):
	"""
	object to handle the actions for a single door
	"""
	
	def __init__(self, door_number):

		self.door_number = door_number
		self.pin = pins["doors"][door_number]
		self.state = "closed"


	def is_open(self):
		"""
		check if the door is open by looking at the switch pin

		:return: boolean if the door is open
		"""
		# @TODO: get the real value from gpio
		if randint(0, 10) == 10:
			return True

		return False

	def open(self):
		"""
		actions performed when the door is opened
		"""
		# @TODO: play a sound
		# @TODO: get the actions to perform from the config and do some action
		
		self.state = "open"
		print "DOOR %s is open" % self.door_number


	def close(self):
		"""
		actions performed when the door is closed
		"""
		if self.state == "open":
			self.state = "closed"
			print "Just closed door %s" % self.door_number

