import os
import sys
import csv
import datetime
import random
import time
import configparser

import util

class Setting_params:
    #==variables==
    #test_window size
    test_window_size_x = 0
    test_window_size_y = 0

    #monitor image params
    mnt_filename = ""
    mnt_size_x = 0
    mnt_size_y = 0
    mnt_disp_x = 0
    mnt_disp_y = 0
    mnt_disp_size_x = 0
    mnt_disp_size_y = 0
    mnt_loc_x = 0
    mnt_loc_y = 0

    #error image params(minimum)
    err_filename = []
    err_msg=[]
    err_keys=[]

    err_msg_size_x=0
    err_msg_size_y=0
    err_msg_loc_x=0
    err_msg_loc_y=0
    err_msg_font_size=0
    err_msg_font_bold=1

    err_size_x = 0
    err_size_y = 0
    err_loc_x = 0
    err_loc_y = 0

    #range of test
    alert_duration_time = 5
    alert_duration_random = 2 #1 as gauss distribution, 2 as uniform distribution
    alert_duration_random_coeff1 = 1
    alert_duration_random_coeff2 = 1

    err_size_max_x = 0
    err_size_max_y = 0
    err_size_step_x = 5
    err_size_step_y = 5
    err_size_random = 0 #0 as no random, 1 as step random, 2 as totally random(ignore step)
    err_size_random_coeff1 = 1
    err_size_random_coeff2 = 2

    #examinee data
    name = "Anonymous"
    age = 20
    sex = "f/m"
    sitting_loc_x = 0
    sitting_loc_y = 0

    #others
    output_filename="imgs/out.csv"

    #==methods==
    #read param
    def read(self, conf_filename):
        inifile=configparser.ConfigParser()
        inifile.read(conf_filename, "UTF-8")
        self.test_window_size_x = int(inifile.get("settings", "test_window_size_x"))
        self.test_window_size_y = int(inifile.get("settings", "test_window_size_y"))
        self.mnt_filename = inifile.get("settings", "mnt_filename")
        self.mnt_size_x = int(inifile.get("settings", "mnt_size_x"))
        self.mnt_size_y = int(inifile.get("settings", "mnt_size_y"))
        self.mnt_disp_size_x = int(inifile.get("settings", "mnt_disp_size_x"))
        self.mnt_disp_size_y = int(inifile.get("settings", "mnt_disp_size_y"))
        self.mnt_loc_x = int(inifile.get("settings", "mnt_loc_x"))
        self.mnt_loc_y = int(inifile.get("settings", "mnt_loc_y"))
        self.mnt_loc_y = int(inifile.get("settings", "mnt_loc_y"))
        tmp_err_filename = inifile.get("settings", "err_filename")
        self.err_filename = tmp_err_filename.split(",")
        tmp_err_msg = inifile.get("settings", "err_msg")
        self.err_msg = tmp_err_msg.split(",")
        tmp_err_keys = inifile.get("settings", "err_keys")
        self.err_keys = tmp_err_keys.split(",")


        self.alert_duration_time = float(inifile.get("settings", "alert_duration_time"))
        self.alert_duration_random = inifile.get("settings", "alert_duration_random")
        self.alert_duration_random_coeff1 = float(inifile.get("settings", "alert_duration_random_coeff1"))
        self.alert_duration_random_coeff2 = float(inifile.get("settings", "alert_duration_random_coeff2"))

        self.err_msg_size_x = int(inifile.get("settings", "err_msg_size_x"))
        self.err_msg_size_y = int(inifile.get("settings", "err_msg_size_y"))
        self.err_msg_loc_x = int(inifile.get("settings", "err_msg_loc_x"))
        self.err_msg_loc_y = int(inifile.get("settings", "err_msg_loc_y"))
        self.err_msg_font_size = str(inifile.get("settings", "err_msg_font_size"))
        self.err_msg_font_bold = int(inifile.get("settings", "err_msg_font_bold"))

        self.err_size_x = int(inifile.get("settings", "err_size_x"))
        self.err_size_y = int(inifile.get("settings", "err_size_y"))
        self.err_loc_x = int(inifile.get("settings", "err_loc_x"))
        self.err_loc_y = int(inifile.get("settings", "err_loc_y"))
        self.err_size_max_x = int(inifile.get("settings", "err_size_max_x"))
        self.err_size_max_y = int(inifile.get("settings", "err_size_max_y"))
        self.err_size_step_x = int(inifile.get("settings", "err_size_step_x"))
        self.err_size_step_y = int(inifile.get("settings", "err_size_step_y"))
        self.err_size_random = inifile.get("settings", "err_size_random")
        self.err_size_random_coeff1 = float(inifile.get("settings", "err_size_random_coeff1"))
        self.err_size_random_coeff2 = float(inifile.get("settings", "err_size_random_coeff2"))

        self.name = inifile.get("settings", "name")
        self.age = int(inifile.get("settings", "age"))
        self.sex = inifile.get("settings", "sex")
        self.sitting_loc_x = int(inifile.get("settings", "sitting_loc_x"))
        self.sitting_loc_y = int(inifile.get("settings", "sitting_loc_y"))

        self.output_filename = inifile.get("settings", "output_filename")


class Test_data:
    #input params
    name = ""
    age = 0
    sex = ""
    sitting_loc_x = 0
    sitting_loc_y = 0
    err_size_x = 0
    err_size_y = 0
    error_loc_x = 0
    error_loc_y = 0

    err_msg_size_x = 0
    err_msg_size_y = 0
    err_msg_loc_x = 0
    err_msg_loc_y = 0

    err_msg_font = ""
    err_msg_font_bold = 0

    err_filename = ""
    err_message = ""
    err_correct = ""
    err_keys = []

    #result time
    duration = 0 # to show alert
    time = -1
    is_correct = -1 #-1 as error, 0 as correct, 1 as wrong

    output_filename = ""

    #time management
    def __init__(self):
        self.time_start = time.time()
        self.time_stop = 0.0
        self.time_elapsed = 0.0
        self.playtime=False

    def make_condition(self, params, status):
        self.name = params.name
        self.age = params.age
        self.sex = params.sex
        self.sitting_loc_x = params.sitting_loc_x
        self.sitting_loc_y = params.sitting_loc_y
        self.err_size_x = params.err_size_x
        self.err_size_y = params.err_size_y
        self.err_loc_x = params.err_loc_x
        self.err_loc_y = params.err_loc_y

        self.err_keys = params.err_keys

        self.err_msg_size_x = params.err_msg_size_x
        self.err_msg_size_y = params.err_msg_size_y
        self.err_msg_loc_x = params.err_msg_loc_x
        self.err_msg_loc_y = params.err_msg_loc_y

        self.err_msg_font = "courier "+params.err_msg_font_size
        self.err_msg_font_bold = params.err_msg_font_bold
        self.output_filename = params.output_filename

        util.select_err(self, params.err_filename, params.err_msg, params.err_keys)

        self.duration = random.gauss(params.alert_duration_time,params.alert_duration_random_coeff1)

        util.usr_make_condition(self,params,status) #ユーザ定義関数

    def start_timer(self):
        if not self.playtime:
            self.time_start = time.time()-self.time_elapsed
            self.playtime = True

    def stop_timer(self):
        if self.playtime:
            self.time_stop=time.time()-self.time_start
            self.playtime = False
            self.time=self.time_stop

    def reset_timer(self):
        self.time_start = time.time()
        self.time_stop = 0.0
        self.time_elapsed = 0.0
        self.playtime=False

    def judge(self,key):
        if key == self.err_correct:
            self.is_correct = 0
        else :
            self.is_correct = 1

    def appenddata(self):
        outdata = [datetime.datetime.now(), self.is_correct, self.time, self.name, self.age, self.sex, self.err_msg_size_x, self.err_msg_size_y, self.err_size_x, self.err_size_y, self.sitting_loc_x, self.sitting_loc_y]
        with open(self.output_filename, "a+") as outf :
            writer = csv.writer(outf)
            writer.writerow(outdata)


    def dump(self):
        print("name "+str(self.name))
        print("age "+str(self.age))
        print("sex "+str(self.sex))
        print("sitting_loc_x "+str(self.sitting_loc_x))
        print("sitting_loc_y "+str(self.sitting_loc_y))
        print("err_size_x "+str(self.err_size_x))
        print("err_size_y "+str(self.err_size_y))
        print("duration "+str(self.duration))
        print("time "+str(self.time))
        print("err_correct "+str(self.err_correct))
        print("is_correct "+str(self.is_correct))

class Status:
    num_test = 0
    testing = False

    def test_start(self):
        self.testing = True

    def test_end(self):
        self.testing = False
        self.num_test += 1
