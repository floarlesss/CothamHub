version = "0.0.0"


import os
import urllib.request as urllib2
from pathlib import Path
from configparser import ConfigParser
from datetime import datetime

import tkinter as tk
from tkinter import messagebox
from tkinter import *

# Grab the config.ini file, and get the user's username. We will do something if the username is "Null" later.
this_file = Path(__file__)
configfile = this_file / ".." / "config.ini"

config = ConfigParser()
config.read(configfile)

username = config["username"]["username"]





# Configure tkinter, by creating a tkinter object and configuring the window settings.
window = tk.Tk()
window.geometry('900x500')
window.configure(bg='blue')
window.resizable(False, False)
window.attributes('-alpha', 0.0)
window.title("PREVIEW: BehaviourApp")

# Position the tkinter window in the middle of the screen. (personally, i like this)
def center_window(w=900, h=500):
    # get screen width and height
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    # calculate position x, y
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))


# 
# Initial setup is done, here we create the name label and other labels that are on the start page of CothamHub.
#
name = tk.Label(
    window,
    bg='blue',
    fg='white',
    font=('Helvetica', '32'),
    text="CothamHub"
)
name.pack(pady=(210, 0))

slogan = tk.Label(window,
                  bg='blue',
                  fg='lightgrey',
                  font=('Arial', '15'),
                  text="Assisting education."
                  )
slogan.pack(pady=(5, 50))



# This variable is for fading in the window. The function is for the same purpose too.
count = 0.0
def fadein():
    global count
    count += 0.1

    if count > 0.9:
        window.attributes('-alpha', 1)

        global status_label
        status_label = tk.Label(window,
                                bg='blue',
                                fg='black',
                                font=('Arial', '20'),
                                text='Checking for updates...'
                                )
        status_label.pack(pady=(20, 0))

        window.after(1, updateChecker)

    else:
        window.attributes('-alpha', count)
        window.after(25, fadein)






window.after(0, center_window)
window.after(1, fadein)
window.mainloop()