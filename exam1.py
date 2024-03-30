import random

def load_words():
    
    return ["полуниця", "авто", "клей", "телефон", "папір", "шкарпетки", "собака"]

def choose_word(word_list):
    return random.choice(word_list)

def main():
    print("вітайємо у грі слова!")
    words = load_words()
    current_word = choose_word(words)
    guessed_letters = []
    attempts = 6
    
    while attempts > 0:
        display_word = ""
        for letter in current_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        print("слово:", display_word)
        print("кількість спроб:", attempts)
       
        guess = input("введіть літеру: ").lower()
