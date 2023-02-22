from distutils.core import setup
import py2exe 
import sys
import cv2 as cv 
import numpy as np   



 
#this allows to run it with a simple double click.
sys.argv.append('py2exe')
 
py2exe_options = {
        "includes": ["sip"],
        "dll_excludes": ["MSVCP90.dll",],
        "compressed": 1,
        "optimize": 2,
        "ascii": 0,
        }
 
setup(
      name = 'PyQt Demo',
      version = '1.0',
      windows = [{ "script":'runst.py'}], 
      zipfile = None,
      options = {'py2exe': py2exe_options}
      )