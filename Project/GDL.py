from random import choice, randint

def generate_language(char_min, char_max, char_rep):
    with open("list_adjs.txt", "r") as file_adjs, open("algo.adj.txt", "w") as result:
        fr_add_L = ""
        new_L = ""
        unique_words = set()
        word = ""
        word_t = ""
        num_char = 0

        for line in file_adjs:
            word = line.strip()
            num_char = randint(char_min, char_max)
            
            letter = ["a","b","c","d","e","é","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
            consonne = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","z"]
            voyelle = ["a","e","é","i","o","u","y"]
            while True:
                word_t = ""
                fr_add_L = ""
                fr_add_L2 = ""
                for _ in range(num_char):
                    while True:
                        new_L = choice(letter)
                        if new_L in consonne and fr_add_L in consonne and fr_add_L2 in consonne:
                            new_L = choice(voyelle)
                        if new_L in voyelle and fr_add_L in voyelle and fr_add_L2 in voyelle:
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
    

    with open("list_nouns.txt", "r") as file_noms, open("algo.nom.txt", "w") as result:
        fr_add_L = ""
        new_L = ""
        word = ""
        word_t = ""
        num_char = 0

        for line in file_noms:
            word = line.strip()
            num_char = randint(char_min, char_max)
            
            

            while True:
                word_t = ""
                fr_add_L = ""
                fr_add_L2 = ""
                for _ in range(num_char):
                    while True:
                        new_L = choice(letter)
                        if new_L in consonne and fr_add_L in consonne and fr_add_L2 in consonne:
                            new_L = choice(voyelle)
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


    with open("list_vbs.txt", "r") as file_vbs, open("algo.vbs.txt", "w") as result:
        fr_add_L = ""
        new_L = ""
        word = ""
        word_t = ""
        num_char = 0

        for line in file_vbs:
            word = line.strip()
            num_char = randint(char_min, char_max)
            
            
            
            while True:
                word_t = ""
                fr_add_L = ""
                fr_add_L2 = ""
                for _ in range(num_char):
                    while True:
                        new_L = choice(letter)
                        if new_L in consonne and fr_add_L in consonne and fr_add_L2 in consonne:
                            new_L = choice(voyelle)
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
