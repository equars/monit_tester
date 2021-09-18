#Monitor reflex test for ***.
#before use, check the README.md file

#====libs====
import os
import sys
import tkinter
#====usr libs====
import class_lib as cl
import view
import util
import tkinter_setting as tk_s

#properties
version = "v0.0"
conf_file = "configure.ini"

#read setting file(class definition of params is in README.md)
params=cl.Setting_params()
params.read(conf_file)

#====main session====
if __name__ == "__main__":
    #define root window
    root=tkinter.Tk()
    root.title("Monitor Reflex Test") #window name
    root.geometry("400x300") #window size

    #root messages
    title_main = tkinter.Label(root, text="モニタ視認性試験", font=tk_s.f_main_title)
    title_version = tkinter.Label(root, text=version)
    title_comment = tkinter.Label(root, text="モニタ視認性試験を行います。SETTINGを確認して、STARTボタンを押してください。")

    #root buttons
    button_setting = tkinter.Button(root, text="SETTING", command=lambda:view.setting_clicked(params))
    button_start = tkinter.Button(root, text="START", command=lambda:view.start_clicked(params,1))
    button_end = tkinter.Button(root, text="END", command=exit)

    #root plotting elements
    title_main.pack(pady=20, side="top")
    title_version.pack(side="top")
    title_comment.pack(pady=5, side="top")

    button_setting.pack(padx=20, side="top")
    button_start.pack(fill="x", padx=20, side="right")
    button_end.pack(fill="x", padx=20, side="left")

    #root event loop(waiting)
    root.mainloop()

