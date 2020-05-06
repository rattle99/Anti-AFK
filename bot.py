from pynput.mouse import Button, Controller
import time

mouse = Controller()

# Read pointer position
print('The current pointer position is {0}'.format(mouse.position))

i = 0

while i in range(300):
    # Move pointer relative to current position
    mouse.move(5,0)
    time.sleep(1)
    mouse.move(0,5)
    time.sleep(1)
    mouse.move(-5,0)
    time.sleep(1)
    mouse.move(0,-5)
    time.sleep(1)