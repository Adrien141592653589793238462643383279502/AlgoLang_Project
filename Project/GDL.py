from random import choice, randint

def generate_language(char_min, char_max, char_rep):
    with open("liste_adjs.txt", "r") as file_adjs, open("algo.adj.txt", "w") as result:
        fr_add_L = ""
        new_L = ""
        unique_words = set()
        word = ""
        word_t = ""
        num_char = 0

        for line in file_adjs:
            word = line.strip()
            num_char = randint(char_min, char_max)
            
            letter = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
            
            while True:
                word_t = ""
                fr_add_L = ""

                for _ in range(num_char):
                    while True:
                        new_L = choice(letter)
                        
                        if char_rep == "no" and new_L == fr_add_L:
                            continue
                        else:
                            break

                    word_t += new_L
                    fr_add_L = new_L 

                if word_t not in unique_words:
                    unique_words.add(word_t)
                    break
            result.write(f"{word} : {word_t}\n")
