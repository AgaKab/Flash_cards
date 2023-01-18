from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
random_word = None
y=0
english_word = ""
new_dict = {}
timer = None
# data_french_list = []
# data_english_list = []


def click():
    global random_word, y, english_word, timer, data_english_list, data_french_list

    try:
        data = pandas.read_csv('words_to_learn.csv')
        data_french_list = data["French"].to_list()
        data_english_list = data["English"].to_list()
        random_word = random.choice(data_french_list)
    except IndexError:
        data = pandas.read_csv('data/french_words.csv')
        data_french_list = data["French"].to_list()
        data_english_list = data["English"].to_list()
        random_word = random.choice(data_french_list)

    # random_word = random.choice(data_french_list)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=f"{random_word}", fill="black")
    canvas.itemconfig(canvas_image, image=card_front_img)
    for x in data_french_list:
        if x == random_word:
            y = data_french_list.index(x)
            # print(y)
    english_word = data_english_list[y]
    timer = window.after(3000, flip)


def click_yes():
    global random_word, y, english_word, new_dict, timer, data_english_list, data_french_list
    # window.after_cancel(timer)

    try:
        data = pandas.read_csv('words_to_learn.csv')
        data_french_list = data["French"].to_list()
        data_english_list = data["English"].to_list()
        random_word = random.choice(data_french_list)
    except IndexError:
        data = pandas.read_csv('data/french_words.csv')
        data_french_list = data["French"].to_list()
        data_english_list = data["English"].to_list()
        random_word = random.choice(data_french_list)

    # random_word = random.choice(data_french_list)
    window.after_cancel(timer)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=f"{random_word}", fill="black")
    canvas.itemconfig(canvas_image, image=card_front_img)
    for x in data_french_list:
        if x == random_word:
            y = data_french_list.index(x)
    english_word = data_english_list[y]

    timer = window.after(3000, flip)
    data_french_list.remove(random_word)
    data_english_list.remove(english_word)
    print(len(data_french_list))
    print(len(data_english_list))
    new_dict = {"French":data_french_list, "English":data_english_list}
    new_df = pandas.DataFrame(new_dict)
    new_df.to_csv("words_to_learn.csv", index=False)


def flip():
    global random_word, y, english_word, data_english_list, data_french_list
    english_word = data_english_list[y]
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=f"{english_word}", fill="white")
    # print(english_word)


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=20, bg=BACKGROUND_COLOR)

# window.after(3000, flip)

canvas = Canvas()
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)

card_back_img = PhotoImage(file="images/card_back.png")
# canvas.create_image(400, 263, image=card_back_img)

card_front_img = PhotoImage(file="images/card_front.png")
canvas_image = canvas.create_image(400, 263, image=card_front_img)
title_text = canvas.create_text(400, 150, text='', fill="black", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text='', fill="black", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=click_yes)
right_button.grid(row=1, column=1)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=click)
wrong_button.grid(row=1, column=0)


# data_to_learn = pandas.read_csv('words_to_learn.csv')
# new_data_french_list = data_to_learn["French"].to_list()
# new_data_english_list = data_to_learn["English"].to_list()
#
#
# data = pandas.read_csv('data/french_words.csv')
# data_french_list = data["French"].to_list()
# data_english_list = data["English"].to_list()
# # data_all_list = data_english_list + data_french_list
# # print(random.choice(data_all_list))

# data_dict = data.to_dict(orient="records")
# print(data_dict)
# print(random.choice(data_dict)["French"])


click()

window.mainloop()
