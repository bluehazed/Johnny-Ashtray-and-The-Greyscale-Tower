import sys
sys.path.insert(0, "..")

from retrogamelib import display
from retrogamelib.constants import *
import menu

def main():
    display.init(2.5, "BubbMan", res=GBRES)
    menu.run_menu()
