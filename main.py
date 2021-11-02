# importing all the modules
from tkinter import *
import time
import psutil
import csv
import file_seeker as fs

# global variables
count = 1
entry = int(fs.GetEntry())
refresh = int(fs.GetRefresh())*1000

# csv specifics
fields = ['Sr.No', 'Time', 'Temp']
blank = ['', '', '']
filename = 'logs.csv'
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerow(blank)

# tkinter specifics
root = Tk()
canvas1 = Canvas(root)
canvas1.pack()
label_temp = Label(canvas1, text = 'Current temprature')
label_temp.grid(row = 1, column = 1)
label_curtemp = Label(canvas1, text = '')
label_curtemp.grid(row = 2, column = 1)
label_time = Label(canvas1, text = 'Current time')
label_time.grid(row = 1, column = 2)
label_curtime = Label(canvas1, text = '')
label_curtime.grid(row = 2, column = 2)

def StartReading():
    global count
    
    # will print the current temprature of the cpu (raspberry pi4) along with time
    curtemp = ''
    temp_o = psutil.sensors_temperatures()
    temp = temp_o['cpu_thermal']
    temp = str(temp)
    curtime = str(time.strftime('%H')) + ':' + str(time.strftime('%M')) + ':' + str(time.strftime('%S'))
    for a in range(27, 32):
        curtemp += str(temp[a])
    label_curtemp.config(text = curtemp)
    label_curtime.config(text = curtime)
    rows = [count, curtime, curtemp]
    
    
    # csv writing
    with open(filename, 'a') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(rows)
    
    # loop control
    if count <= entry:
        count += 1
        root.after(refresh, StartReading)
    else:
        root.destroy()

StartReading()

# tkinter specifics
root.mainloop()