import sqlite3

def fazer_login(usuario, senha):
    conexao = sqlite3.connect("banco_de_dados.db")
    cursor = conexao.cursor()

    # Parametrização: os valores nunca são interpretados como parte do SQL
    query = "SELECT * FROM usuarios WHERE username = ? AND password = ?"
    cursor.execute(query, (usuario, senha))
    
    resultado = cursor.fetchone()
    conexao.close()
    if resultado:
        return "Acesso Permitido!"
    else:
        return "Acesso Negado!"