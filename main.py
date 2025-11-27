from database_manager import DatabaseManager
import os
import random
import sys

class JogoForca:
    def __init__(self):
        self.db = DatabaseManager()

    def limpar_tela(self):
        _ = os.system('cls')

    def status_desenho(self, erros):
        self.erros = erros

        match erros:
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

    def jogar(self):
        self.limpar_tela()
        self.db.populate_if_empty()
        
        #file_handle = open(r"randomlist.txt")
        #words = file_handle.readlines()
        #qty_words = len(words)
        #random_number = random.randint(0, qty_words - 1)
        #chosen = words[random_number]

        chosen = self.db.get_palavra_jogo()
        chosen = chosen.upper()
        game_word = list(chosen)
        hidden_word = ["_"] * len(game_word)
        erros = 0
        wrong_words = list()
        
        while erros < 6:
            win = False
            self.limpar_tela()
            self.status_desenho(erros)
            print(hidden_word, "\n")
            print(">>> Wrong words: ", wrong_words)
            error_tracking = 6 - erros
            print(">>> You still have: " + str(error_tracking) + " attempts!\n")
            guess = str(input("Type your letter:\n"))
            guess = guess.upper()
            
            if guess in game_word:
                for i in range(0, len(game_word)):
                    if guess == game_word[i]:
                        print("Well done!!")
                        hidden_word[i] = guess
                if "_" not in hidden_word:
                    print("\n*****You won!!*****")
                    win = True
                print("\n")
                print(hidden_word)
                print("\n")

            else:
                if guess not in wrong_words:
                    erros = erros + 1
                    wrong_words.append(guess)

            if win:
                break

        if erros == 6:
            self.limpar_tela()
            self.status_desenho(erros)
            print("***No more attempts!***")
            print("Word: "+ chosen +"")
            print("***You lost!***")
            print("""
            1. Jogar novamente
            2. Voltar ao menu
            3. Sair do Programa
            """)
            escolha_replay = input("Digite sua escolha (1-3): ")
            if escolha_replay == "1":
                self.jogar()
            elif escolha_replay == "2":
                pass
            elif escolha_replay == "3":
                self.limpar_tela()
                print("Obrigado por Jogar!")
                sys.exit()

    def add_palavra(self):
        self.db.gerenciar_banco()

    def reset_db_status(self):
        self.db.reset_db_status()

    def gerenciar_banco(self):
        self.db.gerenciar_banco()

    def menu_principal(self):
        while True:
            self.limpar_tela()
            print("""
            === JOGO DA FORCA ===\n
            1. Jogar
            2. Resetar Palavras Jogadas
            3. Gerenciar Banco de Palavras
            4. Sair
            """)
            escolha = input("Digite sua escolha (1-4): ")
            match escolha:
                case '1': 
                    self.jogar()
                case '2': 
                    self.reset_db_status()
                case '3': 
                    self.gerenciar_banco()
                case '4': 
                    self.limpar_tela()
                    print("Obrigado por Jogar!")
                    break

if __name__ == "__main__":
    jogo = JogoForca()
    jogo.menu_principal()