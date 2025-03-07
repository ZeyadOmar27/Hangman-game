import random

def main():
    game()

words = ["Lantern", "Whisper", "Echo", "Fragment", "Serpent", "Obsidian", "Drift", "Velvet", "Quiver", "Solstice"]

def get():
    random_word = random.choice(words).lower()
    return random_word

def display(random_word):
    print("Welcome To Hangman!")
    blanks = "_" * len(random_word)  
    print (blanks)
    return blanks 

def game():
    guessed_letters = []
    random_word = get()
    blanks = display(random_word)
    list_blanks = list(blanks)
    attempts = 5

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already tried that letter.")
            continue
        guessed_letters.append(guess)

        if guess in random_word:
            for index, letter in enumerate(random_word):
                if letter == guess:
                    list_blanks[index] = guess 
            print(" ".join(list_blanks) + "   That's right!")

            if "_" not in list_blanks:
                print("You Won!")
                return 
        else:
            print("Not Right!")
            attempts -= 1
            print(f"Attempts left: {attempts}")

    print(f"You lost! The word was: {random_word}")

if __name__ == "__main__":
    main()
