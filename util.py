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

def select_err(test_data, filename, message, keys):
    lns = len(filename)
    s = math.floor(lns*random.random())
    test_data.err_filename = filename[s]
    test_data.err_message = message[s]
    test_data.err_correct = keys[s]
    print("error set-> filename:"+test_data.err_filename+" err_message:"+test_data.err_message+" err_correct:"+test_data.err_correct)


#====usrdefinition function of generation test condition====
def usr_make_condition(test_data, params, status):
    loc_diff_x = 30*int(status.num_test/3) #each 3rd time of test,diff increase 30.
    if test_data.err_correct == "1":
        test_data.err_msg_loc_x -= loc_diff_x
    elif test_data.err_correct == "3":
        test_data.err_msg_loc_y += loc_diff_x
