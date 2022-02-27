#!/usr/bin/env python

import os
import shutil
import datetime

homedir = os.getenv("HOME")
path = homedir + "/Desktop"
os.chdir(path)

files = os.listdir()

if len(files) > 1:
  binname = datetime.datetime.now().strftime('desktop_%Y%m%d_%H%M%S')
  binpath = "roomba_dustbin/" + binname
  os.mkdir(binpath)
  for f in files:
    if not(f == 'roomba_dustbin'):
      shutil.move(f, binpath)
