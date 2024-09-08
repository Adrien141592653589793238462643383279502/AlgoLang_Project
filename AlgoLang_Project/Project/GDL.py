from random import * 

file_adjs = open("liste_adjs.txt", "r")
result = open("result.txt", "w")
char_min = int(input('Minimum number of characters : '))
char_max = int(input('Maximum number of characters : '))
unique_words = set()

word =""
word_t = ""
num_char = 0 

for line in file_adjs:
    word = line
    num_char = randint(char_min,char_max)
    print(num_char)
    
    i = 0
    letter = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    
    while True:
        word_t = ''.join(choice(letter) for _ in range(num_char))
        
        if word_t not in unique_words:
            unique_words.add(word_t)
            break
    
    word_t = word_t + "\n"
    result.write(word_t)
    word = ""
    word_t = ""

file_adjs.close()
result.close()