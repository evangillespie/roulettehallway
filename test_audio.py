import RPi.GPIO as gpio
from time import sleep

from src import audio_manager as am

__author__ = ("Evan Gillespie",)

am.init()
for i in range(10):
	am.play(i)


sleep(10)
