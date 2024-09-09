from random import * 

file_adjs = open("liste_adjs.txt", "r")
result = open("result.txt", "w")
char_min = int(input('Minimum number of characters : '))
char_max = int(input('Maximum number of characters : '))
char_rep = input("is the repetition of two letters authorised? yes/no : ")
fr_add_L = ""
new_L = ""
if char_rep == "yes": 
    char_rep = True
else : 
    char_rep = False
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
