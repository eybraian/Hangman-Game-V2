import sqlite3
import random
import os

class DatabaseManager: 
    def __init__(self):
        self.connection = sqlite3.connect('database.db')
        self.cursor = self.connection.cursor()
        self.populate_if_empty()

    def limpar_tela(self):
        _ = os.system('cls')
    
    def populate_if_empty(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS palavras (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            word TEXT NOT NULL,
            played BOOLEAN NOT NULL DEFAULT 0);
        ''')
        
        self.cursor.execute("SELECT COUNT(*) FROM palavras")
        count = self.cursor.fetchone()[0]
        
        if count == 0:
            sample_words = ['AVOCADO', 'GRAPE', 'WATERMELON', 'SCISSORS', 'GUITAR', 'DOORBEL', 'FILE', 'DOOR', 'WINDOW', 'SOCCER', 'COMPUTER', 'HORSE']
            for word in sample_words:
                self.cursor.execute("INSERT INTO palavras (word) VALUES (?)", (word,))
        
        self.connection.commit()

    def add_palavra(self, nova_palavra):
        if nova_palavra.strip():
            self.cursor.execute("INSERT INTO palavras (word) VALUES (?)", (nova_palavra.upper(),))
            self.connection.commit()
            print('Palavra '+ nova_palavra + ' adicionada com sucesso!')

    def remove_palavra(self, palavra_indesejada):
        self.cursor.execute("DELETE FROM palavras WHERE word = ?", (palavra_indesejada.upper(),))
        self.connection.commit()
        print('Palavra '+ palavra_indesejada + ' removida com sucesso!')

    def mostra_banco(self):
        self.cursor.execute("SELECT * FROM palavras")
        rows = self.cursor.fetchall()
        for row in rows:
            print(f"ID: {row[0]}, Word: {row[1]}, Played: {row[2]}")

    def gerenciar_banco(self):
        while True:
            self.limpar_tela()
            print('''
            === GERENCIAR BANCO DE PALAVRAS ===
                  
            1. Adicionar Palavra
            2. Remover Palavra
            3. Consultar Banco Existente
            4. Voltar ao Menu
            ''')
            menu_banco = input("Digite sua resposta (1-4): ")
            match menu_banco:
                case '1':
                    self.limpar_tela()
                    nova_palavra = input('Digite a palavra a inserir no jogo: ')
                    self.add_palavra(nova_palavra)
                    input('Digite qualquer tecla para continuar: ')
                       
                case '2':
                    self.limpar_tela()
                    palavra_indesejada = input('Digite a palavra a ser removida do jogo: ')
                    self.remove_palavra(palavra_indesejada)
                    input('Digite qualquer tecla para continuar: ')
                        
                case '3':
                    self.limpar_tela()
                    self.mostra_banco()
                    input('Digite qualquer tecla para continuar: ')
                case '4':
                    break
                    
    def reset_db_status(self):
        self.cursor.execute("UPDATE palavras SET played = 0")
        self.connection.commit()
        self.limpar_tela()
        print("Status das palavras resetado com sucesso!")
        input('Digite qualquer tecla para continuar: ')     

    def get_palavra_jogo(self):
        self.cursor.execute("SELECT word FROM palavras WHERE played = 0 ORDER BY RANDOM() LIMIT 1")
        result = self.cursor.fetchone()

        if result:
            word = result[0]
            self.cursor.execute("UPDATE palavras SET played = 1 WHERE word = ?", (word,))
            self.connection.commit()
            return word
        else:
            self.reset_db_status()
            return self.get_palavra_jogo