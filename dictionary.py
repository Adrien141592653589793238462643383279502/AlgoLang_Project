
list_words = open("algo_words_final.txt", "r")

while True:
    word = input("Quel mot cherchez-vous? Ecrivez stop pour arrêter le programme \n")
    for line in list_words:
        word_s = line.strip()
        if word in word_s:
            print(word_s)
            break
        else:
            print("Le mot n'est pas dans la liste")
    if word == "stop":
        break