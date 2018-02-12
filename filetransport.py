#!/usr/bin/env python
import os
import time
import sys

#while  os.path.isfile('beacon.txt'):
filetransport = "sudo cp beacontext.txt /home/pi/psk31lx/TX/beacontext.txt"


while True:
   os.system(filetransport)
   time.sleep(360)
