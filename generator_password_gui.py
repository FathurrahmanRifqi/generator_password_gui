import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter.ttk import Combobox
import random


#default (sticky tidak diatur) maka pada posisi tengah (center)
# n menempel posisi utara (north ‐ atas)
# s menempel posisi selatan (south ‐ bawah)
# w menempel posisi barat (west ‐ kiri)
# e menempel posisi timur (east ‐kanan)
# ne menempel posisi utara‐timur (kanan‐atas)
# nw menempel posisi utara‐barat (kiri‐atas)
# se menempel posisi selatan‐timur (kanan‐bawah)
# sw menempel posisi selatan‐barat (kiri‐bawah)

# Buat objek
root = Tk()



def MoneyValidation(S):
    if S in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        return True
    root.bell() # .bell() plays that ding sound telling you there was invalid input
    return False

def gen():
    global sc1
    sc1.set("")
    passw=""

    if (entryLength.get() == "" ):
        messagebox.showwarning(title="Peringatan !", message="Harap masukan field terlebih dahulu !",)
    elif (int(entryLength.get()) < 1):
        messagebox.showwarning(title="Peringatan !", message="Panjang password harus lebih dari 0 !", )
    else :
        length = int(entryLength.get())
        lowercase='abcdefghijklmnopqrstuvwxyz'
        uppercase='ABCDEFGHIJKLMNOPQRSTUVWXYZ'+lowercase
        mixs='0123456789'+lowercase+uppercase+'@#$%&*'

        if entryStrength.get()=='Low':
            for i in range(0,length):
                passw=passw+random.choice(lowercase)
            sc1.set(passw)
        elif entryStrength.get()=='Medium':
            for i in range(0,length):
                passw=passw+random.choice(uppercase)
            sc1.set(passw)
        elif entryStrength .get()=='High':
            for i in range(0,length):
                passw=passw+random.choice(mixs)
            sc1.set(passw)

        text_area.configure(state='normal')
        text_area.delete('0.0', tk.END)
        text_area.insert('1.0', sc1.get())
        text_area.configure(state='disabled')

sc1=StringVar('')


# Atur window
lebar = 390
tinggi = 350
setTengahX = (root.winfo_screenwidth() - lebar) // 2
setTengahY = (root.winfo_screenheight() - tinggi) // 2

root.geometry("%ix%i+%i+%i" % (lebar, tinggi, setTengahX, setTengahY))
root.resizable(False, False)
root.wm_title("Generate Password GUI")




# Buat objek frame
frameSaya = Frame(root,width=300, height=200)
frameSaya.grid(row=0,column=0, padx=0, pady=0)
frameSaya.config(background = "#fff")

# Buat tabel pada grid 0,0
labelHeader = Label(frameSaya, text="Aplikasi Password Generator\n Oleh Fathurrahman Rifqi Azzami - 1918101504 - II RPLK",background="#fff")
labelHeader.grid(row=0, column=0, padx=45, pady=30)

frameDua =  Frame(root, width=300, height=300)
frameDua.grid(row=1, column=0, padx=10, pady=40)

labelLength =  Label(frameDua, text="Panjang Password")
labelLength.grid(row=0, column=0, padx=10, pady=5,sticky="w")

vcmd = (root.register(MoneyValidation), '%S')
entryLength =  ttk.Entry(frameDua, width=30)
entryLength.insert(0,"8")
entryLength.grid(row=0, column=1)

labelStrength =  Label(frameDua, text="Kekuatan Password")
labelStrength.grid(row=1, column=0, padx=10, pady=5,sticky="w")

entryStrength =  Combobox(frameDua,width=27, state="readonly")
entryStrength['values']=('Low','Medium','High')
entryStrength.current(1)
entryStrength.grid(row=1, column=1)


buttonSaya =  ttk.Button(frameDua, text="Generate Password", width=26, command=gen)
buttonSaya.grid(row=2, column=1, sticky="w", padx=0, pady=7, ipadx=10)

text_area = scrolledtext.ScrolledText(frameDua,wrap=tk.WORD,width=23,height=3,padx=7,pady=7,background="#f4f4f4",font=("Arial",10))

text_area.grid(row=3, column=1,pady=7)


root.mainloop()


