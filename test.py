import keyboard
try:
    import telegram
    from telegram import *
except ModuleNotFoundError:
    os.system('pip install python-telegram-bot --upgrade')
import asyncio

import os
try:
    import matplotlib.pyplot as plt
except ModuleNotFoundError:
    os.system('pip install matplotlib')
try:
    import pandas as pd
except ModuleNotFoundError:
    os.system('pip install pandas')
try:
    import openpyxl
    from openpyxl import *
except ModuleNotFoundError:
    os.system('pip install openpyxl')
import datetime
from datetime import *
import time

loc = "D:\\Seshrut\\Error-505!!\\Tests\\"

if loc == "":
    loc = str(input("enter the file location where you want to save the result \n"))

Y = "."
A = str(input("Test number ->  "))
wb = openpyxl.Workbook()
test = wb.active
test.title ="test"
test["A1"].value = "No."
test["B1"].value = "Ques"
test["C1"].value = "Hour"
test["D1"].value = "Min"
test["E1"].value = "sec"
test["F1"].value = "time"

X = 0
d = 0
S = 0
H = 0
M = 0

X = datetime.now()
d = int(X.strftime("%d"))
S = int(X.strftime("%S"))
H = int(X.strftime("%H"))
M = int(X.strftime("%M"))

test["H2"].value = "Start"
test["I2"].value = H
test["J2"].value = M
test["K2"].value = S

Q = 0
l = 0
correct = 0
incorrect = 0
unattempted = 0
t_correct = 0
t_incorrect = 0
t_unattempted = 0

total_time_lapsed = 0
os.mkdir("D:\\Seshrut\\Error-505!!\\Tests\\"+"test"+A) # to be modified
time.sleep(1)
while Y != "end":
    X = datetime.now()
    d = int(X.strftime("%d"))
    S = int(X.strftime("%S"))
    H = int(X.strftime("%H"))
    M = int(X.strftime("%M"))

    start_time = time.time()
    if l == 0:
        print("+ - 0 \n")
    Y = str(keyboard.read_key())
    Q = Q + 1
    if Y != "":
        
        X = datetime.now()
        d = int(X.strftime("%d"))
        S = int(X.strftime("%S"))
        H = int(X.strftime("%H"))
        M = int(X.strftime("%M"))

        end_time = time.time()
        time_lapsed = round(end_time - start_time)
        if Y == "insert":
            break
        if Y == "+":
            print(Y)
            Y = 1
            correct = correct + 1
            t_correct = t_correct + time_lapsed
            l = 0

        if Y == "-":
            print(Y)
            Y = -1
            incorrect = incorrect + 1
            t_incorrect = t_incorrect + time_lapsed
            l = 0
        if Y == "0":
            print(Y)
            Y = 0
            unattempted = unattempted + 1
            t_unattempted = t_unattempted + time_lapsed
            l = 0
        if Y != "+" and Y != "-" and Y != "0" and Y != 1 and Y != -1 and Y != 0:
            time.sleep(0.3)
            l = 1
            continue


    test.append([Q,Y, H, M, S, time_lapsed])
    total_time_lapsed = time_lapsed + total_time_lapsed
    wb.save("D:\\Seshrut\\Error-505!!\\Tests\\"+"test"+A+"\\"+"test"+A+".xlsx") # to be modified
    time.sleep(0.3)
t_total = t_correct + t_incorrect + t_unattempted
# Calculate percentages
percent_correct = (correct / (Q-1) ) * 100
percent_incorrect = (incorrect / (Q-1)) * 100
percent_unattempted = (unattempted/ (Q-1)) * 100

percent_t_correct = (t_correct/t_total) * 100
percent_t_incorrect = (t_incorrect/t_total) * 100
percent_t_unattemted = (t_unattempted/t_total) * 100
# Define pie chart labels and colors
label = ["Correct", "Incorrect", "Unattempted"]
color = ["green", "red", "yellow"]

label_1 = ["Correct","Incorrect","Unattempted"]
color_1 = ["green","red","yellow"]
# Create the pie chart
plt.figure(figsize=(8, 8))
plt.pie([percent_correct, percent_incorrect, percent_unattempted], labels=label, autopct="%1.1f%%", startangle=90, colors=color)
plt.title("Test Results Analysis")
plt.axis("equal")  # Equal aspect ratio ensures a circular pie chart
plt.savefig("D:\\Seshrut\\Error-505!!\\Tests\\"+"test"+A+"\\"+"test result"+A+".png") # to be modified

plt.figure(figsize=(8, 8))
plt.pie([percent_t_correct, percent_t_incorrect, percent_t_unattemted], labels=label_1, autopct="%1.1f%%", startangle=90, colors=color_1)
plt.title("Test Time Analysis")
plt.axis("equal")  # Equal aspect ratio ensures a circular pie chart
plt.savefig("D:\\Seshrut\\Error-505!!\\Tests\\"+"test"+A+"\\"+"test time"+A+".png") # to be modified

test["H3"].value = "End"
test["I3"].value = H
test["J3"].value = M
test["K3"].value = S
test["L2"].value = A
wb.save("D:\\Seshrut\\Error-505!!\\Tests\\"+"test"+A+"\\"+"test"+A+".xlsx") # to be modified
os.startfile("D:\\Seshrut\\Error-505!!\\Tests\\"+"test"+A) # to be modified