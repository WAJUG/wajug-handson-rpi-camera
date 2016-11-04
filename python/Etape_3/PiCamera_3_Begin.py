import RPi.GPIO as io
io.setmode(io.BCM)
import sys, tty, termios, time
from picamera import PiCamera
from time import sleep

# The getch method can determine which key has been pressed
# by the user on the keyboard by accessing the system files
# It will then return the pressed key as a variable
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


flag = True

showShortcutsText = "Appuyer sur \"i\" pour afficher les raccourcis"
hideShortcutsText = "Appuyer sur \"i\" pour cacher les raccourcis \n x : exit"

camera = PiCamera()
camera.start_preview()

while True:
    char = getch()
    print(char)

    # The "x" key will break the loop and exit the program
    if(char == "x"):
        camera.stop_preview()
        break

    # The keyboard character variable will be set to blank, ready
    # to save the next key that is pressed
    char = ""
