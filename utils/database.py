import sqlite3

DB_NAME = "culture_ivoirienne.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    # Création des tables si elles n’existent pas
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS proverbes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        texte TEXT NOT NULL
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS recettes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT NOT NULL,
        description TEXT
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS evenements (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT NOT NULL,
        lieu TEXT,
        periode TEXT
    )
    """)
    conn.commit()
    conn.close()

def inserer_proverbe(texte):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO proverbes (texte) VALUES (?)", (texte,))
    conn.commit()
    conn.close()

def lire_proverbes():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM proverbes")
    resultats = cursor.fetchall()
    conn.close()
    return resultats
