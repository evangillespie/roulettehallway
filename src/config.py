
folder_path = "assets/audio/"

# filenames are 001.wav ... 035.wav
audio_filenames = [ "%s.wav" % str(i).zfill(3) for i in range(1, 36)]

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
	"outputs": {
		"mirror_motor1": 21,
		"mirror_motor2": 22,
		"head_servo": 12,
		"gorilla_servo": 13,
		"left_eye" : 23,
		"right_eye": 24
	}
}