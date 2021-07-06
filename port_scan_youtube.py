from tkinter import *
from threading import *
import socket




master = Tk()
master.title("PortScanner")
master.geometry("400x300+200+200")
master.resizable(False,False)


#--------------------------#
#--------------------------#
frame1 = Frame(master,bg="#556b2f")
frame1.place(relx=0,rely=0,relwidth=1.0,relheight=0.2)

l1 = Label(frame1,text="PortScanner - OlcaySoftware\nYouTube",bg="#556b2f",fg="white",font="Arial 12 bold")
l1.pack(padx=10,pady=10,anchor=S)

#--------------------------#
#--------------------------#
frame2 = Frame(master,bg="#556b2f")
frame2.place(relx=0,rely=0.21,relwidth=1.0,relheight=0.2)
l2 = Label(frame2,text="IP ADRESİ GİRİNİZ:",bg="#556b2f",fg="white",font="Arial 12 bold")
l2.pack(padx=5,pady=10,side=LEFT)
e1 = Entry(frame2,bd=3,relief=FLAT)
e1.pack(padx=5,pady=10,side=LEFT)


from tkinter import messagebox
def start():


    if e1.get():

        def islem():

            target = e1.get()
            soket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

            def scanner(port):

                try:

                    soket.connect((target,port))
                    return True
                except:
                    return False

            for portNumber in range(1,100):

                yazdir = "Port Taranıyor..{}".format(portNumber)
                l3["text"] = yazdir
                if scanner(portNumber):
                    bulundu = "** PORT {} /TCP AÇIKTIR".format(portNumber)
                    l3["text"] = bulundu

            scanner()
        t1 = Thread(target=islem)
        t1.start()

    else:

        hata = "LÜTFEN GEREKLİ ALANI DOLDURUN!"
        messagebox.showerror("BOŞ ALANLAR VAR",hata)
        




btn = Button(frame2,text="SCAN",bg="green",fg="white",font="Arial 10 bold",command=start)
btn.pack(padx=5,pady=10,side=LEFT)

#--------------------------#
#--------------------------#

frame3 = Frame(master,bg="#bdb76b")
frame3.place(relx=0,rely=0.42,relwidth=1.0,relheight=0.58)

l3 = Label(frame3,text="SONUÇLAR BURADA GÖRÜNÜR..",bg="#bdb76b",fg="white",font="Arial 15 bold")
l3.pack(pady=20,anchor=S)


#--------------------------#
#--------------------------#


master.mainloop()





