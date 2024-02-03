import random
import time

# List of random sentences for the typing test
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a high-level programming language.",
    "Practice makes perfect.",
    "Coding is fun and challenging.",
    "Hello, world!",
    "Programming is all about solving problems.",
]

def get_random_sentence():
    return random.choice(sentences)

def typing_test():
    print("Welcome to the Speed Typing Test!")
    input("Press Enter to start...")

    while True:
        sentence = get_random_sentence()
        print(f"\nType this sentence: {sentence}")
        input("Press Enter when ready...")
        start_time = time.time()
        user_input = input("Start typing: ")

        end_time = time.time()
        typing_time = end_time - start_time

        if user_input == sentence:
            words_per_minute = len(sentence.split()) / (typing_time / 60)
            print(f"Your typing speed: {words_per_minute:.2f} words per minute")
        else:
            print("Incorrect! Please try again.")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

if __name__ == "__main__":
    typing_test()
