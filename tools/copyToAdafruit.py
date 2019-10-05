#!/usr/bin/env python
"""copyToAdafruit.py copies all .py files found in the current directory to the Adafruit Trinket drive /Volumes/CIRCUITPY"""

import os
import shutil
import yesno

workpath = os.getcwd()
print ("Files to copy")
for path, _, files in os.walk(path):
    for name in files:
        print os.path.join(workpath, name)

okay = yesno.query_yes_no("Copy?", default="no")
if (okay):
    shutil.copytree(path, "/Volumes/CIRCUITPY")
