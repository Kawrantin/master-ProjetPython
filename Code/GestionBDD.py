#!usr/bin/env python3
# -*- coding: utf-8 -*-

import mysql.connector

class GestionBDD(object):

	conn=None

	def __init__(self):
		self.conn = mysql.connector.connect(host="infoweb",user="E145425W",password="E145425W", database="E145425W")


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
			print("ERREUR Activite: " + e.strerror)

		try:
			cursor.execute("""
				CREATE TABLE IF NOT EXISTS installation (
					id varchar(255) NOT NULL,
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
			print("ERREUR Installation: " + e.strerror)

		try:
			cursor.execute("""
				CREATE TABLE IF NOT EXISTS equipement (
					id varchar (255) NOT NULL,
					nom varchar(255) DEFAULT NULL,
					id_installation varchar(255),
					PRIMARY KEY(id),
					FOREIGN KEY (id_installation) REFERENCES installation(id) ON DELETE CASCADE ON UPDATE CASCADE)
				DEFAULT CHARSET=utf8 """)
			self.conn.commit()
		except RuntimeError as e:
			print("ERREUR Equipement: " + e.strerror)

		try:
			cursor.execute("""
				CREATE TABLE IF NOT EXISTS equip_activ (
					id_equip varchar(255) NOT NULL,
					id_activ INTEGER NOT NULL,
					PRIMARY KEY(id_equip, id_activ),
					FOREIGN KEY (id_equip) REFERENCES equipement(id) ON DELETE CASCADE ON UPDATE CASCADE,
					FOREIGN KEY (id_activ) REFERENCES activite(idAct) ON DELETE CASCADE ON UPDATE CASCADE)
				DEFAULT CHARSET=utf8  """)
			self.conn.commit()
		except RuntimeError as e:
			print("ERREUR Equip_ActivAct: " + e.strerror)


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
			cursor.execute("""INSERT INTO activite (idAct, nom) VALUES(%s, %s)""", (ida, nom))
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
			cursor.execute("""INSERT INTO equip_activ (id_equip, id_activ) VALUES(%s, %s)""", (id_equip, id_activ))
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
