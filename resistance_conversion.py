import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
#twst
class Application(tk.Frame):
    def __init__(self, master=None):
        def x():

            a=self.Resistance_EditBox_1.get()
            b=int(a[-1])
            c=int(a[0:-1])
            d=c*10**b
            if d>1000000000:
               e=d/1000000000
               f=str(e)
               self.labelResult['text'] = f+"G"

            elif d>1000000:
                e=d/1000000000
                f=str(e)
                self.labelResult['text'] = f+"M"

            elif d>1000:
                e=d/1000
                f=str(e)
                self.labelResult['text'] = f+"K"

            else:
                labelResult['text'] = d

        self.labelBoard = tk.Label(win, text=u'Resistance display:')
        self.labelBoard.place(x=120,y=20)

        self.Resistance_EditBox_1 = tk.Entry(width=10)
        self.Resistance_EditBox_1.insert(tk.END, '0')
        self.Resistance_EditBox_1.place(x=120,y=40)

        self.labelResistance = tk.Label(win, text=u'Resistance values:')
        self.labelResistance.place(x=250,y=20)

        self.labelResult = tk.Label(win, text=u'---')
        self.labelResult.place(x=250,y=40)

        self.calcButton = tk.Button(win, text=u'check')
        self.calcButton["command"] = x
        self.calcButton.place(x=220,y=160)

win = tk.Tk()
win.title("Resistance conversion")
win.geometry("500x250")
win.resizable(0,0)
win.resizable(False, False)
app = Application(master=win)
def on_closing():
        try:
            app.Vol_Turn_Off()
            win.destroy()
        except :
          if messagebox.askokcancel("Quit", "Do you want to quit?"):
               win.destroy()

win.protocol("WM_DELETE_WINDOW",on_closing)

win.mainloop()