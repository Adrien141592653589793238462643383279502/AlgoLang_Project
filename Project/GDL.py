from random import choice, randint, shuffle



def melanger():
    with open("liste_mots.txt", "r") as file_mots1, open("algo.mots_melange.txt", "w") as result:
        liste_mot = []
        word= ""
        for line in file_mots1:
            word = line.strip()
            liste_mot += word
        shuffle(liste_mot)

        for mot in liste_mot:
            result.write(mot + "\n")




def generate_language(char_min, char_max, char_rep, cons_rep, voy_rep):
    with open("liste_mots.txt", "r") as file_mots, open("algo.mots.txt", "w") as result:
    
        unique_words = set()
        word = ""
        word_t = ""
        num_char = 0

        for line in file_mots:
            word = line.strip()
            num_char = randint(char_min, char_max)
            
            letter = ["a","b","c","d","e","é","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
            consonne = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","z"]
            voyelle = ["a","e","é","i","o","u","y"]
            while True:
                word_t = ""
                fr_add_L = ""
                fr_add_L2 = ""
                if num_char == 1:
                    word_t = choice(letter)
                    if word_t in unique_words:
                        num_char += randint(char_min, char_max - 1)
                else:
                    for _ in range(num_char):
                        while True:
                            new_L = choice(letter)
                            if new_L in consonne and fr_add_L in consonne and fr_add_L2 in consonne and cons_rep == "no":
                                new_L = choice(voyelle)
                            if new_L in voyelle and fr_add_L in voyelle and fr_add_L2 in voyelle and voy_rep == "no":
                                new_L = choice(consonne)
                            elif char_rep == "no" and new_L == fr_add_L:
                                continue
                            else:
                                break

                        word_t += new_L
                        fr_add_L2 = fr_add_L
                        fr_add_L = new_L 

                if word_t not in unique_words:
                    unique_words.add(word_t)
                    break
            result.write(f"{word} : {word_t}\n")
