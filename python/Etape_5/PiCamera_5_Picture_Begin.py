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
pictureNumber = 0
videoNumber = 0

showShortcutsText = "Appuyer sur \"i\" pour afficher les raccourcis"
hideShortcutsText = "Appuyer sur \"i\" pour cacher les raccourcis \n a : rotation gauche | z : rotation droite \n x : exit"

camera = PiCamera()
camera.start_preview()
camera.annotate_text = showShortcutsText

while True:
    char = getch()
    print(char)

    # The "x" key will break the loop and exit the program
    if(char == "x"):
        camera.stop_preview()
        break

    # The "i" key will show/hide shortcuts
    if(char == "i"):
        if flag is True :
            camera.annotate_text = hideShortcutsText
            flag = False
        else:
            camera.annotate_text = showShortcutsText
            flag = True

    # The "a" key will rotate camera -90 degree to the left
    if(char == "a"):
        camera.rotation = camera.rotation - 90

    # The "z" key will rotate camera +90 degree to the right
    if(char == "z"):
        camera.rotation = camera.rotation + 90

    # The keyboard character variable will be set to blank, ready
    # to save the next key that is pressed
    char = ""
