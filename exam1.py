import random

def load_words():
    return {
        "полуниця": "це смачна ягода",
        "авто": "це засіб транспорту",
        "клей": "це речовина для склеювання",
        "телефон": "це пристрій для зв'язку",
        "папір": "це матеріал для запису або малювання",
        "шкарпетки": "це одяг для ніг",
        "собака": "це домашня тварина"
    }

def choose_word(word_list):
    return random.choice(list(word_list.keys()))

def main():
    print("Вітаємо у грі слова!")
    while True:
        words = load_words()
        current_word = choose_word(words)
        guessed_letters = []
        attempts = 6
        
        print("Підказка:", words[current_word])
        
        while attempts > 0:
            display_word = ""
            for letter in current_word:
                if letter in guessed_letters:
                    display_word += letter + " "
                else:
                    display_word += "_ "
            print("Слово:", display_word)
            print("Кількість спроб:", attempts)
            
            guess = input("Введіть літеру або 'exit' для виходу: ").lower()

            if guess == "exit" or guess == "quit":
                print("Дякуємо за гру!")
                return 

            try:
                if len(guess) != 1 or not guess.isalpha():
                    raise ValueError("Будь ласка, введіть лише одну літеру")

                if guess in guessed_letters:
                    print("Ви вже вгадали цю літеру!")
                elif guess in current_word:
                    print("Вітаю! Ви вгадали літеру.")
                    guessed_letters.append(guess)
                    if all(letter in guessed_letters for letter in current_word):
                        print("Ви перемогли!")
                        break
                else:
                    print("На жаль, такої літери немає у слові.")
                    attempts -= 1
            except ValueError as ve:
                print(ve)

        if attempts == 0:
            print("На жаль, ви програли. Слово було '{}'.".format(current_word))
        
        play_again = input("Бажаєте зіграти ще раз? (так/ні): ").lower()
        if play_again != "так":
            print("Дякуємо за гру!")
            break 

if __name__ == "__main__":
    main()
