from tkinter import *
from window import window
import math
import statistics
from scipy import stats
import sys


def menu(run,canvas,canvas2):
    canvas.destroy()
    canvas2.destroy()
    run()

def quit():
    sys.exit()

def clean(canvas2,canvas,run):
   canvas.destroy()
   canvas2.destroy()
   oneT(run)



def result(canvas2,entry,entry2,canvas,clear_button):


    canvas.create_window(350, 48, window=clear_button)
    canvas2.delete('all')
    M=entry2.get()
    enteries_pure = [int(i) for i in entry.get().split(',')]
    alt_hypothesis = int(entry3.get())
    x = statistics.mean(enteries_pure)
    n = len(enteries_pure)
    S = statistics.stdev(enteries_pure)
    T = (x - int(M)) / (S / math.sqrt(n))
    o = n - 1
    a = 0.05
    t = abs(float("%.2f" % stats.t.ppf(a, o)))


    if alt_hypothesis == 1:
        a = a / 2
        t = abs(float("%.2f" % stats.t.ppf(a, o)))
        H1 = 'H1: M≠'
        if T > t and T < -t:
            canvas2.create_text(375, 165,
                               text="for T(" + str("%.2f" % T) + ")" + ">" + "t(" + str(t) + ")" + "/" + "T(" + str(
                                   "%.2f" % T) + ")" + "<" + "-t(" + str(-t) + ")" +
                                    "\nH0(M=" + str(M) + ")rejected" + "\nH1(M≠" + str(M) + ")accepted", fill="black",
                               font=('Calibri 12'))
        else:
            canvas2.create_text(375, 165,
                               text="for T(" + str("%.2f" % T) + ")" + ">" + "t(" + str(t) + ")" + "/" + "T(" + str(
                                   "%.2f" % T) + ")" + "<" + "-t(" + str(-t) + ")" +
                                    "\nH1(M≠" + str(M) + ")rejected" + "\nH0(M=" + str(M) + ")accepted", fill="black",
                               font=('Calibri 12'))
    elif alt_hypothesis == 2:
        H1 = 'H1: M<'
        if T < -t:
            canvas2.create_text(375, 165,
                               text="for T(" + str("%.2f" % T) + ")" + "<" + "-t(" + str(-t) + ")" +
                                    "\nH0(M=" + str(M) + ")rejected\nH1(M<" + str(M) + ")accepted", fill="black",
                               font=('Calibri 12'))
        else:
            canvas2.create_text(375, 165,
                               text="for T(" + str("%.2f" % T) + ")" + "<" + "-t(" + str(-t) + ")" +
                                    "\nH1(M<" + str(M) + ")rejected"+"\nH0(M=" + str(M) + ")accepted", fill="black",
                               font=('Calibri 12'))
    elif alt_hypothesis == 3:
        H1='H1: M>'
        if T > t:
            canvas2.create_text(375, 165,
                               text="for T(" + str("%.2f" % T) + ")" + ">" + "t(" + str(t) + ")" +
                                    "\nH0(M=" + str(M) + ")rejected" + "\nH1(M>" + str(M) + ")accepted", fill="black",
                               font=('Calibri 12'))
        else:
            canvas2.create_text(375, 165,
                               text="for T(" + str("%.2f" % T) + ")" + ">" + "t(" + str(t) + ")" +
                                    "\nH1(M>" + str(M) + ")rejected" + "\nH0(M=" + str(M) + ")accepted", fill="black",
                               font=('Calibri 12'))


    canvas2.create_text(10, 100, text="Samples:" + str(enteries_pure) +
                                      "\nH0: M=" + str(M) +
                                      "\n"+H1+ str(M) +
                                      "\nNumber of Sample(n):" + str(n) +
                                      "\nSample mean:" + str("%.2f" % x) +
                                      "\nSample standard deviation:" + str("%.2f" % S) +
                                      "\nT value:" + str("%.2f" % T) +
                                      "\nDegree of freedom:" + str(o) +
                                      "\nSignificance level:" + str(a) +
                                      "\nt(" + str(o) + "," + str(a) + ")=" + str(t),
                       fill="black", font=('Calibri 12'),anchor=W)




def tTest(canvas,canvas2,entry,entry2,en,clear_button):

    a = entry2.get()
    canvas.create_text(110, 130, text="Choose alternative hypothesis:"
                       "\n1) H1: M≠" +a+"\n2) H1: M<" +a+"\n3) H1: M>" +a,
                       fill="black", font=('Calibri 12'))
    global entry3
    entry3 = Entry(window, width=4)
    canvas.create_window(230, 100, window=entry3)
    canvas.delete(en)
    enter_button = Button(text='Enter', command=lambda: result(canvas2,entry,entry2,canvas,clear_button), font=('helvetica', 9, 'bold'))
    canvas.create_window(200, 48, window=enter_button)

def oneT(run):

    window.title("One Sample T-test")
    canvas = Canvas(window, width=500, height=170)
    canvas2 = Canvas(window, width=500, height=300)


    canvas.create_text(110, 20, text="Enter sample data with comma:", fill="black", font=('Calibri 12'))
    entry = Entry(window,width=25)
    canvas.create_window(85, 40, window=entry)

    canvas.create_text(80, 70, text="Enter null hypothesis:\nH0: M=", fill="black", font=('Calibri 12'))
    entry2 = Entry(window,width=4)
    canvas.create_window(75, 80, window=entry2)

    enter_button = Button(text='Enter', command=lambda: tTest(canvas,canvas2,entry,entry2,en,clear_button), font=('helvetica', 9, 'bold'))
    en=canvas.create_window(200, 48, window=enter_button)

    main_menu = Button(text='Menu', command=lambda: menu(run, canvas, canvas2), font=('helvetica', 9, 'bold'))
    canvas.create_window(250, 48, window=main_menu)

    quit_button = Button(text='Quit', command=quit, font=('helvetica', 9, 'bold'))
    canvas.create_window(300, 48, window=quit_button)

    clear_button = Button(text='Clear', command=lambda: clean(canvas2, canvas,run), font=('helvetica', 9, 'bold'))




    canvas.pack()
    canvas2.pack()
    window.mainloop()
