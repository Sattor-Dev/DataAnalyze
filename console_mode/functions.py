def Bd():

    import statistics
    print("How much data do you want to enter?")

    d1 = float(input("For dataA = "))
    print("\n")
    list_dataA = []
    i = 0
    while i < d1:
         list_dataA.append(i)
         list_dataA[i] = float(input("Number(" + str(i+1) + ")="))
         i = i + 1
    print("\n")
    d2 = float(input("For dataB = "))
    print("\n")
    list_dataB = []
    c = 0
    while c < d2:
         list_dataB.append(c)
         list_dataB[c] = float(input("Number(" + str(c+1) + ")="))
         c = c + 1
    print("\n")
    print("dataA="+str(list_dataA))
    print("dataB="+str(list_dataB))
    print("\n")
    print(" dataA               dataB          data A and B")
    print("-------"+'             '+"-------"+'         '+"------------")
    print("Max="+str(max(list_dataA)),end="")
    print("             Max="+str(max(list_dataB)),end="")
    print("         Max="+str(max(list_dataA+list_dataB)))

    print("Min="+str(min(list_dataA)),end="")
    print("             Min="+str(min(list_dataB)),end="")
    print("         Min="+str(min(list_dataA+list_dataB)))

    print("Sum="+"%.2f"%(sum(list_dataA)),end="")
    print("           Sum="+"%.2f"%(sum(list_dataB)),end="")
    print("       Sum="+"%.2f"%(sum(list_dataA+list_dataB)))

    print("Range="+"%.2f"%(max(list_dataA)-min(list_dataA)),end="")
    print("          Range="+"%.2f"%(max(list_dataB)-min(list_dataB)),end="")
    print("      Range="+"%.2f"%(max(list_dataA+list_dataB)-min(list_dataA+list_dataB)))

    print("Mean="+"% .2f" % (sum(list_dataA)/len(list_dataA)),end="")
    print("          Mean="+"% .2f" % (sum(list_dataB)/len(list_dataB)),end="")
    print("      Mean="+"% .2f" % (sum(list_dataA+list_dataB)/len(list_dataA+list_dataB)))

    print("StDev="+"%.2f"%(statistics.stdev(list_dataA)),end="")
    print("          StDev="+"%.2f"%(statistics.stdev(list_dataB)),end="")
    print("      StDev="+"%.2f"%(statistics.stdev(list_dataA+list_dataB)))

    print("Median="+"%.2f"%(statistics.median(list_dataA)),end="")
    print("         Median="+"%.2f"%(statistics.median(list_dataB)),end="")
    print("     Median="+"%.2f"%(statistics.median(list_dataA+list_dataB)))
    try:
        print("Mode="+str(statistics.mode(list_dataA)),end="")
    except:
        print("Mode = Null",end="")

    try:
        print('            '+"Mode="+str(statistics.mode(list_dataB)),end="")
    except:
        print('         '+"Mode = Null",end="")

    try:
        print('         '+"Mode="+str(statistics.mode(list_dataA+list_dataB)))
    except:
        print('        '+"Mode = Null",end="")


def Hg():

    import numpy as np
    import matplotlib.mlab as mlab
    import matplotlib.pyplot as plt
    import xlrd

    loc = ("Grade.xlsx")

    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0, 0)

    list_excel = []
    print("\n","\n")
    print(sheet.row_values(0))
    n = int(input("\nWhich grade do you want to choose:"))
    n=n-1
    for i in range(sheet.nrows):
       list_excel.append(sheet.cell_value(i, n))

    first_value = list_excel[0]
    list_excel.remove(list_excel[0])
    print("\n"+str(first_value)+"="+str(list_excel))

    num_bins = int(input("\nPlease Enter number of bins:"))
    n, bins, patches = plt.hist(list_excel, num_bins, facecolor='blue', alpha=0.5)
    plt.show()


def Bp():
    import matplotlib.pyplot as plt
    import xlrd
    Data_set = ("Grade.xlsx")
    wb1 = xlrd.open_workbook(Data_set)
    sheet1 = wb1.sheet_by_index(0)
    sheet1.cell_value(0, 0)
    list_excel1 = []
    print("\n","\n")
    print(str(sheet1.row_values(0)) + " or All")
    n1 = str(input("\nWhich grade do you want to choose:"))
    if n1=='All':
        list_excel1 = []
        list_excel2 = []
        list_excel3 = []
        list_excel4 = []
        list_excel5 = []
        for i in range(sheet1.nrows):
              list_excel1.append(sheet1.cell_value(i, 0))
              list_excel2.append(sheet1.cell_value(i, 1))
              list_excel3.append(sheet1.cell_value(i, 2))
              list_excel4.append(sheet1.cell_value(i, 3))
              list_excel5.append(sheet1.cell_value(i, 4))
        first_value1 = list_excel1[0]
        first_value2 = list_excel2[0]
        first_value3 = list_excel3[0]
        first_value4 = list_excel4[0]
        first_value5 = list_excel5[0]
        list_excel1.remove(list_excel1[0])
        list_excel2.remove(list_excel2[0])
        list_excel3.remove(list_excel3[0])
        list_excel4.remove(list_excel4[0])
        list_excel5.remove(list_excel5[0])
        print("\n" + str(first_value1) + "=" + str(list_excel1))
        print("\n" + str(first_value2) + "=" + str(list_excel2))
        print("\n" + str(first_value3) + "=" + str(list_excel3))
        print("\n" + str(first_value4) + "=" + str(list_excel4))
        print("\n" + str(first_value5) + "=" + str(list_excel5))
        box_plot_data = [list_excel1,list_excel2,list_excel3,list_excel4,list_excel5]
        plt.boxplot(box_plot_data)
        plt.show()
    else:
         a = int(n1)
         a=a-1
         for i in range(sheet1.nrows):
            list_excel1.append(sheet1.cell_value(i, a))

         first_value1 = list_excel1[0]
         list_excel1.remove(list_excel1[0])
         print("\n"+str(first_value1)+"="+str(list_excel1))
         box_plot_data = [list_excel1]
         plt.boxplot(box_plot_data)
         plt.show()
def OneT():
    import math
    import statistics
    from scipy import stats
    import sys
    import os

    def clear():
        clear = lambda: os.system('cls')
        clear()

    clear()
    sample = float(input("Enter amount of sample:"))

    list_sample = []
    i = 0
    while i < sample:
        list_sample.append(i)
        list_sample[i] = float(input("Sample(" + str(i + 1) + ")" + "="))
        i = i + 1

    M = float(input("\nPlease enter null hypothesis\n H0: M ="))
    print("\nPlease choose alternative hypothesis")
    print("1) H1: M≠" + str(M))
    print("2) H1: M<" + str(M))
    print("3) H1: M>" + str(M))
    alt_hypothesis = int(input("Enter:"))

    x = statistics.mean(list_sample)
    n = len(list_sample)
    S = statistics.stdev(list_sample)
    T = (x - M) / (S / math.sqrt(n))

    o = n - 1
    a = 0.05

    t = abs(float("%.2f" % stats.t.ppf(a, o)))

    if alt_hypothesis == 1:
        clear()
        print("Samples:" + str(list_sample))
        print("H0: M=" + str(M))
        print("H1: M≠" + str(M))
        print("\n")
        print("Number of Sample(n):" + str(n))
        print("Sample mean:" + str("%.2f" % x))
        print("Sample standard deviation:" + str("%.2f" % S))
        print("T value:" + str("%.2f" % T))
        print("Degree of freedom:" + str(o))
        print("Significance level:" + str(a))
        a = a / 2
        t = abs(float("%.2f" % stats.t.ppf(a, o)))
        print("t(" + str(o) + "," + str(a) + ")=" + str(t))
        print("\n")
        if T > t and T < -t:
            print("for T(" + str("%.2f" % T) + ")" + ">" + "t(" + str(t) + ")" + "/" + "T(" + str(
                "%.2f" % T) + ")" + "<" + "-t(" + str(-t) + ")")
            print("H0(M=" + str(M) + ")rejected" + "\nH1(M≠" + str(M) + ")accepted")
        else:
            print("for T(" + str("%.2f" % T) + ")" + ">" + "t(" + str(t) + ")" + "/" + "T(" + str(
                "%.2f" % T) + ")" + "<" + "-t(" + str(-t) + ")")
            print("H1(M≠" + str(M) + ")rejected"+"\nH0(M=" + str(M) + ")accepted")
    elif alt_hypothesis == 2:
        clear()
        print("Samples:" + str(list_sample))
        print("H0: M=" + str(M))
        print("H1: M<" + str(M))
        print("\n")
        print("Number of Sample(n):" + str(n))
        print("Sample mean:" + str("%.2f" % x))
        print("Sample standard deviation:" + str("%.2f" % S))
        print("T value:" + str("%.2f" % T))
        print("Degree of freedom:" + str(o))
        print("Significance level:" + str(a))
        print("t(" + str(o) + "," + str(a) + ")=" + str(t))
        print("\n")
        if T < -t:
            print("for T(" + str("%.2f" % T) + ")" + "<" + "-t(" + str(-t) + ")")
            print("H0(M=" + str(M) + ")rejected\nH1(M<" + str(M) + ")accepted")
        else:
            print("for T(" + str("%.2f" % T) + ")" + "<" + "-t(" + str(-t) + ")")
            print("H1(M<" + str(M) + ")rejected"+"\nH0(M=" + str(M) + ")accepted")
    elif alt_hypothesis == 3:
        clear()
        print("Samples:" + str(list_sample))
        print("H0: M=" + str(M))
        print("H1: M>" + str(M))
        print("\n")
        print("Number of Sample:(n)" + str(n))
        print("Sample mean:" + str("%.2f" % x))
        print("Sample standard deviation:" + str("%.2f" % S))
        print("T value:" + str("%.2f" % T))
        print("Degree of freedom:" + str(o))
        print("Significance level:" + str(a))
        print("t(" + str(o) + "," + str(a) + ")=" + str(t))
        print("\n")
        if T > t:
            print("for T(" + str("%.2f" % T) + ")" + ">" + "t(" + str(t) + ")")
            print("H0(M=" + str(M) + ")rejected" + "\nH1(M>" + str(M) + ")accepted")
        else:
            print("for T(" + str("%.2f" % T) + ")" + ">" + "t(" + str(t) + ")")
            print("H1(M>" + str(M) + ")rejected"+"\nH0(M=" + str(M) + ")accepted")
    else:
        clear()
        print("Please choose again")
def Pk():
    import sys
    import os

    def clear():
        clear = lambda: os.system('cls')
        clear()
    clear()
    z = float(input("Amount of data:"))
    print("\n")
    list_data = []
    i = 0
    while i < z:
        list_data.append(i)
        list_data[i] = float(input("Number(" + str(i + 1) + ")="))
        i = i + 1

    list_data.sort()
    k = float(input("Enter percentile rank\nk="))
    k = k/100
    N = len(list_data)
    n = k*(N-1)+1
    i = int(n)
    d = n - i
    pk = list_data[i-1]+d*(list_data[i]-list_data[i-1])
    clear()
    print("data="+str(list_data))
    print("Number of data:"+str(N))
    print("rank calculation: n="+str(n))
    print("rank decomposition:"+"i="+str(i)+" "+"d="+str("%.2f"%d))
    print("percentile value calculation:"+str(pk))

def TwoT():
    import math
    import statistics
    from scipy import stats
    from scipy.stats import sem
    import sys
    import os

    def clear():
        clear = lambda: os.system('cls')
        clear()

    clear()
    print("Enter size of sample")
    sample1 = float(input("Group x:"))
    sample2 = float(input("Group y:"))

    list_sample1 = []
    list_sample2 = []
    i = 0
    print("\nGroup x")
    while i < sample1:
        list_sample1.append(i)
        list_sample1[i] = float(input("Data(" + str(i + 1) + ")" + "="))
        i = i + 1

    I = 0
    print("\nGroup y")
    while I < sample2:
        list_sample2.append(I)
        list_sample2[I] = float(input("Data(" + str(I + 1) + ")" + "="))
        I = I + 1

    print("\nH0: Mx=My")
    print("Please choose alternative hypothesis")
    print("1) H1: Mx≠My (Two-tailed)")
    print("2) H1: Mx<My (Left-tailed)")
    print("3) H1: Mx>My (Right-Tailed)")
    alt_hypothesis = int(input("Enter:"))

    variance = float(input("\nAssume equal variance\n1)Yes\n2)No\nEnter:"))

    Xx = statistics.mean(list_sample1)
    Xy = statistics.mean(list_sample2)
    n = len(list_sample1)
    m = len(list_sample2)
    Sx = statistics.variance(list_sample1)
    Sy = statistics.variance(list_sample2)
    SDx = statistics.stdev(list_sample1)
    SDy = statistics.stdev(list_sample2)

    Meandif = Xx - Xy
    Variancedif = Sx - Sy
    SDdif = SDx - SDy
    SDerdif = sem(list_sample1) - sem(list_sample2)

    if variance == 1:
        Sx1 = 0
        for i in list_sample1:
            Sx1 = pow((i - Xx), 2) + Sx1
        Sx2 = 0
        for x in list_sample2:
            Sx2 = pow((x - Xy), 2) + Sx2
        S = (Sx1 + Sx2) / ((n + m) - 2)
        T = (Xx - Xy) / math.sqrt(S * (1 / n + 1 / m))
        o = n + m - 2
        a = 0.05
        t = abs(float("%.2f" % stats.t.ppf(a, o)))
        if alt_hypothesis == 1:
            clear()
            print("Group(x):" + str(list_sample1))
            print("Group(y):" + str(list_sample2))
            print("H0: Mx=My")
            print("H1: Mx≠My")
            print("\n")
            print("Variable    Sample size" + "     Mean" + "     SD" + "     Variance" + "     SE Mean")
            print("Group(x):       " + str(n) + "          " + str("%.2f" % Xx) + "     " + str(
                "%.2f" % statistics.stdev(list_sample1)) + "     " + str(
                "%.2f" % statistics.variance(list_sample1) + "        " + str("%.2f" % sem(list_sample1))))
            print("Group(y):       " + str(m) + "          " + str("%.2f" % Xy) + "     " + str(
                "%.2f" % statistics.stdev(list_sample2)) + "     " + str(
                "%.2f" % statistics.variance(list_sample2) + "        " + str("%.2f" % sem(list_sample2))))
            print("Difference:     " + "    " + "       " + str("%.2f" % Meandif) + "     " + str(
                "%.2f" % SDdif) + "     " + str("%.2f" % Variancedif) + "        " + str("%.2f" % SDerdif))
            print("\nDifference: Mu(Group(x)-Mu(Group(y))")
            print("Estimate for difference:" + str(Meandif))
            print("\nT value:" + str("%.2f" % T))
            print("Degree of freedom:" + str(o))
            print("Significance level:" + str(a))
            a = a / 2
            t = abs(float("%.2f" % stats.t.ppf(a, o)))
            print("t(" + str(o) + "," + str(a) + ")=" + str(t))
            print("\n")
            if T > t and T < -t:
                print("for T(" + str("%.2f" % T) + ")" + ">" + "t(" + str(t) + ")" + "/" + "T(" + str(
                    "%.2f" % T) + ")" + "<" + "-t(" + str(-t) + ")")
                print("H0(Mx=My)rejected" + "\nH1(Mx≠My)accepted")
            else:
                print("for T(" + str("%.2f" % T) + ")" + ">" + "t(" + str(t) + ")" + "/" + "T(" + str(
                    "%.2f" % T) + ")" + "<" + "-t(" + str(-t) + ")")
                print("H1(Mx≠My)rejected\nH0(Mx=My) accepted")
        elif alt_hypothesis == 2:
            clear()
            print("Group(x):" + str(list_sample1))
            print("Group(y):" + str(list_sample2))
            print("H0: Mx=My")
            print("H1: Mx<My")
            print("\n")
            print("Variable    Sample size" + "     Mean" + "     SD" + "     Variance" + "     SE Mean")
            print("Group(x):       " + str(n) + "          " + str("%.2f" % Xx) + "     " + str(
                "%.2f" % statistics.stdev(list_sample1)) + "     " + str(
                "%.2f" % statistics.variance(list_sample1) + "        " + str("%.2f" % sem(list_sample1))))
            print("Group(y):       " + str(m) + "          " + str("%.2f" % Xy) + "     " + str(
                "%.2f" % statistics.stdev(list_sample2)) + "     " + str(
                "%.2f" % statistics.variance(list_sample2) + "        " + str("%.2f" % sem(list_sample2))))
            print("Difference:     " + "    " + "       " + str("%.2f" % Meandif) + "     " + str(
                "%.2f" % SDdif) + "     " + str("%.2f" % Variancedif) + "        " + str("%.2f" % SDerdif))
            print("\nDifference: Mu(Group(x)-Mu(Group(y))")
            print("Estimate for difference:" + str(Meandif))
            print("\nT value:" + str("%.2f" % T))
            print("Degree of freedom:" + str(o))
            print("Significance level:" + str(a))
            print("t(" + str(o) + "," + str(a) + ")=" + str(t))
            print("\n")
            if T < -t:
                print("for T(" + str("%.2f" % T) + ")" + "<" + "-t(" + str(-t) + ")")
                print("H0(Mx=My)rejected\nH1(Mx<My)accepted")
            else:
                print("for T(" + str("%.2f" % T) + ")" + "<" + "-t(" + str(-t) + ")")
                print("H1(Mx<My)rejected\nH0(Mx=My)accepted")
        elif alt_hypothesis == 3:
            clear()
            print("Group(x):" + str(list_sample1))
            print("Group(y):" + str(list_sample2))
            print("H0: Mx=My")
            print("H1: Mx>My")
            print("\n")
            print("Variable    Sample size" + "     Mean" + "     SD" + "     Variance" + "     SE Mean")
            print("Group(x):       " + str(n) + "          " + str("%.2f" % Xx) + "     " + str(
                "%.2f" % statistics.stdev(list_sample1)) + "     " + str(
                "%.2f" % statistics.variance(list_sample1) + "        " + str("%.2f" % sem(list_sample1))))
            print("Group(y):       " + str(m) + "          " + str("%.2f" % Xy) + "     " + str(
                "%.2f" % statistics.stdev(list_sample2)) + "     " + str(
                "%.2f" % statistics.variance(list_sample2) + "        " + str("%.2f" % sem(list_sample2))))
            print("Difference:     " + "    " + "       " + str("%.2f" % Meandif) + "     " + str(
                "%.2f" % SDdif) + "     " + str("%.2f" % Variancedif) + "        " + str("%.2f" % SDerdif))
            print("\nDifference: Mu(Group(x)-Mu(Group(y))")
            print("Estimate for difference:" + str(Meandif))
            print("\nT value:" + str("%.2f" % T))
            print("Degree of freedom:" + str(o))
            print("Significance level:" + str(a))
            print("t(" + str(o) + "," + str(a) + ")=" + str(t))
            print("\n")
            if T > t:
                print("for T(" + str("%.2f" % T) + ")" + ">" + "t(" + str(t) + ")")
                print("H0(Mx=My)rejected" + "\nH1(Mx>My)accepted")
            else:
                print("for T(" + str("%.2f" % T) + ")" + ">" + "t(" + str(t) + ")")
                print("H1(Mx>My)rejected\nH0(Mx=My)accepted")
        else:
            clear()
            print("Please choose again")

    elif variance == 2:

        T = (Xx - Xy) / math.sqrt(Sx / n + Sy / m)
        o = int(pow((Sx / n + Sy / m), 2) / (pow((Sx / n), 2) / (n - 1) + pow((Sy / n), 2) / (m - 1)))
        a = 0.05
        t = abs(float("%.2f" % stats.t.ppf(a, o)))
        if alt_hypothesis == 1:
            clear()
            print("Group(x):" + str(list_sample1))
            print("Group(y):" + str(list_sample2))
            print("H0: Mx=My")
            print("H1: Mx≠My")
            print("\n")
            print("Variable    Sample size" + "     Mean" + "     SD" + "     Variance" + "     SE Mean")
            print("Group(x):       " + str(n) + "          " + str("%.2f" % Xx) + "     " + str(
                "%.2f" % statistics.stdev(list_sample1)) + "     " + str(
                "%.2f" % statistics.variance(list_sample1) + "        " + str("%.2f" % sem(list_sample1))))
            print("Group(y):       " + str(m) + "          " + str("%.2f" % Xy) + "     " + str(
                "%.2f" % statistics.stdev(list_sample2)) + "     " + str(
                "%.2f" % statistics.variance(list_sample2) + "        " + str("%.2f" % sem(list_sample2))))
            print("Difference:     " + "    " + "       " + str("%.2f" % Meandif) + "     " + str(
                "%.2f" % SDdif) + "     " + str("%.2f" % Variancedif) + "        " + str("%.2f" % SDerdif))
            print("\nDifference: Mu(Group(x)-Mu(Group(y))")
            print("Estimate for difference:" + str(Meandif))
            print("\nT value:" + str("%.2f" % T))
            print("Degree of freedom:" + str(o))
            print("Significance level:" + str(a))
            a = a / 2
            t = abs(float("%.2f" % stats.t.ppf(a, o)))
            print("t(" + str(o) + "," + str(a) + ")=" + str(t))
            print("\n")
            if T > t and T < -t:
                print("for T(" + str("%.2f" % T) + ")" + ">" + "t(" + str(t) + ")" + "/" + "T(" + str(
                    "%.2f" % T) + ")" + "<" + "-t(" + str(-t) + ")")
                print("H0(Mx=My)rejected" + "\nH1(Mx≠My)accepted")
            else:
                print("for T(" + str("%.2f" % T) + ")" + ">" + "t(" + str(t) + ")" + "/" + "T(" + str(
                    "%.2f" % T) + ")" + "<" + "-t(" + str(-t) + ")")
                print("H1(Mx≠My)rejected\nH0(Mx=My)accepted")
        elif alt_hypothesis == 2:
            clear()
            print("Group(x):" + str(list_sample1))
            print("Group(y):" + str(list_sample2))
            print("H0: Mx=My")
            print("H1: Mx<My")
            print("\n")
            print("Variable    Sample size" + "     Mean" + "     SD" + "     Variance" + "     SE Mean")
            print("Group(x):       " + str(n) + "          " + str("%.2f" % Xx) + "     " + str(
                "%.2f" % statistics.stdev(list_sample1)) + "     " + str(
                "%.2f" % statistics.variance(list_sample1) + "        " + str("%.2f" % sem(list_sample1))))
            print("Group(y):       " + str(m) + "          " + str("%.2f" % Xy) + "     " + str(
                "%.2f" % statistics.stdev(list_sample2)) + "     " + str(
                "%.2f" % statistics.variance(list_sample2) + "        " + str("%.2f" % sem(list_sample2))))
            print("Difference:     " + "    " + "       " + str("%.2f" % Meandif) + "     " + str(
                "%.2f" % SDdif) + "     " + str("%.2f" % Variancedif) + "        " + str("%.2f" % SDerdif))
            print("\nDifference: Mu(Group(x)-Mu(Group(y))")
            print("Estimate for difference:" + str(Meandif))
            print("\nT value:" + str("%.2f" % T))
            print("Degree of freedom:" + str(o))
            print("Significance level:" + str(a))
            print("t(" + str(o) + "," + str(a) + ")=" + str(t))
            print("\n")
            if T < -t:
                print("for T(" + str("%.2f" % T) + ")" + "<" + "-t(" + str(-t) + ")")
                print("H0(Mx=My)rejected\nH1(Mx<My)accepted")
            else:
                print("for T(" + str("%.2f" % T) + ")" + "<" + "-t(" + str(-t) + ")")
                print("H1(Mx<My)rejected\nH0(Mx=My)accepted")
        elif alt_hypothesis == 3:
            clear()
            print("Group(x):" + str(list_sample1))
            print("Group(y):" + str(list_sample2))
            print("H0: Mx=My")
            print("H1: Mx>My")
            print("\n")
            print("Variable    Sample size" + "     Mean" + "     SD" + "     Variance" + "     SE Mean")
            print("Group(x):       " + str(n) + "          " + str("%.2f" % Xx) + "     " + str(
                "%.2f" % statistics.stdev(list_sample1)) + "     " + str(
                "%.2f" % statistics.variance(list_sample1) + "        " + str("%.2f" % sem(list_sample1))))
            print("Group(y):       " + str(m) + "          " + str("%.2f" % Xy) + "     " + str(
                "%.2f" % statistics.stdev(list_sample2)) + "     " + str(
                "%.2f" % statistics.variance(list_sample2) + "        " + str("%.2f" % sem(list_sample2))))
            print("Difference:     " + "    " + "       " + str("%.2f" % Meandif) + "     " + str(
                "%.2f" % SDdif) + "     " + str("%.2f" % Variancedif) + "        " + str("%.2f" % SDerdif))
            print("\nDifference: Mu(Group(x)-Mu(Group(y))")
            print("Estimate for difference:" + str(Meandif))
            print("\nT value:" + str("%.2f" % T))
            print("Degree of freedom:" + str(o))
            print("Significance level:" + str(a))
            print("t(" + str(o) + "," + str(a) + ")=" + str(t))
            print("\n")
            if T > t:
                print("for T(" + str("%.2f" % T) + ")" + ">" + "t(" + str(t) + ")")
                print("H0(Mx=My)rejected" + "\nH1(Mx>My)accepted")
            else:
                print("for T(" + str("%.2f" % T) + ")" + ">" + "t(" + str(t) + ")")
                print("H1(Mx>My)rejected\nH0(Mx=My)accepted")
        else:
            clear()
            print("Please choose again")
def PairedT():
    import math
    import statistics
    from scipy import stats
    from scipy.stats import sem
    import sys
    import os

    def clear():
        clear = lambda: os.system('cls')
        clear()

    clear()
    print("Enter size of sample")
    sample1 = float(input("Group x:"))
    sample2 = float(input("Group y:"))

    list_sample1 = []
    list_sample2 = []
    i = 0
    print("\nGroup x")
    while i < sample1:
        list_sample1.append(i)
        list_sample1[i] = float(input("Data(" + str(i + 1) + ")" + "="))
        i = i + 1

    I = 0
    print("\nGroup y")
    while I < sample2:
        list_sample2.append(I)
        list_sample2[I] = list_sample1[I] - float(input("Data(" + str(I + 1) + ")" + "="))
        I = I + 1

    print("\nH0: Md=0")
    print("Please choose alternative hypothesis")
    print("1) H1: Md≠0 (Two-tailed)")
    print("2) H1: Md<0 (Left-tailed)")
    print("3) H1: Md>0 (Right-Tailed)")
    alt_hypothesis = int(input("Enter:"))

    Mean = statistics.mean(list_sample2)
    n = len(list_sample2)
    Variance = statistics.variance(list_sample2)
    SD = statistics.stdev(list_sample2)

    T = Mean / math.sqrt(Variance / n)

    o = n - 1
    a = 0.05
    t = abs(float("%.2f" % stats.t.ppf(a, o)))
    if alt_hypothesis == 1:
        clear()
        print("Group(x-y):" + str(list_sample2))
        print("H0: Md=0")
        print("H1: Md≠0")
        print("Variable    Sample size" + "     Mean" + "     SD" + "     Variance" + "     SE Mean")
        print(
            "Group(x-y):     " + str(n) + "         " + str("%.2f" % Mean) + "     " + str("%.2f" % SD) + "     " + str(
                "%.2f" % Variance) + "        " + str("%.2f" % sem(list_sample2)))
        print("\nT value:" + str("%.2f" % T))
        print("Degree of freedom:" + str(o))
        print("Significance level:" + str(a))
        a = a / 2
        t = abs(float("%.2f" % stats.t.ppf(a, o)))
        print("t(" + str(o) + "," + str(a) + ")=" + str(t))
        print("\n")
        if T > t and T < -t:
            print("for T(" + str("%.2f" % T) + ")" + ">" + "t(" + str(t) + ")" + "/" + "T(" + str(
                "%.2f" % T) + ")" + "<" + "-t(" + str(-t) + ")")
            print("H0(Md=0)rejected" + "\nH1(Md≠0)accepted")
        else:
            print("for T(" + str("%.2f" % T) + ")" + ">" + "t(" + str(t) + ")" + "/" + "T(" + str(
                "%.2f" % T) + ")" + "<" + "-t(" + str(-t) + ")")
            print("H1(Md≠0)rejected\nH0(Md=0) accepted")
    elif alt_hypothesis == 2:
        clear()
        print("Group(x-y):" + str(list_sample2))
        print("H0: Md=0")
        print("H1: Md<0")
        print("Variable    Sample size" + "     Mean" + "     SD" + "     Variance" + "     SE Mean")
        print(
            "Group(x-y):     " + str(n) + "         " + str("%.2f" % Mean) + "     " + str("%.2f" % SD) + "     " + str(
                "%.2f" % Variance) + "        " + str("%.2f" % sem(list_sample2)))
        print("\nT value:" + str("%.2f" % T))
        print("Degree of freedom:" + str(o))
        print("Significance level:" + str(a))
        print("t(" + str(o) + "," + str(a) + ")=" + str(t))
        print("\n")
        if T < -t:
            print("for T(" + str("%.2f" % T) + ")" + "<" + "-t(" + str(-t) + ")")
            print("H0(Md=0)rejected\nH1(Md<0)accepted")
        else:
            print("for T(" + str("%.2f" % T) + ")" + "<" + "-t(" + str(-t) + ")")
            print("H1(Md<0)rejected\nH0(Md=0)accepted")
    elif alt_hypothesis == 3:
        clear()
        print("Group(x-y):" + str(list_sample2))
        print("H0: Md=0")
        print("H1: Md>0")
        print("Variable    Sample size" + "     Mean" + "     SD" + "     Variance" + "     SE Mean")
        print(
            "Group(x-y):     " + str(n) + "         " + str("%.2f" % Mean) + "     " + str("%.2f" % SD) + "     " + str(
                "%.2f" % Variance) + "        " + str("%.2f" % sem(list_sample2)))
        print("\nT value:" + str("%.2f" % T))
        print("Degree of freedom:" + str(o))
        print("Significance level:" + str(a))
        print("t(" + str(o) + "," + str(a) + ")=" + str(t))
        print("\n")
        if T > t:
            print("for T(" + str("%.2f" % T) + ")" + ">" + "t(" + str(t) + ")")
            print("H0(Md=0)rejected" + "\nH1(Md>0)accepted")
        else:
            print("for T(" + str("%.2f" % T) + ")" + ">" + "t(" + str(t) + ")")
            print("H1(Md>0)rejected\nH0(Md=0)accepted")
    else:
        clear()
        print("Please choose again")


