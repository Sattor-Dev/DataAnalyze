from tkinter import *
from window import window
import statistics
import os, sys


def menu(run,canvas,canvas2):
    canvas.destroy()
    canvas2.destroy()
    run()

def clean(run,canvas,canvas2):
    canvas.destroy()
    canvas2.destroy()
    basDisStat(run)

def quit():
    sys.exit()



def DisStat(canvas,canvas2,entry1,entry2,clean_button):
    canvas.create_window(400, 50, window=clean_button)

    enteries1_list = list(entry1.get())
    enteries2_list = list(entry2.get())
    enteries1 = [int(i) for i in entry1.get().split(',')]
    enteries2 = [int(i) for i in entry2.get().split(',')]

    l = [enteries1, enteries2, enteries1 + enteries2]
    new_list = [(" ", "Max", "Min", "Sum", "Range", "Mean", "StDev", "Median", "Mode")]
    group = ['Group-A', 'Group-B', 'A and B']
    i = 0
    for x in l:
        new_tuple1 = []
        new_tuple1.append(group[i])
        new_tuple1.append(max(x))
        new_tuple1.append(min(x))
        new_tuple1.append(sum(x))
        new_tuple1.append(max(x) - min(x))
        new_tuple1.append("%.2f" % (sum(x) / len(x)))
        new_tuple1.append("%.2f" % (statistics.stdev(x)))
        new_tuple1.append(statistics.median(x))
        new_tuple1.append(statistics.mode(x))
        new_tuple2 = tuple(new_tuple1)
        new_list.append(new_tuple2)
        i += 1

    canvas.create_text(50, 110, text="Entered data:\n" + "Group-A: \n" + "Group-B: ", fill="black", font=('Calibri 11'))
    canvas.create_text(75, 110, text=enteries1_list, fill="black", font=('Calibri 11'), justify=LEFT, anchor="w")
    canvas.create_text(75, 128, text=enteries2_list, fill="black", font=('Calibri 11'), justify=LEFT, anchor="w")

    total_rows = len(new_list)
    total_columns = len(new_list[0])
    t = 10
    for i in range(total_rows):
        t += 20
        c = 7
        for j in range(total_columns):
            c += 50
            e = Entry(window, width=7, fg='blue',
                      font=('Calibri', 10), justify=CENTER)
            if (new_list[i][j] in group or new_list[i][j] == " "):
                e.insert(END, new_list[i][j])
                e.configure(width=10, disabledforeground='black', state=DISABLED, justify=LEFT)
                canvas2.create_window(c, t, window=e)
            elif (new_list[i][j] in new_list[0]):
                e.insert(END, new_list[i][j])
                e.configure(disabledforeground='black', state=DISABLED)
                canvas2.create_window(c, t, window=e)
            else:
                e.insert(END, new_list[i][j])
                e.configure(disabledforeground='black', state=DISABLED)
                canvas2.create_window(c, t, window=e)


def basDisStat(run):

    window.title("Basic Descriptive Statistics")
    canvas = Canvas(window, width=500, height=150)
    canvas.create_text(80, 10, text="Enter data with comma", fill="black", font=('Calibri 12'))

    canvas2 = Canvas(window, width=500, height=200)


    #First entry
    canvas.create_text(45, 40, text="For group-A:", fill="black", font=('Calibri 12'))
    entry1 = Entry(window)
    canvas.create_window(155, 40, window=entry1)

    #Second entry
    canvas.create_text(45, 65, text="For group-B:", fill="black", font=('Calibri 12'))
    entry2 = Entry(window)
    canvas.create_window(155, 65, window=entry2)


    submit_button = Button(text='Enter', command=lambda:DisStat(canvas,canvas2,entry1,entry2,clean_button), font=('helvetica', 9, 'bold'))
    canvas.create_window(250, 50, window=submit_button)

    main_menu = Button(text='Menu', command=lambda: menu(run, canvas, canvas2), font=('helvetica', 9, 'bold'))
    canvas.create_window(300, 50, window=main_menu)

    quit_button = Button(text='Quit', command=quit, font=('helvetica', 9, 'bold'))
    canvas.create_window(350, 50, window=quit_button)

    clean_button = Button(text='Clear', command=lambda: clean(run, canvas, canvas2), font=('helvetica', 9, 'bold'))



    canvas.pack()
    canvas2.pack()
    window.mainloop()

