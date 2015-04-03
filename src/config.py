import os

os.path.dirname(os.path.realpath(__file__))
folder_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + "/assets/audio/"

pins = {
	"doors": [
		4,
		5,
		6,
		16,
		17,
		18,
		19,
		20
	],
	# not really used. reference only
	"outputs": {
		"mirror_motor1": 21,
		"mirror_motor2": 22
	}
}

# filenames are 001.wav ... 035.wav
audio_filenames = [ "%s.wav" % str(i).zfill(3) for i in range(1, 36)]

# map of door numbers to their audio file indexes
# list index is the door number
# each index contains another list of audio_filenames indexes. Make sense?
audio_door_map = [
	# door 0
	range(0, 4),
	# door 1
	range(4, 8),
	# door 2
	range(8, 12),
	# door 3
	range(12, 16),
	# door 4
	range(16, 20),
	# door 5
	range(20, 24),
	# door 6
	range(24, 28),
	# door 7
	range(28, 35)
]

switch_door_map = [
	# door 0
	[],
	# door 1
	[],
	# door 2
	[pins['outputs']['mirror_motor1']],
	# door 3
	[],
	# door 4
	[pins['outputs']['mirror_motor2']],
	# door 5
	[],
	# door 6
	[],
	# door 7
	[]
]
