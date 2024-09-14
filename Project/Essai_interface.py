from tkinter import *
from random import * 


fenetre = Tk()
fenetre.geometry("600x400")
fenetre.title("Interface")
fenetre["bg"] = "red"
fenetre.resizable(height= True, width=True)


titre = Label(fenetre, text="AlgoLang, Générateur aléatoire de langues",font=("Times New Roman",50,"bold"), fg="black",bg="red" )
titre.pack()


#Choisir les nombres minimaux et maximaux de lettres

boite = Frame(fenetre)



def fonction():
    print(car_min.get())
    print(car_max.get())
    char_max = car_max.get()
    char_min = car_min.get()

car_min = IntVar()
car_max = IntVar()


text1 = Label(boite, text="Le nombre minimal de caractère est:")
text1.pack()
entree1 = Entry(boite, textvariable=car_min)
entree1.pack()


text2 = Label(boite, text="Le nombre maximal de caractère est:")
text2.pack()
entree2 = Entry(boite, textvariable=car_max)
entree2.pack()

bouton = Button(boite, text="Valider", command=fonction)
bouton.pack()

boite.pack(side=LEFT)



#Choisir si une lettre peut se répéter

boite2 = Frame(fenetre, height=50,width=30)
boite2
def fonction1():
    print(repet.get())
    char_rep = repet.get()

repet = StringVar()


text3 = Label(boite2, text="Répétitions de lettres? yes/no")
text3.pack()
entree3 = Entry(boite2, textvariable=repet)
entree3.pack()


bouton1 = Button(boite2, text="Valider", command=fonction1)
bouton1.pack()

boite2.pack(side=RIGHT)


#Valider tout et fermer l'interface

bouton2 = Button(fenetre, text="Valider Tout", command=fenetre.destroy)
bouton2.pack()

fenetre.mainloop()




    

file_adjs = open("liste_adjs.txt", "r")
result = open("result.txt", "w")

fr_add_L = ""
new_L = ""
unique_words = set()
word =""
word_t = ""
num_char = 0
char_repet= set()

if repet == "yes": 
    char_rep = True
else : 
    char_rep = False

for line in file_adjs:
    
    word = line
    num_char = randint(car_min.get(),car_max.get())
    print(num_char)
    
    
    letter = ["a","b","c","d","e","é","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    
    while True:
        for _ in range (num_char):
            while True : 
                new_L = choice(letter)
                if new_L != fr_add_L and char_rep == False :
                    fr_add_L = new_L
                    word_t = word_t + new_L
                    break
                if char_rep == True :
                    word_t = word_t + new_L
                    break
            new_L = ""    

        if word_t not in unique_words:
            unique_words.add(word_t)
            break
    
    word_t = word_t + "\n"
    result.write(word + "|===>" + word_t)
    word = ""
    word_t = ""

file_adjs.close()
result.close()
