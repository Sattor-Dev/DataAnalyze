import tkinter.filedialog
from tkinter import *
from window import window
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

import sys
import xlrd


def menu(run,canvas,canvas2):
    canvas.destroy()
    canvas2.destroy()
    run()

def clean(canvas,canvas2,entry):
    canvas2.delete('all')
    entry.delete(0, 'end')

def quit():
    sys.exit()



def get_data(canvas,canvas2,entry,sheet):

        canvas2.delete('all')

        clear_button = Button(text='Clear', command=lambda:clean(canvas,canvas2,entry), font=('helvetica', 9, 'bold'))
        canvas.create_window(300, 110, window=clear_button)

        list_excel = []

        if entry.get() != '6':
            n = int(entry.get()) - 1
            for i in range(sheet.nrows):
                list_excel.append(sheet.cell_value(i, n))
            canvas2.create_text(250, 100, text=list_excel, fill="black", font=('Calibri 12'),width=480)

            list_excel.remove(list_excel[0])
            box_plot_data = [list_excel]
            plt.boxplot(box_plot_data)
            plt.show()
        else:
            print(entry.get())
            list_excel1 = []
            list_excel2 = []
            list_excel3 = []
            list_excel4 = []
            list_excel5 = []
            for t in range(sheet.nrows):
                list_excel1.append(sheet.cell_value(t, 0))
                list_excel2.append(sheet.cell_value(t, 1))
                list_excel3.append(sheet.cell_value(t, 2))
                list_excel4.append(sheet.cell_value(t, 3))
                list_excel5.append(sheet.cell_value(t, 4))
            list_excel1.remove(list_excel1[0])
            list_excel2.remove(list_excel2[0])
            list_excel3.remove(list_excel3[0])
            list_excel4.remove(list_excel4[0])
            list_excel5.remove(list_excel5[0])
            box_plot_data = [list_excel1, list_excel2, list_excel3, list_excel4, list_excel5]
            plt.boxplot(box_plot_data)
            plt.show()

def upload(canvas,canvas2):


    file = tkinter.filedialog.askopenfilename()
    wb = xlrd.open_workbook(file)
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0, 0)
    i=40
    sheet_list = sheet.row_values(0)
    sheet_list.append('6:All')
    for x in  range(len(sheet_list)):
        e = Entry(window, width=7, fg='blue',font=('Arial', 10, 'bold'),justify=CENTER)
        e.insert(END,sheet_list[x])
        e.configure(state=DISABLED,disabledforeground="black")
        canvas.create_window(i, 80, window=e)
        i+=55

    canvas.create_text(75, 110, text="Choose grade(1-6):", fill="black", font=('Calibri 12'))
    entry = Entry(window,width=2)
    canvas.create_window(150, 110, window=entry)
    enter_button = Button(text='Enter', command=lambda:get_data(canvas,canvas2,entry,sheet), font=('helvetica', 9, 'bold'))
    canvas.create_window(200, 110, window=enter_button)
    quit_button = Button(text='Quit', command=quit, font=('helvetica', 9, 'bold'))
    canvas.create_window(250, 110, window=quit_button)




def boxPlot(run):

    window.title("Boxplot")
    canvas = Canvas(window, width=500, height=140)
    canvas.create_text(80, 10, text="Select excel data file", fill="black", font=('Calibri 12'))

    canvas2 = Canvas(window, width=500, height=300)


    button_upload = Button(text='Upload', command=lambda:upload(canvas,canvas2), font=('helvetica', 9, 'bold'))
    canvas.create_window(40, 40, window=button_upload)

    main_menu = Button(text='Menu', command=lambda: menu(run, canvas, canvas2), font=('helvetica', 9, 'bold'))
    canvas.create_window(90, 40, window=main_menu)


    canvas.pack()
    canvas2.pack()
    window.mainloop()
