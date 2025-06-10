import random

def hangman():
    word_list = ["varsha", "saanvi", "aadhya", "coding", "laptop"]
    word = random.choice(word_list)
    guessed_letters = []
    attempts = 6  #  6 incorrect guesses
    score = 0

    print("Hello, my name is Varsha and I am your game host.")
    print("Let's play a game of Hangman!")
    print("🎮 Welcome to Hangman game with Scoring")
    print(f"You have {attempts} incorrect guesses allowed.")
    print("_ " * len(word))

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("❗ Please enter a single alphabet letter.")
            continue

        if guess in guessed_letters:
            print("⛔ You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("✅ Good guess!")
            score += 5  # add points for a correct guess
        else:
            attempts -= 1
            print(f"❌ Wrong guess! Attempts left: {attempts}")
            score -= 2  # Subtract points for a wrong guess

        # Display current progress
        display_word = [letter if letter in guessed_letters else "_" for letter in word]
        print(" ".join(display_word))
        print(f"Current Score: {score}")

        if "_" not in display_word:
            print(f"🎉 Congratulations! You've guessed the word '{word}'!")
            break
    else:
        print(f"💀 Game Over! The word was '{word}'.")

    print(f"🏁 Final Score: {score}")

# Run the game
hangman()