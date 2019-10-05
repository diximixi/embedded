#!/usr/bin/env python
"""copyToAdafruit.py copies all .py files found in the current directory to the Adafruit Trinket drive /Volumes/CIRCUITPY"""

import os
import shutil
import yesno

dstRoot = "/Volumes/CIRCUITPY"

workpath = os.getcwd()
print ("Files to copy")
for path, _, files in os.walk(workpath):
    for name in files:
        print (" "+os.path.join(os.path.relpath(path), name))

okay = yesno.query_yes_no("Copy?", default="no")
if (okay):
    for path, _, files in os.walk(workpath):
        for name in files:
            relpath = os.path.relpath(path)
            file = os.path.join(path, name)

            dstPath = os.path.join(dstRoot, relpath)
            if (not os.path.exists(dstPath)):
                os.makedirs(dstPath)
            print("Copy " + os.path.relpath(file) + " to " + dstPath)
            shutil.copy(file, dstPath)
