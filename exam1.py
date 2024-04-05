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
       
       try:
            guess = input("Введіть літеру: ").lower()

            if len(guess) != 1 or not guess.isalpha():
                raise ValueError("Будь ласка, введіть лише одну літеру")

            if guess in guessed_letters:
                print("Ви вже вгадали цю літеру!")
            elif guess in current_word:
                print("Вітаю! Ви вгадали літеру.")
                guessed_letters.append(guess)
                if all(letter in guessed_letters for letter in current_word):
                    print("Вітаю! Ви перемогли! Слово було '{}'.".format(current_word))
                    break
            else:
                print("На жаль, такої літери немає у слові.")
                attempts -= 1
        except ValueError as ve:
            print(ve)

    if attempts == 0:
        print("На жаль, ви програли. Слово було '{}'.".format(current_word))

if __name__ == "__main__":
    main()
