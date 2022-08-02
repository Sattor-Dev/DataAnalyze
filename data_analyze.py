import sys
from tkinter import *
from window import window
from basdisstat import basDisStat
from boxplot import boxPlot
from histogram import histogram
from onet import oneT
from pairedt import pairedT
from percentile import percentile
from twot import twoT
from resource_path import resource_path



def quit():
    sys.exit()

def delete_canvas(main):
    main.destroy()


def create_btn(main_canvas,text,width,height,x,y,com):


    new_btn=Button(text=text,width=width,height=height, command=com)
    main_canvas.create_window(x,y,window=new_btn)


def run():
    window.title("DataAnalyze by Sattoroff")
    window.geometry("500x400")
    bg = PhotoImage(file=resource_path("images/background.png"))
    main_canvas = Canvas(window, width=500, height=400)
    main_canvas.pack()
    main_canvas.create_image(0, 0, image=bg,
                         anchor="nw")
    list = ["Basic Descriptive Statistics", "Histogram", "Boxplot", "Percentile", "One Sample T-test",
            "Two Sample T-test", "Paired T-test", "Quit"]
    com = [lambda: [delete_canvas(main_canvas), basDisStat(run)],
           lambda: [delete_canvas(main_canvas), histogram(run)],
           lambda: [delete_canvas(main_canvas), boxPlot(run)],
           lambda: [delete_canvas(main_canvas), percentile(run)],
           lambda: [delete_canvas(main_canvas), oneT(run)],
           lambda: [delete_canvas(main_canvas), twoT(run)],
           lambda: [delete_canvas(main_canvas), pairedT(run)], quit]

    i = 25
    t = 0
    j = "btn"
    for name in list:
        create_btn(main_canvas,name, 25, 2, 250, i, com[t])
        i += 50
        t += 1

    window.mainloop()


run()