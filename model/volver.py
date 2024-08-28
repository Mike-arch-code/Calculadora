import os
import sys

def volver():
    
    python = sys.executable
    os.execv(python, ['python'] + sys.argv)
    