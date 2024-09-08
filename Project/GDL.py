from random import * 

file_adjs = open("liste_adjs.txt", "r")
result = open("resultat.txt", "w")
car_max = int(input('nombre maximum de caractere'))
car_min = int(input('nombre minimum de caractere'))
mot =""
mot_t = ""
nombre_car = 0 
n_lettre = 0
lettre = ["a","b,","c","d","e","f","h","i","j","k","l","m","n","o","p","q","r","s","t,","u","v","w","x","y","z"]

 
for ligne in file_adjs:
    mot = ligne
    nombre_car = randint(car_min,car_max)
    print(nombre_car)
    
    for lettre in range(nombre_car): 
        
        mot_t += randint(lettre)
        
    mot_t = mot_t + "\n"
    result.write(mot_t)
    mot = ""
    mot_t = ""


    
    
file_adjs.close()
result.close()

