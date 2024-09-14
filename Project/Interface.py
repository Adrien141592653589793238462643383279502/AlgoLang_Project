from tkinter import *
from GDL import generate_language

window = Tk()
window.geometry("400x600")
window.title("Language Generator Interface")
window['bg'] = 'white'
window.resizable(height=False, width=False)

textZone = Label(window, text="AlgoLang Project", font=("Noto Mono Sans", 20, "bold"), fg="black", bg="white").pack()
title = Label(window, text="Random Languages Generator", font=("Noto Mono Sans", 15, "bold"), fg="black", bg="white").pack()

questions_frame = Frame(window, bg="white")
questions_frame.pack(pady=20)

min_choice = StringVar()
min_choice.set(None)

def toggle_custom_min():
    if min_choice.get() == "Other":
        custom_min.config(state=NORMAL)
    else:
        custom_min.delete(0, END)
        custom_min.config(state=DISABLED)

question1_label = Label(questions_frame, text="Minimum number of characters:", bg="white").grid(sticky="w")
radio1 = Radiobutton(questions_frame, text="1", variable=min_choice, value="1", bg="white", command=toggle_custom_min).grid(sticky="w")
radio2 = Radiobutton(questions_frame, text="2", variable=min_choice, value="2", bg="white", command=toggle_custom_min).grid(sticky="w")
radio3 = Radiobutton(questions_frame, text="3", variable=min_choice, value="3", bg="white", command=toggle_custom_min).grid(sticky="w")
radio4 = Radiobutton(questions_frame, text="5", variable=min_choice, value="5", bg="white", command=toggle_custom_min).grid(sticky="w")
radio5 = Radiobutton(questions_frame, text="Other (specify):", variable=min_choice, value="Other", bg="white", command=toggle_custom_min).grid(sticky="w")

custom_min = Entry(questions_frame, bg="white", state=DISABLED)
custom_min.grid(sticky="w")

max_choice = StringVar()
max_choice.set(None)

def toggle_custom_max():
    if max_choice.get() == "Other":
        custom_max.config(state=NORMAL)
    else:
        custom_max.delete(0, END)
        custom_max.config(state=DISABLED)

question2_label = Label(questions_frame, text="Maximum number of characters:", bg="white").grid(sticky="w", pady=(20, 0))
radio6 = Radiobutton(questions_frame, text="5", variable=max_choice, value="5", bg="white", command=toggle_custom_max).grid(sticky="w")
radio7 = Radiobutton(questions_frame, text="9", variable=max_choice, value="9", bg="white", command=toggle_custom_max).grid(sticky="w")
radio8 = Radiobutton(questions_frame, text="12", variable=max_choice, value="12", bg="white", command=toggle_custom_max).grid(sticky="w")
radio9 = Radiobutton(questions_frame, text="15", variable=max_choice, value="15", bg="white", command=toggle_custom_max).grid(sticky="w")
radio10 = Radiobutton(questions_frame, text="Other (specify):", variable=max_choice, value="Other", bg="white", command=toggle_custom_max).grid(sticky="w")

custom_max = Entry(questions_frame, bg="white", state=DISABLED)
custom_max.grid(sticky="w")

char_rep_choice = StringVar()
char_rep_choice.set(None)

question3_label = Label(questions_frame, text="Allow repetition of letters?", bg="white").grid(sticky="w", pady=(20, 0))
radio11 = Radiobutton(questions_frame, text="Yes", variable=char_rep_choice, value="yes", bg="white").grid(sticky="w")
radio12 = Radiobutton(questions_frame, text="No", variable=char_rep_choice, value="no", bg="white").grid(sticky="w")

def get_answers():
    min_answer = custom_min.get() if min_choice.get() == "Other" else min_choice.get()
    max_answer = custom_max.get() if max_choice.get() == "Other" else max_choice.get()
    char_rep = char_rep_choice.get()
    
    if not min_answer or not max_answer or not char_rep:
        return
    
    generate_language(int(min_answer), int(max_answer), char_rep)
    
    window.destroy()

    success_window = Tk()
    success_window.geometry("300x150")
    success_window.title("Success")
    Label(success_window, text="Language successfully generated!", font=("Arial", 14)).pack(pady=30)
    Button(success_window, text="OK", command=success_window.destroy).pack(pady=10)

submit_button = Button(window, text="Submit", command=get_answers, bg="white").pack(pady=20)

window.mainloop()
