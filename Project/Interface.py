from tkinter import *
from LangMaker import generate_language

window = Tk()
window.geometry("500x800")
window.title("LangMake GUI")
window['bg'] = '#f3f4f6'
window.resizable(height=False, width=False)

textZone = Label(window, text="AlgoLang Project", font=("Consolas", 30, "bold"), fg="#333333", bg="#f3f4f6")
textZone.pack()

title = Label(window, text="Random Languages Generator", font=("Consolas", 20, "bold"), fg="#333333", bg="#f3f4f6")
title.pack()

questions_frame = Frame(window, bg="#f3f4f6")
questions_frame.pack(pady=20, padx=20)

min_choice = StringVar()
min_choice.set(None)

def toggle_custom_min():
    if min_choice.get() == "Other":
        custom_min.config(state=NORMAL)
    else:
        custom_min.delete(0, END)
        custom_min.config(state=DISABLED)

question1_label = Label(questions_frame, text="Minimum number of characters:", bg="#f3f4f6", fg="#333333", font=("Consolas", 12))
question1_label.grid(sticky="w", padx=10)

radio1 = Radiobutton(questions_frame, text="1", variable=min_choice, value="1", bg="#f3f4f6", fg="#333333", font=("Consolas", 10), command=toggle_custom_min)
radio1.grid(sticky="w", padx=10)

radio2 = Radiobutton(questions_frame, text="2", variable=min_choice, value="2", bg="#f3f4f6", fg="#333333", font=("Consolas", 10), command=toggle_custom_min)
radio2.grid(sticky="w", padx=10)

radio3 = Radiobutton(questions_frame, text="3", variable=min_choice, value="3", bg="#f3f4f6", fg="#333333", font=("Consolas", 10), command=toggle_custom_min)
radio3.grid(sticky="w", padx=10)

radio4 = Radiobutton(questions_frame, text="5", variable=min_choice, value="5", bg="#f3f4f6", fg="#333333", font=("Consolas", 10), command=toggle_custom_min)
radio4.grid(sticky="w", padx=10)

radio5 = Radiobutton(questions_frame, text="Other (specify):", variable=min_choice, value="Other", bg="#f3f4f6", fg="#333333", font=("Consolas", 10), command=toggle_custom_min)
radio5.grid(sticky="w", padx=10)

custom_min = Entry(questions_frame, bg="#ffffff", fg="#333333", font=("Consolas", 10), state=DISABLED)
custom_min.grid(sticky="w", padx=10)

max_choice = StringVar()
max_choice.set(None)

def toggle_custom_max():
    if max_choice.get() == "Other":
        custom_max.config(state=NORMAL)
    else:
        custom_max.delete(0, END)
        custom_max.config(state=DISABLED)

question2_label = Label(questions_frame, text="Maximum number of characters:", bg="#f3f4f6", fg="#333333", font=("Consolas", 12))
question2_label.grid(sticky="w", pady=(20, 0), padx=10)

radio6 = Radiobutton(questions_frame, text="7", variable=max_choice, value="7", bg="#f3f4f6", fg="#333333", font=("Consolas", 10), command=toggle_custom_max)
radio6.grid(sticky="w", padx=10)

radio7 = Radiobutton(questions_frame, text="9", variable=max_choice, value="9", bg="#f3f4f6", fg="#333333", font=("Consolas", 10), command=toggle_custom_max)
radio7.grid(sticky="w", padx=10)

radio8 = Radiobutton(questions_frame, text="12", variable=max_choice, value="12", bg="#f3f4f6", fg="#333333", font=("Consolas", 10), command=toggle_custom_max)
radio8.grid(sticky="w", padx=10)

radio9 = Radiobutton(questions_frame, text="15", variable=max_choice, value="15", bg="#f3f4f6", fg="#333333", font=("Consolas", 10), command=toggle_custom_max)
radio9.grid(sticky="w", padx=10)

radio10 = Radiobutton(questions_frame, text="Other (specify):", variable=max_choice, value="Other", bg="#f3f4f6", fg="#333333", font=("Consolas", 10), command=toggle_custom_max)
radio10.grid(sticky="w", padx=10)

custom_max = Entry(questions_frame, bg="#ffffff", fg="#333333", font=("Consolas", 10), state=DISABLED)
custom_max.grid(sticky="w", padx=10)

cons_rep_choice = StringVar()
cons_rep_choice.set(None)

question4_label = Label(questions_frame, text="Allow repetition of more than 2 consonants?", bg="#f3f4f6", fg="#333333", font=("Consolas", 12))
question4_label.grid(sticky="w", pady=(20, 0), padx=10)

radio11 = Radiobutton(questions_frame, text="Yes", variable=cons_rep_choice, value="yes", bg="#f3f4f6", fg="#333333", font=("Consolas", 10))
radio11.grid(sticky="w", padx=10)

radio12 = Radiobutton(questions_frame, text="No", variable=cons_rep_choice, value="no", bg="#f3f4f6", fg="#333333", font=("Consolas", 10))
radio12.grid(sticky="w", padx=10)

voy_rep_choice = StringVar()
voy_rep_choice.set(None)

question5_label = Label(questions_frame, text="Allow repetition of more than 2 vowels?", bg="#f3f4f6", fg="#333333", font=("Consolas", 12))
question5_label.grid(sticky="w", pady=(20, 0), padx=10)

radio11 = Radiobutton(questions_frame, text="Yes", variable=voy_rep_choice, value="yes", bg="#f3f4f6", fg="#333333", font=("Consolas", 10))
radio11.grid(sticky="w", padx=10)

radio12 = Radiobutton(questions_frame, text="No", variable=voy_rep_choice, value="no", bg="#f3f4f6", fg="#333333", font=("Consolas", 10))
radio12.grid(sticky="w", padx=10)

def get_answers():
    min_answer = custom_min.get() if min_choice.get() == "Other" else min_choice.get()
    max_answer = custom_max.get() if max_choice.get() == "Other" else max_choice.get()
    cons_rep = cons_rep_choice.get()
    voy_rep = voy_rep_choice.get()

    if not min_answer or not max_answer:
        return
    
    generate_language(int(min_answer), int(max_answer), cons_rep, voy_rep)
    
    window.destroy()

    success_window = Tk()
    success_window.geometry("320x150")
    success_window.title("Success")
    success_window['bg'] = '#f3f4f6'
    Label(success_window, text="Language successfully generated!", font=("Consolas", 12), bg="#f3f4f6", fg="#333333").pack(pady=30)
    Button(success_window, text="OK", command=success_window.destroy, bg="#e0e0e0", fg="#333333").pack(pady=10)

submit_button = Button(window, text="Submit", command=get_answers, bg="#e0e0e0", fg="#333333", font=("Consolas", 12))
submit_button.pack(pady=20)

window.mainloop()
