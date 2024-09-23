from tkinter import *
from LangMake import generate_language, mix

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

char_rep_choice = StringVar()
char_rep_choice.set(None)

question3_label = Label(questions_frame, text="Allow repetition of same letters?", bg="#f3f4f6", fg="#333333", font=("Consolas", 12)).grid(sticky="w", pady=(10, 0), padx=(10))
radio11 = Radiobutton(questions_frame, text="Yes", variable=char_rep_choice, value="yes", bg="#f3f4f6").grid(sticky="w", padx=10)
radio12 = Radiobutton(questions_frame, text="No", variable=char_rep_choice, value="no", bg="#f3f4f6").grid(sticky="w", padx=10)

cons_rep_choice = StringVar()
cons_rep_choice.set(None)

question4_label = Label(questions_frame, text="Allow repetition of more than 2 consonants?", bg="#f3f4f6", fg="#333333", font=("Consolas", 12)).grid(sticky="w", pady=(20, 0), padx=10)
radio11 = Radiobutton(questions_frame, text="Yes", variable=cons_rep_choice, value="yes", bg="#f3f4f6", fg="#333333", font=("Consolas", 10)).grid(sticky="w", padx=10)
radio12 = Radiobutton(questions_frame, text="No", variable=cons_rep_choice, value="no", bg="#f3f4f6", fg="#333333", font=("Consolas", 10)).grid(sticky="w", padx=10)

vow_rep_choice = StringVar()
vow_rep_choice.set(None)

question5_label = Label(questions_frame, text="Allow repetition of more than 2 vowels?", bg="#f3f4f6", fg="#333333", font=("Consolas", 12))
question5_label.grid(sticky="w", pady=(20, 0), padx=10)

radio11 = Radiobutton(questions_frame, text="Yes", variable=vow_rep_choice, value="yes", bg="#f3f4f6", fg="#333333", font=("Consolas", 10))
radio11.grid(sticky="w", padx=10)

radio12 = Radiobutton(questions_frame, text="No", variable=vow_rep_choice, value="no", bg="#f3f4f6", fg="#333333", font=("Consolas", 10))
radio12.grid(sticky="w", padx=10)

def get_answers():
    try:
        min_answer = custom_min.get() if min_choice.get() == "Other" else min_choice.get()
        max_answer = custom_max.get() if max_choice.get() == "Other" else max_choice.get()
        char_rep = char_rep_choice.get()
        cons_rep = cons_rep_choice.get()
        vow_rep = vow_rep_choice.get()

        if not min_answer or not max_answer:
            raise ValueError

        min_answer = int(min_answer)
        max_answer = int(max_answer)

        if min_answer < 1 or max_answer < 1 or max_answer < min_answer:
            raise ValueError
        
        mix()
        generate_language(min_answer, max_answer, char_rep, cons_rep, vow_rep)
        
        window.destroy()

        success_window = Tk()
        success_window.geometry("320x150")
        success_window.title("Success")
        success_window['bg'] = '#f3f4f6'
        Label(success_window, text="Language successfully generated!", font=("Consolas", 12), bg="#f3f4f6", fg="#333333").pack(pady=30)
        Button(success_window, text="OK", command=success_window.destroy, bg="#e0e0e0", fg="#333333").pack(pady=10)

    except ValueError:
        
        error_window = Tk()
        error_window.geometry("400x200")
        error_window.title("Error")
        error_window['bg'] = '#f3f4f6'
        
        Label(error_window, text="Invalid input:", font=("Consolas", 12), bg="#f3f4f6", fg="#333333").pack(pady=10)
        
        if max_answer and min_answer and int(max_answer) < int(min_answer):
            Label(error_window, text="Maximum characters cannot be", font=("Consolas", 12), bg="#f3f4f6", fg="#333333").pack()
            Label(error_window, text="less than minimum characters.", font=("Consolas", 12), bg="#f3f4f6", fg="#333333").pack()
        
        else:
            Label(error_window, text="Number of characters should be positive integers.", font=("Consolas", 12), bg="#f3f4f6", fg="#333333").pack()

        Button(error_window, text="OK", command=error_window.destroy, bg="#e0e0e0", fg="#333333").pack(pady=10)
        error_window.mainloop()

submit_button = Button(window, text="Submit", command=get_answers, bg="#e0e0e0", fg="#333333", font=("Consolas", 12))
submit_button.pack(pady=20)

window.mainloop()
