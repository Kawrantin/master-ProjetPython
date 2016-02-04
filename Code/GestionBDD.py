#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Gestion d'une BDD sqlite
import sqlite3

# Creation de la BDD
conn = sqlite3.connect('ma_base.db')
# BDD temporaire:
#conn = sqlite3.connect(':memory:')


# Creation d'une table dans la BDD
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
     id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     name TEXT,
     age INTERGER
)""")
conn.commit()

# Suppression d'une table de la BDD
cursor = conn.cursor()
cursor.execute("""DROP TABLE users""")
conn.commit()

# Insertion de donnees dans la BDD
# Technique 1\
cursor.execute("""
INSERT INTO users(name, age) VALUES(?, ?)""", ("olivier", 30))
# Technique 2\
data = {"name" : "olivier", "age" : 30}
cursor.execute("""
INSERT INTO users(name, age) VALUES(:name, :age)""", data)
# Technique 3\ + recuperation de l'id de la ligne
id = cursor.lastrowid
print('dernier id: %d' % id)
# Plusieurs insert en meme temps
users = []
users.append(("olivier", 30))
users.append(("jean-louis", 90))
cursor.executemany("""
INSERT INTO users(name, age) VALUES(?, ?)""", users)

# Recuperer un tuple de donnees
cursor.execute("""SELECT name, age FROM users""")
user1 = cursor.fetchone()
print(user1)
# Recuperer plusieurs tuples de donnees
cursor.execute("""SELECT id, name, age FROM users""")
rows = cursor.fetchall() #Ligne non obligatoire
for row in rows:
    print('{0} : {1} - {2}'.format(row[0], row[1], row[2]))
# Recherche d'un tuple precis
id = 2
cursor.execute("""SELECT id, name FROM users WHERE id=?""", (id,))
response = cursor.fetchone()

# Modification d'un tuple
cursor.execute("""UPDATE users SET age = ? WHERE id = 2""", (31,))

# Revenir au dernier commit()
conn.rollback()

# Gestion des erreurs
try:
    conn = sqlite3.connect('data/users.db')
    cursor = conn.cursor()
    cursor.execute("""
CREATE TABLE users(
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT,
    age INTERGER
)
""")
    conn.commit()
except sqlite3.OperationalError:
    print('Erreur la table existe déjà')
except Exception as e:
    print("Erreur")
    conn.rollback()
    # raise e
finally:
    conn.close()

# Erreurs pouvant etre attrapees
##Error
##DatabaseError
##DataError
##IntegrityError
##InternalError
##NotSupportedError
##OperationalError
##ProgrammingError
##InterfaceError
##Warning





# Fermeture de la connection a la BDD
db.close()
