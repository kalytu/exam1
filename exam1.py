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