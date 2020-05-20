import tkinter as tk
from tkinter import ttk
import datetime
import calendar

class simpleCalender:
    def __init__(self, master):
        #label
        ttk.Label(master, text = 'When were you born?').grid(row=0,column=0,padx=15,pady=15)
        #label
        ttk.Label(master, text = 'Select Year').grid(row=1,column=0,padx=5,pady=5)
        #string var
        self.year = tk.StringVar()
        #year dropdown
        self.spinbxyear = tk.Spinbox(master, from_ = 1920, 
                                 to = datetime.datetime.now().year,
                                 textvariable = self.year)
        self.spinbxyear.grid(row=2,column=0,padx=15,pady=15)
        #label
        ttk.Label(master, text = 'Select Month').grid(row=3,column=0,padx=15,pady=15)
        #string var
        self.month = tk.StringVar()
        self.combobox = ttk.Combobox(master, textvariable = self.month) # textvar = combobox value
        self.combobox.grid(row=4,column=0,padx=5,pady=5)
        
        # possible combox values
        self.combobox.config(values = ('January', 'February', 'March', 'April',
                                       'May', 'June', 'July', 'August', 'September',
                                       'October', 'November', 'December'))
        self.combobox.set('January')
        #label
        ttk.Label(master, text = 'Select Date').grid()
        self.dateofmonth = tk.StringVar()
        self.lastday = 31
        self.spinbxday = tk.Spinbox(master, from_ = 1, to = 31,
                                     textvariable = self.dateofmonth)
        self.spinbxday.grid(row=5,column=0,padx=15,pady=15)
        #button
        ttk.Button(master, text = "Get Date of Birth", command = self.getDOB).grid(row=6,column=0,padx=5,pady=5)
        #label
        self.displaydob = ttk.Label(master, text = "Please select a date")
        self.displaydob.grid(row=7,column=0,padx=15,pady=15)

    def getyear(self):
        "docstring for method getyear"
        if int(self.year.get()) in range(int(self.spinbxyear['from']), int(self.spinbxyear['to']+1)):
            return int(self.year.get())
        else:
            return -1
    
    def getmonth(self):
        "docstring for method getmonth()"
        if self.month.get() in self.combobox['values']:
            return self.month.get()
        else:
            return -1
        
    def getdate(self):
        "docstring for method getdate()"
        if int(self.dateofmonth.get()) in range(1, 32):
            return int(self.dateofmonth.get())
        else:
            return -1

    def getDOB(self):
        "docstring for method getDOB()"
        year = self.getyear()
        month = self.getmonth()
        
        if calendar.isleap(year) and month=='February':
            self.lastday =  29
        elif not calendar.isleap(year) and month=='February':
            self.lastday = 28
        elif month in ('January', 'March', 'May', 'July', 'August', 'October', 'December'):
            self.lastday = 31
        elif month in ('April', 'June', 'September', 'November'):
            self.lastday = 30
        else:
            self.lastday = -1
        
        if self.getdate() > self.lastday or self.getdate()<1 or self.lastday == -1:
            date = -1
        else:
            date = self.getdate()
        
        if year != -1 and month != -1 and date != -1:
            self.displaydob.config(text = f'{month} {date}, {year}')
        else:
            self.displaydob.config(text = "Date is not valid.")

def CalenderApp():
    root = tk.Tk()
    root.title("Calendar App")
    simpleCalender(root)
    tk.mainloop()

def main():
    CalenderApp()

if __name__ == '__main__':
    main()
