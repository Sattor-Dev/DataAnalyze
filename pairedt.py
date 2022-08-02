from tkinter import *
from window import window
import math
import statistics
from scipy import stats
import sys
from scipy.stats import sem
import numpy as np

def menu(run,canvas,canvas2):
    canvas.destroy()
    canvas2.destroy()
    run()

def clean(canvas2,canvas,run):
   canvas.destroy()
   canvas2.destroy()
   pairedT(run)

def table(tuple_list,canvas2):

    total_rows = len(tuple_list)
    total_columns = len(tuple_list[0])
    t = 80

    for i in range(total_rows):
        t += 20
        c = 60
        for j in range(total_columns):
            e = Entry(window, width=12, fg='blue',
                      font=('Arial', 10, 'bold'), justify=CENTER)
            if (tuple_list[i][j] =="Group(x-y)" or tuple_list[i][j] == " "):
                e.insert(END, tuple_list[i][j])
                e.configure(width=12, disabledforeground='black', state=DISABLED, justify=LEFT)
                canvas2.create_window(c, t, window=e)
                c += 75
            elif (tuple_list[i][j] in tuple_list[0]):
                e.insert(END, tuple_list[i][j])
                e.configure(disabledforeground='black', state=DISABLED)
                canvas2.create_window(c, t, window=e)
                c += 75
            else:
                e.insert(END, tuple_list[i][j])
                e.configure(disabledforeground='black', state=DISABLED)
                canvas2.create_window(c, t, window=e)
                c += 75



def pairedTtest(canvas,canvas2,entry_x,entry_y,hypo_entry,clear_button):

    canvas2.delete('all')

    canvas.create_window(400, 50, window=clear_button)



    enteries_x = [int(i) for i in entry_x.get().split(',')]
    enteries_y = [int(i) for i in entry_y.get().split(',')]
    comma_list=[]
    s=0
    while s<len(np.subtract(enteries_x, enteries_y)):
        comma_list.append(np.subtract(enteries_x, enteries_y)[s])
        comma_list.append(',')
        s+=1
    comma_list.pop()

    canvas2.create_text(50, 40, text="Entered data:\n" + "Group-x: \n" + "Group-y: \n"+"Group(x-y): ", fill="black", font=('Calibri 11'))
    canvas2.create_text(90, 32, text=list(entry_x.get()), fill="black", font=('Calibri 11'),  anchor="w")
    canvas2.create_text(90, 50, text=list(entry_y.get()), fill="black", font=('Calibri 11'),  anchor="w")
    canvas2.create_text(90, 68, text=list(comma_list), fill="black", font=('Calibri 11'),  anchor="w")



    if hypo_entry.get() == '1':
        alt_hypo = "Md≠0"
    elif hypo_entry.get() == '2':
        alt_hypo = "Md<0"
    elif hypo_entry.get() == '3':
        alt_hypo = "Md>0"
    else:
        alt_hypo = "null"

    canvas2.create_text(250, 25, text="H0: Md=0\nH1: " + alt_hypo, fill="black", font=('Calibri 11'), anchor="w")

    l = np.subtract(enteries_x,enteries_y)
    new_list = [(" ", "Size", "Mean", "SD", "Variance", "SE Mean")]


    new_tuple1 = []
    new_tuple1.append("Group(x-y)")
    new_tuple1.append(len(l))
    new_tuple1.append(float("%.2f" % statistics.mean(l)))
    new_tuple1.append(float("%.2f" % statistics.stdev(l)))
    new_tuple1.append(float("%.2f" % statistics.variance(l)))
    new_tuple1.append(float("%.2f" % (sem(l))))
    new_tuple2 = tuple(new_tuple1)
    new_list.append(new_tuple2)

    table(new_list, canvas2)


    T = statistics.mean(l) / math.sqrt(statistics.variance(l) / len(l))

    o = len(l) - 1
    a = 0.05
    ll=0.05

    if hypo_entry.get() == '1':
        a = a / 2


    t = abs(float("%.2f" % stats.t.ppf(a, o)))
    canvas2.create_text(10, 165, text="\nT value:" + str("%.2f" % T) +
                                      "\nDegree of freedom:" + str(o) +
                                      "\nSignificance level:" + str(ll) +
                                      "\nt(" + str(o) + "," + str(a) + ")=" + str(t), fill="black",font=('Calibri 11'), anchor="w")

    if hypo_entry.get() == '1':
       if T > t and T < -t:
            canvas2.create_text(300, 165,text="for T(" + str("%.2f" % T) + ")" + ">" + "t(" + str(t) + ")" + "/" + "T(" + str(
                "%.2f" % T) + ")" + "<" + "-t(" + str(-t) + ")" +
                                     "\nH0(Md=0)rejected" + "\nH1(Md≠0)accepted", fill="black",font=('Calibri 11'))
       else:
            canvas2.create_text(300,165, text="for T(" + str("%.2f" % T) + ")" + ">" + "t(" + str(t) + ")" + "/" + "T(" + str(
                "%.2f" % T) + ")" + "<" + "-t(" + str(-t) + ")" +
                                                 "\nH1(Md≠0)rejected\nH0(Md=0) accepted", fill="black",font=('Calibri 11'))

    elif hypo_entry.get()=='2':

            if T < -t:
                canvas2.create_text(300, 165, text="for T(" + str("%.2f" % T) + ")" + "<" + "-t(" + str(-t) + ")" +
                                                   "\nH0(Md=0)rejected\nH1(Md<0)accepted", fill="black",font=('Calibri 11'))
            else:
                canvas2.create_text(300, 165, text="for T(" + str("%.2f" % T) + ")" + "<" + "-t(" + str(-t) + ")" +
                                                   "\nH1(Md<0)rejected\nH0(Md=0)accepted", fill="black",font=('Calibri 11'))
    elif hypo_entry.get()=='3':

            if T > t:
                canvas2.create_text(300, 165, text="for T(" + str("%.2f" % T) + ")" + ">" + "t(" + str(t) + ")" +
                                                   "\nH0(Md=0)rejected" + "\nH1(Md>0)accepted", fill="black",font=('Calibri 11'))

            else:
                canvas2.create_text(300, 165, text="for T(" + str("%.2f" % T) + ")" + ">" + "t(" + str(t) + ")" +
                                                   "\nH1(Md>0)rejected\nH0(Md=0)accepted", fill="black",font=('Calibri 11'))




def pairedT(run):

    window.title("Paired T-test")
    canvas = Canvas(window, width=500, height=177)
    canvas2 = Canvas(window, width=500, height=225)


    canvas.create_text(80, 10, text="Enter data with comma", fill="black", font=('Calibri 12'))

    canvas.create_text(45, 40, text="For group-x:", fill="black", font=('Calibri 12'))
    entry_x = Entry(window)
    canvas.create_window(155, 40, window=entry_x)

    # Second entry
    canvas.create_text(45, 65, text="For group-y:", fill="black", font=('Calibri 12'))
    entry_y = Entry(window)
    canvas.create_window(155, 65, window=entry_y)

    canvas.create_text(130, 120, text="\nH0: Md=0"+"\nPlease choose alternative hypothesis:"+
                       "\n1) H1: Md≠0 (Two-tailed)"+
                       "\n2) H1: Md<0 (Left-tailed)"+
                       "\n3) H1: Md>0 (Right-Tailed)",
                        fill="black", font=('Calibri 12'))


    hypo_entry = Entry(window, width=4)
    canvas.create_window(272, 110, window=hypo_entry)


    # Submit button
    submit_button = Button(text='Enter', command=lambda: pairedTtest(canvas,canvas2,entry_x,entry_y,hypo_entry,clear_button), font=('helvetica', 9, 'bold'))
    canvas.create_window(250, 50, window=submit_button)


    main_menu = Button(text='Menu', command=lambda: menu(run, canvas, canvas2), font=('helvetica', 9, 'bold'))
    canvas.create_window(300, 50, window=main_menu)

    clear_button = Button(text='Clear', command=lambda: clean(canvas2, canvas,run), font=('helvetica', 9, 'bold'))

    quit_button = Button(text='Quit', command=lambda: sys.exit(), font=('helvetica', 9, 'bold'))
    canvas.create_window(350, 50, window=quit_button)


    canvas.pack()
    canvas2.pack()
    window.mainloop()
