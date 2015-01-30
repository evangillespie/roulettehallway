import pyglet

__author__ = ('Evan Gillespie',)


class AudioManager(object):
	"""
	class for simply playing the audio files when triggered
	"""

	def __init__(self):
		"""
		load all the audio files into memory to be used later
		"""
		folder_path = "assets/audio/"
		filenames = [
			"ahem_x.wav",
			"applause2_x.wav",
			"baby_cry.wav",
			"carpentry.wav",
			"cuckoo_clock2_x.wav",
			"hammer_anvil3.wav",
			"helicopter.wav",
			"ice_cream_truck.wav"
		]


		self.clips = []
		for f in filenames:
			self.clips.append(
				pyglet.resource.media(
					folder_path + f,
					streaming=False
				)
			)


	def play(self, clip_index):
		"""
		play a particular audio clip

		:param clip_index: index number of the clip in question
		"""
		self.clips[clip_index].play()

	def get_num_clips(self):
		return len(self.clips)