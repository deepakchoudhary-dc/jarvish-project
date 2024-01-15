from tkinter import *
from time import strftime

root = Tk()
root.title('Clock')
root.geometry("300x300")
root.configure(bg="black")
root.resizable(False, False)

def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)

def lighting_effect():
    lbl.config(foreground="red")
    lbl.after(500, lambda: lbl.config(foreground="white"))
    lbl.after(1000, lighting_effect)

lbl = Label(root, font=('calibri', 40, 'bold'),
            background='black',
            foreground='white')
lbl.pack(expand=True)

time()
lighting_effect()

root.mainloop()



