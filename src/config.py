
folder_path = "assets/audio/"

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
		"mirror_motor2": 22,
		"head_servo": 12,
		"gorilla_servo": 13,
		"left_eye" : 23,
		"right_eye": 24
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