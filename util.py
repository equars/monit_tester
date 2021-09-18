import sys
import math
import random
import threading
import tkinter

import class_lib as cl


def dump_data():
    print("dump data")

def beep(freq, dur=100):
    import winsound
    #winsound.Beep(freq, dur) #cannot async
    winsound.PlaySound("./sounds/beep-01a.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)

def select_err(test_data, filename, message, correct):
    lns = len(filename)
    s = math.floor(lns*random.random())
    test_data.err_filename = filename[s]
    test_data.err_message = message[s]
    test_data.err_correct = correct[s]


