from tkinter import *
from window import window
import math
import statistics
from scipy import stats
import sys
from scipy.stats import sem


def menu(run,canvas,canvas2):
    canvas.destroy()
    canvas2.destroy()
    run()

def clean(canvas2,canvas,run):
   canvas.destroy()
   canvas2.destroy()
   twoT(run)

def table(tuple_list,canvas2):
    group = ['Group-x: ', 'Group-y: ', 'Difference: ']
    total_rows = len(tuple_list)
    total_columns = len(tuple_list[0])
    t = 110

    for i in range(total_rows):
        t += 20
        c = 60
        for j in range(total_columns):
            e = Entry(window, width=12, fg='blue',
                      font=('Arial', 10, 'bold'), justify=CENTER)
            if (tuple_list[i][j] in group or tuple_list[i][j] == " "):
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



def twoTtest(canvas,canvas2,entry_x,entry_y,hypo_entry,var_entry,clear_button):
    window.geometry("500x600")
    canvas2.delete('all')


    canvas.create_window(400, 50, window=clear_button)

    enteries_x = [int(i) for i in entry_x.get().split(',')]
    enteries_y = [int(i) for i in entry_y.get().split(',')]
    canvas2.create_text(50, 40, text="Entered data:\n" + "Group-x: \n" + "Group-y: ", fill="black", font=('Calibri 11'))
    canvas2.create_text(75, 40, text=list(entry_x.get()), fill="black", font=('Calibri 11'),  anchor="w")
    canvas2.create_text(75, 60, text=list(entry_y.get()), fill="black", font=('Calibri 11'),  anchor="w")

    Xx = statistics.mean(enteries_x)
    Xy = statistics.mean(enteries_y)
    n = len(enteries_x)
    m = len(enteries_y)
    Sx = statistics.variance(enteries_x)
    Sy = statistics.variance(enteries_y)
    SDx = statistics.stdev(enteries_x)
    SDy = statistics.stdev(enteries_y)

    if hypo_entry.get() == '1':
        alt_hypo = "Mx≠My"
    elif hypo_entry.get() == '2':
        alt_hypo = "Mx<My"
    elif hypo_entry.get() == '3':
        alt_hypo = "Mx>My"
    else:
        alt_hypo = "null"

    canvas2.create_text(10, 90, text="H0: Mx=My\nH1: " + alt_hypo, fill="black", font=('Calibri 11'), anchor="w")

    l = [enteries_x, enteries_y]
    new_list = [(" ", "Size", "Mean", "SD", "Variance", "SE Mean")]
    i = 0
    for x in l:
        new_tuple1 = []
        new_tuple1.append(len(x))
        new_tuple1.append(float("%.2f" % statistics.mean(x)))
        new_tuple1.append(float("%.2f" % statistics.stdev(x)))
        new_tuple1.append(float("%.2f" % statistics.variance(x)))
        new_tuple1.append(float("%.2f" % (sem(x))))
        # new_tuple2 = tuple(new_tuple1)
        new_list.append(new_tuple1)
        i += 1

    new_list.append(list(map(lambda i, j: float("%.2f" % (i - j)), new_list[1], new_list[2])))
    tuple_list = []
    new_list[1].insert(0, "Group-x: ")
    new_list[2].insert(0, "Group-y: ")
    new_list[3].insert(0, "Difference: ")
    for v in new_list:
        tuple_list.append(tuple(v))

    table(tuple_list, canvas2)


    if int(var_entry.get()) == 1:
        Sx1 = 0
        for i in enteries_x:
            Sx1 = pow((i - Xx), 2) + Sx1
        Sx2 = 0
        for x in enteries_y:
            Sx2 = pow((x - Xy), 2) + Sx2
        S = (Sx1 + Sx2) / ((n + m) - 2)
        T = (Xx - Xy) / math.sqrt(S * (1 / n + 1 / m))
        o = n + m - 2
        a = 0.05
        l=0.05
        if hypo_entry.get() == '1':
            a=a/2
        t = abs(float("%.2f" % stats.t.ppf(a, o)))


        canvas2.create_text(15, 260, text="\nDifference: Mu(Group(x)-Mu(Group(y))" +
                                          "\nEstimate for difference:" + str("%.2f" % (Xx - Xy)) +
                                          "\nT value:" + str("%.2f" % T) +
                                          "\nDegree of freedom:" + str(o) +
                                          "\nSignificance level:" + str(l) +
                                          "\nt(" + str(o) + "," + str(a) + ")=" + str(t), fill="black",
                            font=('Calibri 11'), anchor="w")

        if hypo_entry.get() == '1':
            t = abs(float("%.2f" % stats.t.ppf(a , o)))

            if T > t and T < -t:
                canvas2.create_text(350, 300, text="for T(" + str("%.2f" % T) + ")" + ">" + "t(" + str(t) + ")" + "/" + "T(" + str(
                    "%.2f" % T) + ")" + "<" + "-t(" + str(-t) + ")"+
                                    "\nH0(Mx=My)rejected" + "\nH1(Mx≠My)accepted", fill="black",
                                    font=('Calibri 11'))
            else:
                canvas2.create_text(350,300, text="for T(" + str("%.2f" % T) + ")" + ">" + "t(" + str(t) + ")" + "/" + "T(" + str(
                    "%.2f" % T) + ")" + "<" + "-t(" + str(-t) + ")" +
                                                 "\nH1(Mx≠My)rejected\nH0(Mx=My) accepted", fill="black",
                                    font=('Calibri 11'))

        elif hypo_entry.get()=='2':

            if T < -t:
                canvas2.create_text(350, 300, text="for T(" + str("%.2f" % T) + ")" + "<" + "-t(" + str(-t) + ")" +
                                                   "\nH0(Mx=My)rejected\nH1(Mx<My)accepted", fill="black",font=('Calibri 11'))
            else:
                canvas2.create_text(350, 300, text="for T(" + str("%.2f" % T) + ")" + "<" + "-t(" + str(-t) + ")" +
                                                   "\nH1(Mx<My)rejected\nH0(Mx=My)accepted", fill="black",font=('Calibri 11'))
        elif hypo_entry.get()=='3':

            if T > t:
                canvas2.create_text(350, 300, text="for T(" + str("%.2f" % T) + ")" + ">" + "t(" + str(t) + ")" +
                                                   "\nH0(Mx=My)rejected" + "\nH1(Mx>My)accepted", fill="black",font=('Calibri 11'))

            else:
                canvas2.create_text(350, 300, text="for T(" + str("%.2f" % T) + ")" + ">" + "t(" + str(t) + ")" +
                                                   "\nH1(Mx>My)rejected\nH0(Mx=My)accepted", fill="black",font=('Calibri 11'))

    elif var_entry.get()=='2':
        T = (Xx - Xy) / math.sqrt(Sx / n + Sy / m)
        o = int(pow((Sx / n + Sy / m), 2) / (pow((Sx / n), 2) / (n - 1) + pow((Sy / n), 2) / (m - 1)))
        a = 0.05
        l=0.05
        if hypo_entry.get() == '1':
            a=a/2
        t = abs(float("%.2f" % stats.t.ppf(a, o)))
        canvas2.create_text(15, 260, text="\nDifference: Mu(Group(x)-Mu(Group(y))" +
                                          "\nEstimate for difference:" + str("%.2f" % (Xx - Xy)) +
                                          "\nT value:" + str("%.2f" % T) +
                                          "\nDegree of freedom:" + str(o) +
                                          "\nSignificance level:" + str(l) +
                                          "\nt(" + str(o) + "," + str(a) + ")=" + str(t), fill="black",
                            font=('Calibri 11'), anchor="w")
        if hypo_entry.get()=='1':
            t = abs(float("%.2f" % stats.t.ppf(a, o)))
            if T > t and T < -t:
                canvas2.create_text(350, 300, text="for T(" + str("%.2f" % T) + ")" + ">" + "t(" + str(t) + ")" + "/" + "T(" + str(
                    "%.2f" % T) + ")" + "<" + "-t(" + str(-t) + ")" +
                                                   "\nH0(Mx=My)rejected" + "\nH1(Mx≠My)accepted", fill="black",font=('Calibri 11'))

            else:
                canvas2.create_text(350, 300, text="for T(" + str("%.2f" % T) + ")" + ">" + "t(" + str(t) + ")" + "/" + "T(" + str(
                    "%.2f" % T) + ")" + "<" + "-t(" + str(-t) + ")" +
                                                   "\nH1(Mx≠My)rejected\nH0(Mx=My)accepted", fill="black",font=('Calibri 11'))
        elif hypo_entry.get()=='2':
            if T < -t:
                canvas2.create_text(350, 300, text="for T(" + str("%.2f" % T) + ")" + "<" + "-t(" + str(-t) + ")" +
                                                   "\nH0(Mx=My)rejected\nH1(Mx<My)accepted", fill="black",font=('Calibri 11'))

            else:
                canvas2.create_text(350, 300, text="for T(" + str("%.2f" % T) + ")" + "<" + "-t(" + str(-t) + ")" +
                                                   "\nH1(Mx<My)rejected\nH0(Mx=My)accepted", fill="black",font=('Calibri 11'))
        elif hypo_entry.get()=='3':
            if T > t:
                canvas2.create_text(350, 300, text="for T(" + str("%.2f" % T) + ")" + ">" + "t(" + str(t) + ")" +
                                                   "\nH0(Mx=My)rejected" + "\nH1(Mx>My)accepted", fill="black",font=('Calibri 11'))

            else:
                canvas2.create_text(350, 300, text="for T(" + str("%.2f" % T) + ")" + ">" + "t(" + str(t) + ")" +
                                                   "\nH1(Mx>My)rejected\nH0(Mx=My)accepted", fill="black",font=('Calibri 11'))







def twoT(run):

    window.title("Two Sample T-test")

    canvas = Canvas(window, width=500, height=235)
    canvas2 = Canvas(window, width=500, height=450)


    canvas.create_text(80, 10, text="Enter data with comma", fill="black", font=('Calibri 12'))

    canvas.create_text(45, 40, text="For group-x:", fill="black", font=('Calibri 12'))
    entry_x = Entry(window)
    canvas.create_window(155, 40, window=entry_x)

    # Second entry
    canvas.create_text(45, 65, text="For group-y:", fill="black", font=('Calibri 12'))
    entry_y = Entry(window)
    canvas.create_window(155, 65, window=entry_y)

    canvas.create_text(130, 120, text="\nH0: Mx=My"+"\nPlease choose alternative hypothesis:"+
                       "\n1) H1: Mx≠My (Two-tailed)"+
                       "\n2) H1: Mx<My (Left-tailed)"+
                       "\n3) H1: Mx>My (Right-Tailed)",
                        fill="black", font=('Calibri 12'))

    canvas.create_text(82, 200, text="\nAssume equal variance:\n1)Yes\n2)No",
                       fill="black", font=('Calibri 12'))

    hypo_entry = Entry(window, width=4)
    canvas.create_window(272, 110, window=hypo_entry)

    var_entry = Entry(window, width=4)
    canvas.create_window(178, 190, window=var_entry)

    # Submit button
    submit_button = Button(text='Enter', command=lambda: twoTtest(canvas,canvas2,entry_x,entry_y,hypo_entry,var_entry,clear_button), font=('helvetica', 9, 'bold'))
    canvas.create_window(250, 50, window=submit_button)

    # Quit button
    quit_button = Button(text='Quit', command=lambda: sys.exit(), font=('helvetica', 9, 'bold'))
    canvas.create_window(350, 50, window=quit_button)

    main_menu = Button(text='Menu', command=lambda: menu(run, canvas,canvas2), font=('helvetica', 9, 'bold'))
    canvas.create_window(300, 50, window=main_menu)

    clear_button = Button(text='Clear', command=lambda: clean(canvas2, canvas,run), font=('helvetica', 9, 'bold'))

    canvas.pack()
    canvas2.pack()
    window.mainloop()
