from database_manager import DatabaseManager
import os
import random
import sys

class HangmanGame:
    def __init__(self):
        self.db = DatabaseManager()

    def clean_screen(self):
        _ = os.system('cls')

    def drawing_status(self, mistakes):
        self.mistakes = mistakes

        match mistakes:
            case 0:
                print('''
                +---+
                |   |
                    |
                    |
                    |
                    |
                =========''')
            case 1:
                print('''
                +---+
                |   |
                O   |
                    |
                    |
                    |
                =========''')
            case 2:
                print('''
                +---+
                |   |
                O   |
                |   |
                    |
                    |
                =========''')
            case 3:
                print('''
                +---+
                |   |
                O   |
                /|  |
                    |
                    |
                =========''')
            case 4:
                print('''
                +---+
                |   |
                O   |
                /|\ |
                    |
                    |
                =========''')
            case 5:
                print(''' 
                +---+
                |   |
                O   |
                /|\ |
                /   |
                    |
                =========''')
            case 6:
                print('''
                +---+
                |   |
                O   |
                /|\ |
                / \ |
                    |
                =========''')

    def play(self):
        self.clean_screen()
        self.db.populate_if_empty()
        chosen = self.db.get_game_word()
        chosen = chosen.upper()
        game_word = list(chosen)
        hidden_word = ["_"] * len(game_word)
        mistakes = 0
        wrong_words = list()
        
        while mistakes < 6:
            win = False
            self.clean_screen()
            self.drawing_status(mistakes)
            print(hidden_word, "\n")
            print(">>> Wrong words: ", wrong_words)
            error_tracking = 6 - mistakes
            print(">>> You still have: " + str(error_tracking) + " attempts!\n")
            guess = str(input("Type your letter:\n"))
            guess = guess.upper()
            
            if guess in game_word:
                for i in range(0, len(game_word)):
                    if guess == game_word[i]:
                        hidden_word[i] = guess
                if "_" not in hidden_word:
                    self.clean_screen()
                    print("\n*****You won!!*****")
                    self.drawing_status(mistakes)
                    win = True
                print("\n")
                print(hidden_word)
                print("\n")
                

            else:
                if guess not in wrong_words:
                    mistakes = mistakes + 1
                    wrong_words.append(guess)

            if win:
                input("Press any key to continue:")
                break

        if mistakes == 6:
            self.clean_screen()
            self.drawing_status(mistakes)
            print("***No more attempts!***")
            print("Word: "+ chosen +"")
            print("***You lost!***")
            print("""
            1. Play again
            2. Return to Menu
            3. Exit program
            """)
            replay_choice = input("Type your choice (1-3): ")
            if replay_choice == "1":
                self.play()
            elif replay_choice == "2":
                pass
            elif replay_choice == "3":
                self.clean_screen()
                print("Thanks for playing!")
                sys.exit()

    def add_word(self):
        self.db.add_word()

    def reset_db_status(self):
        self.db.reset_db_status()

    def database_menu(self):
        self.db.manage_database()

    def main_menu(self):
        while True:
            self.clean_screen()
            print("""
            === HANGMAN GAME ===\n
            1. Play 
            2. Reset Played Words
            3. Manage Word Database
            4. Exit
            """)
            escolha = input("Type your choice (1-4): ")
            match escolha:
                case '1': 
                    self.play()
                case '2': 
                    self.reset_db_status()
                case '3': 
                    self.database_menu()
                case '4': 
                    self.clean_screen()
                    print("Thanks for playing!")
                    break

if __name__ == "__main__":
    jogo = HangmanGame()
    jogo.main_menu()