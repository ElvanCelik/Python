import tkinter as tk
import random as rd

form=tk.Tk()
form.title("Tekrar Uygulaması")
form.geometry("500x250+500+300")
#random sayı üretip listeye atıyor
liste = []
for i in range(5):
    while (len(liste)) != 5:
        a=rd.randint(1,50)
        if a not in liste:
            liste.append(a)
def gostermek():  #listeyi yazdıran kod
    label.config(text= liste , bg="green")
label= tk.Label(form ,fg="white", bg="blue")
label.pack()

def saydamlik():
    form.wm_attributes("-alpha" , 0.4)
def normal():
    form.wm_attributes("-alpha", 1.0)

def pencereBoyutuNormal():
    form.state('normal')
def pencereBoyutuFull():
    form.state('zoomed')
def pencereBoyutuIcon():
    form.state('iconic')


goster= tk.Button(form,text="Göster", fg="light pink", bg="black", command=gostermek)
goster.pack(side=tk.LEFT)



saydam=tk.Button(form,text="Saydamlaştır",fg="light pink",bg="black",command=saydamlik)
saydam.pack(side=tk.LEFT)
opak=tk.Button(form,text="Opak yap",fg="light pink",bg="black",command=normal)
opak.pack(side=tk.LEFT)


boyutn=tk.Button(form,text="normal boyut",fg="light pink",bg="black",command=pencereBoyutuNormal)
boyutn.pack(side=tk.LEFT)
boyutz=tk.Button(form,text="tam ekran",fg="light pink",bg="black",command=pencereBoyutuFull)
boyutz.pack(side=tk.LEFT)
boyuti=tk.Button(form,text="ikon",fg="light pink",bg="black",command=pencereBoyutuIcon)
boyuti.pack(side=tk.LEFT)


form.mainloop()


