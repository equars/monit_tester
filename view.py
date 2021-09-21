import sys
import tkinter
import time

import class_lib as cl
import util

global err, canvas, err_cnv_create_image

def setting_clicked(status, params):
    print("Setting window opening. Operate some on GUI.")
    #local func
    def save_params(params):
        params.name = str(ent_p1.get())
        params.age = int(ent_p2.get())
        params.sex = ent_p3.get()
        params.alert_duration_time = float(ent_p4.get())
        params.alert_duration_random = float(ent_p5.get())
        params.alert_duration_random_coeff1 = float(ent_p6.get())

    #vals
    setting_window_width = 600
    setting_window_height = 500
    box_base_x = 30
    box_base_y = 10
    box_height = 20
    entry_diff = 180
    entry_width = 30

    #element definition
    setting_window = tkinter.Toplevel()
    setting_window.title("設定")
    setting_window.geometry(str(setting_window_width)+"x"+str(setting_window_height))

    lbl_title1 = tkinter.Label(setting_window, text="被験者パラメータ")
    lbl_title1.place(x=box_base_x+entry_diff, y=box_base_y)
    box_base_y+=box_height

    lbl_p1 = tkinter.Label(setting_window, text="name")
    lbl_p1.place(x=box_base_x, y=box_base_y)
    ent_p1 = tkinter.Entry(setting_window, width=entry_width)
    ent_p1.insert(0, params.name)
    ent_p1.place(x=box_base_x+entry_diff, y=box_base_y)
    box_base_y+=box_height

    lbl_p2 = tkinter.Label(setting_window, text="age")
    lbl_p2.place(x=box_base_x, y=box_base_y)
    ent_p2 = tkinter.Entry(setting_window, width=entry_width)
    ent_p2.insert(0, params.age)
    ent_p2.place(x=box_base_x+entry_diff, y=box_base_y)
    box_base_y+=box_height

    lbl_p3 = tkinter.Label(setting_window, text="sex")
    lbl_p3.place(x=box_base_x, y=box_base_y)
    ent_p3 = tkinter.Entry(setting_window, width=entry_width)
    ent_p3.insert(0, params.sex)
    ent_p3.place(x=box_base_x+entry_diff, y=box_base_y)
    box_base_y+=box_height

    lbl_title2 = tkinter.Label(setting_window, text="試験パラメータ")
    lbl_title2.place(x=box_base_x+entry_diff, y=box_base_y)
    box_base_y+=box_height

    lbl_p4 = tkinter.Label(setting_window, text="alert_duration_time")
    lbl_p4.place(x=box_base_x, y=box_base_y)
    ent_p4 = tkinter.Entry(setting_window, width=entry_width)
    ent_p4.insert(0, params.alert_duration_time)
    ent_p4.place(x=box_base_x+entry_diff, y=box_base_y)
    box_base_y+=box_height

    lbl_p5 = tkinter.Label(setting_window, text="alert_duration_random")
    lbl_p5.place(x=box_base_x, y=box_base_y)
    ent_p5 = tkinter.Entry(setting_window, width=entry_width)
    ent_p5.insert(0, params.alert_duration_random)
    ent_p5.place(x=box_base_x+entry_diff, y=box_base_y)
    box_base_y+=box_height

    lbl_p6 = tkinter.Label(setting_window, text="alert_duration_random_coeff1")
    lbl_p6.place(x=box_base_x, y=box_base_y)
    ent_p6 = tkinter.Entry(setting_window, width=entry_width)
    ent_p6.insert(0, params.alert_duration_random_coeff1)
    ent_p6.place(x=box_base_x+entry_diff, y=box_base_y)
    box_base_y+=box_height

    button_save = tkinter.Button(setting_window, text="SAVE", command=lambda:save_params(params))
    button_quit = tkinter.Button(setting_window, text="QUIT", command=lambda:setting_window.destroy())

    #plot
    button_save.pack(fill="x", padx=20, side="right")
    button_quit.pack(fill="x", padx=20, side="left")

    setting_window.mainloop()

def start_clicked(status, params):
    print("Test window opens. ->'s' as start, 'q' as quit.")
    test_data = cl.Test_data() #make test data
    test_data.make_condition(params, status)

    #vals
    disp_real_ratio_x = float(params.mnt_disp_size_x)/float(params.mnt_size_x)
    disp_real_ratio_y = float(params.mnt_disp_size_y)/float(params.mnt_size_y)

    #local func
    def err_show():
        err_cnv.place(x=test_data.err_loc_x, y=test_data.err_loc_y)
        err_msg_cnv.place(x=int(test_data.err_msg_loc_x), y=int(test_data.err_msg_loc_y))
        test_data.start_timer()
        util.beep(440,10000)

    def key_event(event):
        global err, canvas, err_cnv_create_image
        key_name = event.keysym
        if key_name == "s":
            status.test_start()
            print("'s' pressed, after duration time, error alerted.")
            print("Duration time ->"+str(test_data.duration)+"sec")
            test_window.after(int(test_data.duration*1000), err_show)

            #refresh msg and img
            err_msg_cnv.delete("err_msg_txt")
            err_msg_cnv.create_text((test_data.err_msg_size_x/2,params.err_msg_size_y/2),text=test_data.err_message, font=test_data.err_msg_font, fill="white", anchor=tkinter.CENTER, tag = "err_msg_txt")
            err_cnv.delete("err_cnv")
            err = tkinter.PhotoImage(file=test_data.err_filename)
            err_cnv.create_image(0, 0, image=err, anchor=tkinter.NW, tag="err_img")


        elif key_name == "q":

            print("'q' pressed, quit test window.")
            test_window.destroy()

        elif key_name == "n":
            status.test_end()
            print("'n' pressed, clear and make new test_data.->'s' as start, 'q' as quit.")
            err_cnv.place(x=-int(params.err_loc_x), y=-int(params.err_loc_y))
            err_msg_cnv.place(x=-int(params.err_msg_loc_x), y=-int(params.err_msg_loc_y))
            test_data.make_condition(params, status)

        else:
            if status.testing:
                if key_name in test_data.err_keys:
                    status.test_end()
                    test_data.stop_timer()
                    test_data.reset_timer()
                    test_data.judge(key_name)
                    test_data.appenddata()
                    test_data.dump()
                else:
                    print("Examnee select wrong key other than the options.")
            else:
                print("press 's' to start test.")


    #main
    test_window = tkinter.Toplevel()
    test_window.title("試験画面")
    test_window.geometry(str(params.test_window_size_x)+"x"+str(params.test_window_size_y))

    canvas = tkinter.Canvas(test_window, bg="black", width=params.mnt_disp_size_x, height=params.mnt_disp_size_y)
    canvas.place(x=0, y=0)
    monitor = tkinter.PhotoImage(file=params.mnt_filename)
    #monitor = monitor.subsample(disp_real_ratio_x, disp_real_ratio_y)

    err = tkinter.PhotoImage(file=test_data.err_filename)

    canvas.create_image(params.mnt_loc_x, 0, image=monitor, anchor=tkinter.NW)
    canvas.pack()

    err_cnv = tkinter.Canvas(test_window, bg="white", highlightthickness=0, width=test_data.err_size_x, height=test_data.err_size_y)
    err_cnv_create_image = err_cnv.create_image(0, 0, image=err, anchor=tkinter.NW, tag="err_img")
    err_cnv.place(x=-int(test_data.err_loc_x), y=-int(test_data.err_loc_y))

    err_msg_cnv = tkinter.Canvas(test_window, bg="red", highlightthickness=0, width=params.err_msg_size_x, height=test_data.err_msg_size_y)
    err_msg_cnv.place(x=-int(test_data.err_msg_loc_x), y=-int(test_data.err_msg_loc_y))
    #err_msg_cnv.create_text((test_data.err_msg_size_x/2,params.err_msg_size_y/2),text=test_data.err_message, font=test_data.err_msg_font, fill="white", anchor=tkinter.CENTER, tag = "err_msg_txt")

    test_window.bind("<Key>", key_event)
    test_window.focus_set()
    test_window.mainloop()
