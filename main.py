from tkinter import *

window=Tk()
window.minsize(width=500,height=500)
window.title("BMI CALCULATİON")
window.config(padx=20,pady=20)
window.config(bg="green")

lab=Label()
lab.config(text="kilonuzu giriniz :")
lab.config(font=("Arial",20,"bold"))
lab.pack()

entr=Entry()
entr.config(width=20)
entr.pack()

lab2=Label()
lab2.config(text="boyunuzu giriniz :")
lab2.config(font=("Arial",20,"bold"))
lab2.pack()

entr2=Entry()
entr2.config(width=20)
entr2.pack()
def hesaplama():

    weight=entr.get()
    kilo=float(weight)
    height=entr2.get()
    boy=float(height)
    hesap=(kilo)//(boy*boy)

    if hesap<18.5:
        mylab=Label()
        mylab.config(font=("Arial",25,"bold"))
        mylab.config(text=f"vücut kilo/ boy endeksiniz : {hesap} ,vücudunuz zayıf potansiyeldedir",fg="black")
        mylab.pack()
    elif 18.5<hesap<24.9:
        mylab=Label()
        mylab.config(font=("Arial",25,"bold"))
        mylab.config(text=f"vücut kilo/ boy endeksiniz : {hesap},vücudunuz ortalama potansiyeldedir",fg="yellow",bg="black")
        mylab.pack()
    else:
        mylab=Label()
        mylab.config(font=("Arial",25,"bold"))
        mylab.config(text=f"vücut kilo/ boy endeksiniz : {hesap},vücudunuz kilolu potansiyeldedir",fg="red")
        mylab.pack()
but=Button()
but.config(command=hesaplama)
but.config(text="hesapla")
but.pack(side="bottom")
window.mainloop()