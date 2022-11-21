from subprocess import call
import time
import sys

iteration = 0

def take_screenshot(iteration):
    call(["screencapture", f'./screenshots/{iteration}.jpg'])

interval = 10

if len(sys.argv) == 2:
    interval = int(sys.argv[1])

while True:
    time.sleep(interval)
    take_screenshot(iteration)
    iteration = iteration + 1
