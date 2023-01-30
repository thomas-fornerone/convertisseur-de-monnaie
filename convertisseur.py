from tkinter import *

USD = 1.08767 #Dollar américain 
JPY = 141.2555 #Le yen japonais
GBP = 0.88288 #Livre sterling

def convert1():
    euro1 = float(entryEUR1.get())
    dollar = USD*euro1
    entryDOLLAR.delete(0, END)
    entryDOLLAR.insert(0, dollar)

def convert2():
    euro2 = float(entryEUR2.get())
    yen = JPY*euro2
    entryYEN.delete(0, END)
    entryYEN.insert(0, yen)

def convert3():
    euro3 = float(entryEUR3.get())
    livres = GBP*euro3
    entryLIVRE.delete(0, END)
    entryLIVRE.insert(0, livres)

fen = Tk()
fen.geometry("600x600")

labelBvn = Label(fen, text = "Bonjour, bienvenue sur notre convertisseur")
labelBvn.place( x = 200, y = 50)


#Conversions euros/dollars
labelC1 = Label(fen, text = "Conversions euros/dollars")
labelC1.place( x = 50, y = 100)
euroC1 = Label(fen, text = "Euros :")
euroC1.place( x = 50, y = 130)
entryEUR1 = Entry(fen)
entryEUR1.place(x = 100, y = 130)
Convert = Button(fen, text = "Valider la conversion", command = convert1)
Convert.place(x = 70, y = 160)
dollarC1 = Label(fen, text = "Dollars :")
dollarC1.place( x = 50, y = 200)
entryDOLLAR = Entry(fen)
entryDOLLAR.place(x = 100, y = 200)

#Conversions euros/yens
labelC2 = Label(fen, text = "Conversions euros/yens")
labelC2.place( x = 50, y = 250)
euroC2 = Label(fen, text = "Euros :")
euroC2.place( x = 50, y = 280)
entryEUR2 = Entry(fen)
entryEUR2.place(x = 100, y = 280)
Convert2 = Button(fen, text = "Valider la conversion", command = convert2)
Convert2.place(x = 70, y = 310)
yenC2 = Label(fen, text = "Yens :")
yenC2.place( x = 50, y = 350)
entryYEN = Entry(fen)
entryYEN.place(x = 100, y = 350)

#Conversions euros/livres sterling
labelC3 = Label(fen, text = "Conversions euros/livres sterling")
labelC3.place( x = 50, y = 400)
euroC3 = Label(fen, text = "Euros :")
euroC3.place( x = 50, y = 430)
entryEUR3 = Entry(fen)
entryEUR3.place(x = 100, y = 430)
Convert3 = Button(fen, text = "Valider la conversion", command = convert3)
Convert3.place(x = 70, y = 460)
livreC3 = Label(fen, text = "Livres sterling :")
livreC3.place( x = 50, y = 500)
entryLIVRE = Entry(fen)
entryLIVRE.place(x = 140, y = 500)


fen.mainloop()