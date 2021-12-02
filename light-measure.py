import picamera
import time

x=2560
y=1440

name = input()

cam = picamera.PiCamera()
cam.resolution = (x,y)
cam.start_preview()
time.sleep(5)
cam.capture(name)
print("Done!")