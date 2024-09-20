from random import choice, randint, shuffle

def mix():
    with open("list_words.txt", "r") as file_mots1, open("algo.mixed_words.txt", "w") as result:
        list_words = []
        word = ""
        for line in file_mots1:
            word = line.strip()
            list_words += word
        shuffle(list_words)

        for mot in list_words:
            result.write(mot + "\n")

def generate_language(char_min, char_max, cons_rep, voy_rep):
    with open("list_words.txt", "r") as file_mots, open("algo.words.txt", "w") as result:
    
        unique_words = set()
        word = ""
        word_t = ""
        num_char = 0

        for line in file_mots:
            word = line.strip()
            num_char = randint(char_min, char_max)
            
            letter = ["a","b","c","d","e","é","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
            consonant = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","z"]
            vowel = ["a","e","é","i","o","u","y"]

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
                            if new_L in consonant and fr_add_L in consonant and fr_add_L2 in consonant and cons_rep == "no":
                                new_L = choice(vowel)
                            if new_L in vowel and fr_add_L in vowel and fr_add_L2 in vowel and voy_rep == "no":
                                new_L = choice(consonant)
                            else:
                                break

                        word_t += new_L
                        fr_add_L2 = fr_add_L
                        fr_add_L = new_L 

                if word_t not in unique_words:
                    unique_words.add(word_t)
                    break
            result.write(f"{word} : {word_t}\n")
