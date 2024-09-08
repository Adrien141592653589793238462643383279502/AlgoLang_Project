from random import * 

file_adjs = open("liste_adjs.txt", "r")
result = open("resultat.txt", "w")
car_max = int(input('nombre maximum de caractere'))
car_min = int(input('nombre minimum de caractere'))
mot =""
mot_t = ""
nombre_car = 0 
n_lettre = 0


for ligne in file_adjs:
    mot = ligne
    nombre_car = randint(car_min,car_max)
    print(nombre_car)
    for lettre in range(nombre_car): 

        n_lettre = randint(1,26)
        if n_lettre == 1:
            mot_t = mot_t + "a"
        if n_lettre == 2:
            mot_t = mot_t + "b"

        if n_lettre == 3:
            mot_t = mot_t + "c"

        if n_lettre == 4:
            mot_t = mot_t + "d"

        if n_lettre == 5:
            mot_t = mot_t + "e"

        if n_lettre == 6:
            mot_t = mot_t + "f"

        if n_lettre == 7:
            mot_t = mot_t + "g"

        if n_lettre == 8:
            mot_t = mot_t + "h"

        if n_lettre == 9:
            mot_t = mot_t + "i"

        if n_lettre == 10:
            mot_t + mot_t + "j"

        if n_lettre == 11:
            mot_t + mot_t + "k"

        if n_lettre == 12:
            mot_t = mot_t + "l"

        if n_lettre == 13:
            mot_t = mot_t + "m"

        if n_lettre == 14: 
            mot_t = mot_t + "n"

        if n_lettre == 15:
            mot_t = mot_t + "o"

        if n_lettre == 16:
            mot_t = mot_t + "p"

        if n_lettre == 17:
            mot_t = mot_t + "q"

        if n_lettre == 18:
            mot_t = mot_t + "r"

        if n_lettre == 19:
            mot_t = mot_t + "s"

        if n_lettre == 20:
            mot_t = mot_t + "t"

        if n_lettre == 21:
            mot_t = mot_t + "u"

        if n_lettre == 22:
            mot_t = mot_t + "v"

        if n_lettre == 23:
            mot_t = mot_t + "w"

        if n_lettre == 24: 
            mot_t = mot_t + "x"

        if n_lettre == 25:
            mot_t = mot_t + "y"

        if n_lettre == 26:
            mot_t = mot_t + "z"
    mot_t = mot_t + "\n"
    result.write(mot_t)
    mot = ""
    mot_t = ""


    
    
file_adjs.close()
result.close()

