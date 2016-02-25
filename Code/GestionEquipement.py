#!usr/bin/env python3
# -*- coding: utf-8 -*-

import mysql.connector

class GestionBD(object):

	conn=None

	def __init__(self):
		self.conn = mysql.connector.connect(host="infoweb",user="",password="", database="")


	def newTables(self):
		cursor = self.conn.cursor()
		try:
			cursor.execute("""
				CREATE TABLE IF NOT EXISTS equipement (
					id varchar(50) DEFAULT NULL,
				    nom varchar(50) DEFAULT NULL,
					id_installation INTEGER DEFAULT NULL,
				    PRIMARY KEY(id),
					FOREIGN KEY (id_installation) REFERENCES installation(id) ON DELETE CASCADE ON UPDATE CASCADE)
				DEFAULT CHARSET=utf8 """)
			cursor.execute("""
				CREATE TABLE IF NOT EXISTS activite (
					idAct int(5) NOT NULL AUTO_INCREMENT,
					nom varchar(50) DEFAULT NULL,
				    PRIMARY KEY(idAct))
				DEFAULT CHARSET=utf8  """)
			cursor.execute("""
				CREATE TABLE IF NOT EXISTS installation (
				    id varchar(50) DEFAULT NULL,
				    nom varchar(50) DEFAULT NULL,
				    adresse varchar(50) DEFAULT NULL,
				    codePostal INTEGER DEFAULT NULL,
				    ville varchar(50) DEFAULT NULL,
				    latitude INTEGER DEFAULT NULL,
				    longitude INTEGER DEFAULT NULL,
				    PRIMARY KEY(id))
				DEFAULT CHARSET=utf8  """)
			cursor.execute("""
				CREATE TABLE IF NOT EXISTS Equip_Activ (
				    id_equip varchar(50) DEFAULT NULL,
				    id_activ varchar(50) DEFAULT NULL,
					FOREIGN KEY (id_equip) REFERENCES equipement(id) ON DELETE CASCADE ON UPDATE CASCADE,
					FOREIGN KEY (id_activ) REFERENCES activite(idAct) ON DELETE CASCADE ON UPDATE CASCADE
				DEFAULT CHARSET=utf8  """)
		except:
			print("ERREUR : La table existe déjà.")
		else:
			self.conn.commit()

"""Fonctions d'ajouts"""
	def insertInstall(self, ide, nom, adresse, codePostal, ville, latitude, longitude):
		cursor = self.conn.cursor()
		try:
			cursor.execute("""
				INSERT INTO pagesTEST (id, nom, adresse, codePostal, ville, latitude, longitude)
				VALUES(%s, %s, %s, %s, %s, %s, %s)""", (ide, nom, adresse, codePostal, ville, latitude, longitude))
		except:
			print("L'installation existe déjà.")
		else:
			self.conn.commit()


	def insertActivite(self, ide, nom):
		cursor = self.conn.cursor()
		try:
			cursor.execute("""
				INSERT INTO pagesTEST (id, nom)
				VALUES(%s, %s)""", (ide, nom))
		except:
			print("L'activité existe déjà.")
		else:
			self.conn.commit()


	def insertEquip(self, ide, nom, id_installation):
		cursor = self.conn.cursor()
		try:
			cursor.execute("""
				INSERT INTO pagesTEST (id, nom, id_installation)
				VALUES(%s, %s, %s)""", (ide, nom, id_installation))
		except:
			print("L'equipement existe déjà.")
		else:
			self.conn.commit()


	def insertEquip(self, id_equip, id_activ):
		cursor = self.conn.cursor()
		try:
			cursor.execute("""
				INSERT INTO pagesTEST (id_equip, id_activ)
				VALUES(%s, %s)""", (id_equip, id_activ))
		except:
			print("L'ensemble existe déjà.")
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
