from tkinter import *
import time
import psutil

root = Tk()
canvas1 = Canvas(root)
canvas1.pack()


curtemp = ''

temp_o = psutil.sensors_temperatures()
temp = temp_o['cpu_thermal']
temp = str(temp)

curtime = str(time.strftime('%H')) + ':' + str(time.strftime('%M')) + ':' + str(time.strftime('%S'))

for a in range(27, 32):
    curtemp += str(temp[a])

print(curtemp, curtime)

root.mainloop()