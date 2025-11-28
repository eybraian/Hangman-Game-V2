from tabulate import tabulate
import sqlite3
import os

class DatabaseManager: 
    def __init__(self):
        self.connection = sqlite3.connect('database.db')
        self.cursor = self.connection.cursor()
        self.populate_if_empty()

    def clean_screen(self):
        _ = os.system('cls')
    
    def populate_if_empty(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS WordsDatabase (
        word TEXT PRIMARY KEY,
        played BOOLEAN NOT NULL DEFAULT 0);
        ''')
        
        self.cursor.execute("SELECT COUNT(*) FROM WordsDatabase")
        count = self.cursor.fetchone()[0]
        
        if count == 0:
            sample_words = ['AVOCADO', 'GRAPE', 'WATERMELON', 'SCISSORS', 'GUITAR', 'DOORBEL', 'FILE', 'DOOR', 'WINDOW', 'SOCCER', 'COMPUTER', 'HORSE']
            for word in sample_words:
                self.cursor.execute("INSERT INTO WordsDatabase (word) VALUES (?)", (word,))
        
        self.connection.commit()

    def add_word(self, new_word):
        if new_word.strip():
            self.cursor.execute("INSERT INTO WordsDatabase (word) VALUES (?)", (new_word.upper(),))
            self.connection.commit()
            print('Word '+ new_word + ' sucessfuly added!')

    def remove_word(self, unwanted_word):
        self.cursor.execute("DELETE FROM WordsDatabase WHERE word = ?", (unwanted_word.upper(),))
        self.connection.commit()
        print('Word '+ unwanted_word + ' sucessfuly removed!')

    def show_database(self):
        self.cursor.execute("SELECT * FROM WordsDatabase ORDER BY word ASC")
        rows = self.cursor.fetchall()

        formatted_rows = []
        for row in rows:
            played_status_icon = "✓" if row[1] else "X"
            formatted_rows.append([row[0], played_status_icon])

        headers = ["Word", "Played"]
        print("\n=== WORD DATABASE ===")
        print(tabulate(formatted_rows, headers=headers, tablefmt="grid"))

    def manage_database(self):
        while True:
            self.clean_screen()
            print('''
            === DATABASE MANAGING ===
                  
            1. Add New Word
            2. Remove Word
            3. Show Database Words
            4. Return to Menu
            ''')
            database_menu = input("Type your choice (1-4): ")
            match database_menu:
                case '1':
                    self.clean_screen()
                    new_word = input('Type the new word to be added to the game: ')
                    self.add_word(new_word)
                    input('Press any key to continue: ')
                       
                case '2':
                    self.clean_screen()
                    unwanted_word = input('Type the word to be removed from the game: ')
                    self.remove_word(unwanted_word)
                    input('Press any key to continue: ')
                        
                case '3':
                    self.clean_screen()
                    self.show_database()
                    input('Press any key to continue: ')
                case '4':
                    break
                    
    def reset_db_status(self):
        self.cursor.execute("UPDATE WordsDatabase SET played = 0")
        self.connection.commit()
        self.clean_screen()
        print("Database word's status sucessfuly turned to Unplayed!")
        input('Press any key to continue: ')     

    def get_game_word(self):
        self.cursor.execute("SELECT word FROM WordsDatabase WHERE played = 0 ORDER BY RANDOM() LIMIT 1")
        result = self.cursor.fetchone()

        if result:
            word = result[0]
            self.cursor.execute("UPDATE WordsDatabase SET played = 1 WHERE word = ?", (word,))
            self.connection.commit()
            return word
        else:
            self.reset_db_status()
            return self.get_game_word