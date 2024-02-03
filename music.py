import pygame
import os

def play_music(file_path):
    pygame.init()
    pygame.mixer.init()

    try:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        print(f"Playing: {os.path.basename(file_path)}")
        while pygame.mixer.music.get_busy():
            continue
    except pygame.error:
        print("Couldn't play the music.")

    pygame.mixer.quit()
    pygame.quit()

if __name__ == "__main__":
    while True:
        print("\n1. Play Music")
        print("2. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            file_path = input("Enter the path to the music file: ")
            if os.path.exists(file_path):
                play_music(file_path)
            else:
                print("File not found.")
        elif choice == '2':
            break
        else:
            print("Invalid choice. Please choose 1 or 2.")
