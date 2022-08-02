from functions import *

import sys
import os

def clear():
    clear = lambda: os.system('cls')
    clear()

clear()
def mainMenu():
    print("\n           ****** WELCOME TO MY PROJECT ******         \n\n")
    print("         ***** GLOBAL SMART IT CONVERGENCE *****         \n\n\n\n\n")
    print("COURSE: DATA ANALYSIS ")
    print("STUDENTS: SATTOROV SAMARIDDIN")
    input()
    return 0
mainMenu()

clear()
def menu():
    print("                  ************MAIN MENU**************")
    #time.sleep(1)
    print()

    choice = input("""
                      A: Basic Descriptive Statistics
                      B: Histogram
                      C: Boxplot
                      D: Percentile
                      F: One Sample T-test
                      G: Two Sample T-test
                      H: Paired T-test
                      E: Quit

                      Please enter your choice: """)

    if choice == "A" or choice =="a":
        clear()
        Bd()
        print("\n")
        print("1.Again")
        print("2.Main menu")
        print("3.Quit")
        chose = int(input("Enter:"))
        if chose == 1:
            clear()
            Bd()
            input()
            clear()
            menu()
        elif chose == 2:
            clear()
            menu()
        else:
            sys.exit()

    elif choice == "B" or choice =="b":
        clear()
        Hg()
        print("\n")
        print("1.Again")
        print("2.Main menu")
        print("3.Quit")
        chose = int(input("Enter:"))
        if chose == 1:
            clear()
            Hg()
            clear()
            menu()
        elif chose == 2:
            clear()
            menu()
        else:
            sys.exit()

    elif choice == "C" or choice =="c":
        clear()
        Bp()
        print("\n")
        print("1.Again")
        print("2.Main menu")
        print("3.Quit")
        chose = int(input("Enter:"))
        if chose == 1:
            clear()
            Bp()
            clear()
            menu()
        elif chose == 2:
            clear()
            menu()
        else:
            sys.exit()
    elif choice == "D" or choice =="d":
        clear()
        Pk()
        print("\n")
        print("1.Again")
        print("2.Main menu")
        print("3.Quit")
        chose = int(input("Enter:"))
        if chose == 1:
            clear()
            Pk()
            clear()
            menu()
        elif chose == 2:
            clear()
            menu()
        else:
            sys.exit()
    elif choice == "F" or choice =="f":
        clear()
        OneT()
        print("\n")
        print("1.Again")
        print("2.Main menu")
        print("3.Quit")
        chose = int(input("Enter:"))
        if chose == 1:
            clear()
            OneT()
            clear()
            menu()
        elif chose == 2:
            clear()
            menu()
        else:
            sys.exit()
    elif choice == "G" or choice =="g":
        clear()
        TwoT()
        print("\n")
        print("1.Again")
        print("2.Main menu")
        print("3.Quit")
        chose = int(input("Enter:"))
        if chose == 1:
            clear()
            TwoT()
            clear()
            menu()
        elif chose == 2:
            clear()
            menu()
        else:
            sys.exit()
    elif choice == "H" or choice =="h":
        clear()
        PairedT()
        print("\n")
        print("1.Again")
        print("2.Main menu")
        print("3.Quit")
        chose = int(input("Enter:"))
        if chose == 1:
            clear()
            PairedT()
            clear()
            menu()
        elif chose == 2:
            clear()
            menu()
        else:
            sys.exit()
    elif choice=="E" or choice=="e":
        sys.exit
    else:
        clear()
        print("You must only select either A,B or C.")
        print("Please try again")
        menu()
menu()