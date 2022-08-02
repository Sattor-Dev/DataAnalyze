import tkinter.filedialog
from tkinter import *
from window import window
import xlrd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import sys


def menu(run,canvas,canvas2):
    canvas.destroy()
    canvas2.destroy()
    run()

def clean(canvas,canvas2,entry,run,file):

    canvas2.delete('all')
    upload(canvas,canvas2,run,file)




def quit():
    sys.exit()


def get_data(canvas,canvas2,entry,entry2,sheet,clear_button):

        canvas2.delete('all')


        canvas.create_window(300, 110, window=clear_button)

        list_excel = []
        n = int(entry.get()) - 1
        for i in range(sheet.nrows):
            list_excel.append(sheet.cell_value(i, n))


        canvas2.create_text(250, 100, text=list_excel, fill="black", font=('Calibri 12'),width=480)
        if entry2.get()!='':
            bin = int(entry2.get())
            n, bins, patches = plt.hist(list_excel, bin, facecolor='blue', alpha=1)
            plt.show()

        canvas2.create_text(80, 200, text='Enter number of bins:', fill="black", font=('Calibri 12'), width=480)
        canvas2.create_window(162, 198, window=entry2)

def open_file(canvas,canvas2,run):
    file = tkinter.filedialog.askopenfilename()
    upload(canvas,canvas2,run,file)

def upload(canvas,canvas2,run,file):



    wb = xlrd.open_workbook(file)
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0, 0)
    i=40
    for x in  range(len(sheet.row_values(0))):
        e = Entry(window, width=7, fg='blue',font=('Arial', 10, 'bold'),justify=CENTER)
        e.insert(END,sheet.row_values(0)[x])
        e.configure(state=DISABLED,disabledforeground="black")
        canvas.create_window(i, 80, window=e)
        i+=55
    canvas.create_text(75, 110, text="Choose grade(1-5):", fill="black", font=('Calibri 12'))

    entry = Entry(window,width=2)
    canvas.create_window(150, 110, window=entry)

    entry2 = Entry(window, width=2)

    enter_button1 = Button(text='Enter', command=lambda: get_data(canvas,canvas2,entry,entry2,sheet,clear_button), font=('helvetica', 9, 'bold'))
    canvas.create_window(200, 110, window=enter_button1)
    quit_button = Button(text='Quit', command=quit, font=('helvetica', 9, 'bold'))
    canvas.create_window(250, 110, window=quit_button)
    clear_button = Button(text='Clear', command=lambda: clean(canvas,canvas2, entry,run,file), font=('helvetica', 9, 'bold'))



def histogram(run):

    window.title("Histogram")
    canvas = Canvas(window, width=500, height=140)
    canvas.create_text(80, 10, text="Select excel data file", fill="black", font=('Calibri 12'))

    canvas2 = Canvas(window, width=500, height=300)


    button_upload = Button(text='Upload', command=lambda:open_file(canvas,canvas2,run), font=('helvetica', 9, 'bold'))
    canvas.create_window(40, 40, window=button_upload)

    main_menu = Button(text='Menu', command=lambda: menu(run,canvas, canvas2), font=('helvetica', 9, 'bold'))
    canvas.create_window(90, 40, window=main_menu)



    canvas.pack()
    canvas2.pack()
    window.mainloop()