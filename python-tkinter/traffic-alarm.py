#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  traffic-alarm.py
#
#  Copyright 2015 Josh Neudorf <neudorf@users.noreply.github.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#  Credit to Sean Gallo for the traffic light vector image. 
#  https://seangallodesigns.files.wordpress.com/2011/05/stoplight.png
#
#  For use with Python 2.x
#  Tested with Python 2.7
#

from Tkinter import *
import tkMessageBox
import ttk
from datetime import *

class trafficLight():
    def __init__(self, master):
        time1 = ''
        self.master = master
        self._createGUI()

    def _createGUI(self):
        bgcolor = 'black'
        fgcolor = 'white'
        self.master.configure(background = bgcolor)
        self.master.title('Traffic Light Alarm')
        self.master.resizable(False,False)
        self.style = ttk.Style()
        self.style.configure('TFrame', background = bgcolor, foreground = fgcolor)
        self.style.configure('TButton', background = bgcolor, foreground = fgcolor, font = ('Arial Black', 10))
        self.style.configure('TLabel', background = bgcolor, foreground = fgcolor, font = ('Arial Black', 10))
        self.style.configure('Status.TLabel', background = bgcolor, foreground = fgcolor, font = ('Arial', 10))
        self.style.configure('Result.TLabel', background = bgcolor, foreground = fgcolor, font = ('Courier', 10))
        # create and display header frame with image
        self.frame_header = ttk.Frame(self.master)
        self.frame_header.pack(side = TOP)
        self.logo = PhotoImage(file="stoplightRed.png")
        self.header_label = ttk.Label()
        self.header_label.logo = self.logo
        self.header_label = ttk.Label(self.frame_header, image = self.header_label.logo)
        self.header_label.pack(side=TOP)
        # create and display frame to hold user input widgets
        self.frame_input = ttk.Frame(self.master)
        self.frame_input.pack(side = TOP)

        ttk.Label(self.frame_input, text = 'Bed Time:').grid(row = 0, column = 1, columnspan = 3, sticky = 'sw')
        ttk.Label(self.frame_input, text = 'Wake Time:').grid(row = 0, column = 5, columnspan = 3, sticky = 'sw')

        self.start_minute = StringVar()
        self.start_hour = StringVar()
        self.end_minute = StringVar()
        self.end_hour = StringVar()
        # create a Spinbox for each hour/minute of start/end
        Spinbox(self.frame_input, from_ = 0, to = 24,
                textvariable = self.start_hour, width = 2,
                font = 'Courier 12').grid(row = 1, column = 1)
        Spinbox(self.frame_input, from_ = 0, to = 59,
                textvariable = self.start_minute, width = 2,
                font = 'Courier 12').grid(row = 1, column = 2)
        Spinbox(self.frame_input, from_ = 0, to = 12,
                textvariable = self.end_hour, width = 2,
                font = 'Courier 12').grid(row = 1, column = 5)
        Spinbox(self.frame_input, from_ = 0, to = 59,
                textvariable = self.end_minute, width = 2,
                font = 'Courier 12').grid(row = 1, column = 6)

        # set default start and end dates
        self.start_hour.set(20)
        self.start_minute.set(0)
        self.end_hour.set(6)
        self.end_minute.set(0)

        ttk.Button(self.frame_input, text = 'Submit',
                   command = self._submit_callback).grid(row = 3, column = 0, columnspan = 9, pady = 5)

    def _submit_callback(self):
        try:
            start = time(int(self.start_hour.get()),int(self.start_minute.get()),0)
            end = time(int(self.end_hour.get()),int(self.end_minute.get()),0)
        except ValueError as e:
            tkMessageBox.showerror(title = 'ValueError',
                                message = ('Invalid time range\nBed Time: {}\nWake Time: {}\n').format(start, end))
            self.start_hour.set(20)
            self.start_minute.set(0)
            self.end_hour.set(6)
            self.end_minute.set(0)
            return
        self.current = datetime.now()
        if start >= time(self.current.hour,self.current.minute,self.current.second) >= end:
            self.logo = PhotoImage(file="stoplightGreen.png")
        else:
            self.logo = PhotoImage(file="stoplightRed.png")
        self.header_label.logo = self.logo
        self.header_label.config(image = self.header_label.logo)
        self.master.after(500,self._submit_callback)


def main():
    root = Tk()
    app = trafficLight(root)
    root.mainloop()
if __name__ == '__main__': main()
