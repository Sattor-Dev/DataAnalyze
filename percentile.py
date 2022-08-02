from tkinter import *
import sys
from window import window

def menu(run,canvas,canvas2):
    canvas.destroy()
    canvas2.destroy()
    run()


def quit():
    sys.exit()

def clean(canvas2,entry,entry2):
   canvas2.delete('all')
   entry.delete(0,'end')
   entry2.delete(0,'end')


def calculate(canvas,canvas2,entry,entry2):

    canvas2.delete('all')
    clear_button = Button(text='Clear', command=lambda:clean(canvas2,entry,entry2), font=('helvetica', 9, 'bold'))
    canvas.create_window(350, 48, window=clear_button)
    enteries = list(entry.get())
    enteries_pure = [int(i) for i in entry.get().split(',')]
    canvas2.create_text(50, 10, text="Entered data:", fill="black", font=('Calibri 12'))
    canvas2.create_text(100, 10, text=enteries, fill="black", font=('Calibri 12'), justify=LEFT, anchor="w")
    enteries_pure.sort()

    k = float(entry2.get())
    k = k / 100
    N = len(enteries_pure)
    n = k * (N - 1) + 1
    i = int(n)
    d = n - i
    pk = enteries_pure[i - 1] + d * (enteries_pure[i] - enteries_pure[i - 1])

    canvas2.create_text(8, 40, text="Amount of data: " + str(N), fill="black", font=('Calibri 12'), anchor=W)
    canvas2.create_text(8, 60, text="Rank calculation: n=" + str(n), fill="black", font=('Calibri 12'), anchor=W)
    canvas2.create_text(8, 80, text="Rank decomposition: " + "i=" + str(i) + " " + "d=" + str("%.2f" % d), fill="black",font=('Calibri 12'), anchor=W)
    canvas2.create_text(8, 100, text="Percentile value calculation: " + str("%.2f" % pk), fill="black", font=('Calibri 12'),anchor=W)

def percentile(run):

    window.title("Percentile")

    canvas = Canvas(window, width=500, height=100)
    canvas.create_text(85, 20, text="Enter data with comma:", fill="black", font=('Calibri 12'))

    canvas2 = Canvas(window, width=500, height=300)

    entry = Entry(window,width=25)
    canvas.create_window(85, 50, window=entry)
    canvas.create_text(75, 80, text="Enter percentile rank:", fill="black", font=('Calibri 12'))
    entry2 = Entry(window, width=2)
    canvas.create_window(160, 80, window=entry2)

    submit_button = Button(text='Enter', command=lambda:calculate(canvas,canvas2,entry,entry2), font=('helvetica', 9, 'bold'))
    canvas.create_window(200, 48, window=submit_button)

    main_menu = Button(text='Menu', command=lambda: menu(run, canvas, canvas2), font=('helvetica', 9, 'bold'))
    canvas.create_window(250, 48, window=main_menu)

    quit_button = Button(text='Quit', command=quit, font=('helvetica', 9, 'bold'))
    canvas.create_window(300, 48, window=quit_button)



    canvas.pack()
    canvas2.pack()
    window.mainloop()
