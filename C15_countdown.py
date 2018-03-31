# countdown.py - A simple countdown script.

import time
import subprocess

timeLeft = 3

while timeLeft > 0:
    print(timeLeft, end='')
    time.sleep(1)
    timeLeft -= 1

# At the end of the countdown, play a sound file.
subprocess.Popen(['start', '.\\files\\alarm.wav'], shell=True)

