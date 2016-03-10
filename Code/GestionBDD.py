#!usr/bin/env python3
# -*- coding: utf-8 -*-

<<<<<<< HEAD
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


# PRINT("PROBBLEM WITH ROw {) : {} 
=======
import mysql.connector

class GestionBDD(object):

	conn=None

	def __init__(self):
		self.conn = mysql.connector.connect(host="infoweb",user="",password="", database="")


	def newTables(self):
		cursor = self.conn.cursor()

		try:
			cursor.execute("""
				CREATE TABLE IF NOT EXISTS activite (
					idAct INTEGER NOT NULL,
					nom varchar(255) DEFAULT NULL,
					PRIMARY KEY(idAct))
				DEFAULT CHARSET=utf8  """)
			self.conn.commit()
		except RuntimeError as e:
			print("ERREUR : " + e.strerror)

		try:
			cursor.execute("""
				CREATE TABLE IF NOT EXISTS installation (
					id varchar(255) DEFAULT NULL,
					nom varchar(255) DEFAULT NULL,
					adresse varchar(255) DEFAULT NULL,
					codePostal INTEGER DEFAULT NULL,
					ville varchar(255) DEFAULT NULL,
					latitude FLOAT DEFAULT NULL,
					longitude FLOAT DEFAULT NULL,
					PRIMARY KEY(id))
				DEFAULT CHARSET=utf8  """)
			self.conn.commit()
		except RuntimeError as e:
			print("ERREUR : " + e.strerror)

		try:
			cursor.execute("""
				CREATE TABLE IF NOT EXISTS equipement (
					id varchar (255) DEFAULT NULL,
					nom varchar(255) DEFAULT NULL,
					id_installation varchar(255) DEFAULT NULL,
					PRIMARY KEY(id),
					FOREIGN KEY (id_installation) REFERENCES installation(id) ON DELETE CASCADE ON UPDATE CASCADE)
				DEFAULT CHARSET=utf8 """)
			self.conn.commit()
		except RuntimeError as e:
			print("ERREUR : " + e.strerror)

		try:
			cursor.execute("""
				CREATE TABLE IF NOT EXISTS Equip_Activ (
					id_equip varchar(255) DEFAULT NULL,
					id_activ INTEGER DEFAULT NULL,
					PRIMARY KEY(id_equip, id_activ),
					FOREIGN KEY (id_equip) REFERENCES equipement(id) ON DELETE CASCADE ON UPDATE CASCADE,
					FOREIGN KEY (id_activ) REFERENCES activite(idAct) ON DELETE CASCADE ON UPDATE CASCADE)
				DEFAULT CHARSET=utf8  """)
			self.conn.commit()
		except RuntimeError as e:
			print("ERREUR : " + e.strerror)


	"""Fonctions d'ajouts"""
	def insertInstall(self, idi, nom, adresse, codePostal, ville, latitude, longitude):
		cursor = self.conn.cursor()
		try:
			cursor.execute("""INSERT INTO installation (id, nom, adresse, codePostal, ville, latitude, longitude) VALUES(%s, %s, %s, %s, %s, %s, %s)""", (idi, nom, adresse, codePostal, ville, latitude, longitude))
		except RuntimeError as e:
			print("ERREUR : " + e.strerror)
		else:
			self.conn.commit()


	def insertActivite(self, ida, nom):
		cursor = self.conn.cursor()
		try:
			cursor.execute("""INSERT INTO activite (id, nom) VALUES(%s, %s)""", (ida, nom))
		except RuntimeError as e:
			print("ERREUR : " + e.strerror)
		else:
			self.conn.commit()


	def insertEquip(self, ide, nom, id_installation):
		cursor = self.conn.cursor()
		try:
			cursor.execute("""INSERT INTO equipement (id, nom, id_installation) VALUES(%s, %s, %s)""", (ide, nom, id_installation))
		except RuntimeError as e:
			print("ERREUR : " + e.strerror)
		else:
			self.conn.commit()


	def insertEquipActiv(self, id_equip, id_activ):
		cursor = self.conn.cursor()
		try:
			cursor.execute("""INSERT INTO Equip_Activ (id_equip, id_activ) VALUES(%s, %s)""", (id_equip, id_activ))
		except RuntimeError as e:
			print("ERREUR : " + e.strerror)
		else:
			self.conn.commit()


	"""Getters: (Juste la forme)"""
		# def getAdresse(self, ide):
		# 	cursor = self.conn.cursor()
		# 	try:
		# 		cursor.execute("""SELECT adPage FROM pagesTEST WHERE idPage = %s""", [ide])
		# 	except:
		# 		print("ERREUR : Indentifiant inexistant.")
		# 	else:
		# 	row = cursor.fetchone()
		# 	while row :
		# 		# print(row)
		# 		if row is not None:
		# 			break
		# 		row = cursor.fetchone()
		# 	return row[0]

	"""Setters: (Juste la forme)"""
		# def setAdresse(self, ide, adPage):
		# 	cursor = self.conn.cursor()
		# 	cursor.execute("""UPDATE pagesTEST SET adPage = %s WHERE idPage = %s """, (adPage, ide))
		# 	self.conn.commit()

	"""Fonction de déconnexion de la BDD"""
	def deco(self):
		self.conn.close()
>>>>>>> b6122ca7d07e8702026d498e89e4b1e59f4ce73e
