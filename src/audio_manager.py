
from .config import *
import pygame
from time import sleep

__author__ = ('Evan Gillespie',)


class AudioManager(object):
	"""
	class for simply playing the audio files when triggered
	"""

	def __init__(self):
		"""
		load all the audio files into memory to be used later
		"""
		pygame.mixer.pre_init()
		pygame.init()

		self.clips = []
		for f in audio_filenames:
			self.clips.append(
				pygame.mixer.Sound(folder_path+f)
			)


	def play(self, clip_index):
		"""
		play a particular audio clip

		:param clip_index: index of the clip in question in the audio_filenames list
		"""
		self.clips[clip_index].play()

	def get_num_clips(self):
		return len(self.clips)
