
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
		clips.append(
			pygame.mixer.Sound(folder_path+f)
		)


def play(clip_index):
	"""
	play a particular audio clip

	:param clip_index: index of the clip in question in the audio_filenames list
	"""
	clips[clip_index].play()


def get_num_clips():
	return len(clips)
