import tkinter
import random

words = ['python', 'java', 'kotlin', 'javascript']

hangman_art = [
    "   +---+\n   |   |\n       |\n       |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n       |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n   |   |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n  /|   |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n  /|\\  |\n       |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n  /|\\  |\n  /    |\n       |\n=========",
    "   +---+\n   |   |\n   O   |\n  /|\\  |\n  / \\  |\n       |\n========="
]


def choose_word():
    return random.choice(words)

def update_hangman(mistakes):
    hangman.label.configure(text=hangman_art[mistakes])


root = tkinter.Tk()
root.title("Hangman with Tkinter") 

hangman_label = tk.Label(root, text=hangman_art[0], font=("Helvetica", 12))
hangman_label.grid(row=0, column=0, columnspan=3)

word = choose_word()
word_with_blanks = '_' * len(word)
word_label = tk.Label(root, text=word_with_blanks, font=("Helvetica", 12))
word_label.grid(row=1, column=0, columnspan=3)


guess.entry = tk.Entry(root, font=("Helvetica", 12))
guess.entry.grid(row=2, column=0, columnspan=3)
guess.button = tk.Button(root, text="Guess", command=guess, font=("Helvetica", 12))





root.mainloop()
