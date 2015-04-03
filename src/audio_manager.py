
from .config import *
import pygame
from time import sleep

__author__ = ('Evan Gillespie',)

clips = []

def init():
	"""
	load all the audio files into memory to be used later
	"""
	pygame.mixer.pre_init()
	pygame.init()

	for f in audio_filenames:
		path = folder_path+f
		print "adding %s" % path
		clips.append(
			pygame.mixer.Sound(path)
		)


def play(clip_index):
	"""
	play a particular audio clip

	:param clip_index: index of the clip in question in the audio_filenames list
	"""
	clips[clip_index].play()

