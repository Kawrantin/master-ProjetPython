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
				    PRIMARY KEY(id))""")
			cursor.execute("""
				CREATE TABLE IF NOT EXISTS activite (
					idAct int(5) NOT NULL AUTO_INCREMENT,
					nom varchar(50) DEFAULT NULL,
				    PRIMARY KEY(idAct)) """)
			cursor.execute("""
				CREATE TABLE IF NOT EXISTS installation (
				    id varchar(50) DEFAULT NULL,
				    nom varchar(50) DEFAULT NULL,
				    adresse varchar(50) DEFAULT NULL,
				    codePostal INTEGER DEFAULT NULL,
				    ville varchar(50) DEFAULT NULL,
				    latitude INTEGER DEFAULT NULL,
				    longitude INTEGER DEFAULT NULL,
				    PRIMARY KEY(id)) """)
		except:
			print("ERREUR : La table existe déjà.")
		self.conn.commit()


	def insertInstall(self, ide, nom, adresse, codePostal, ville, latitude, longitude):
		cursor = self.conn.cursor()
		try:
			cursor.execute("""
				INSERT INTO pagesTEST (id, nom, adresse, codePostal, ville, latitude, longitude)
				VALUES(%s, %s, %s, %s, %s, %s, %s)""", (ide, nom, adresse, codePostal, ville, latitude, longitude))
		except:
			print("La page existe déjà.")
			self.conn.commit()

	def insertActivite(self, nom):
		cursor = self.conn.cursor()
		try:
			cursor.execute("""
				INSERT INTO pagesTEST (numInstall, nomInstall, numAdresse, adresse, codePostal, ville, latitude, longitude)
				VALUES(%s, %s, %s, %s, %s, %s, %s, %s)""", (numInstall, nomInstall, numAdresse, adresse, codePostal, ville, latitude, longitude))
		except:
			print("La page existe déjà.")
			self.conn.commit()


"""Getters:"""
	def getAdresse(self, ide):
		cursor = self.conn.cursor()
		try:
			cursor.execute("""SELECT adPage FROM pagesTEST WHERE idPage = %s""", [ide])
		except:
			print("ERREUR : Indentifiant inexistant.")
		else:
		row = cursor.fetchone()
		while row :
			# print(row)
			if row is not None:
				break
			row = cursor.fetchone()
		return row[0]


	def getNbLien(self, ide): #Fonctionne
		cursor = self.conn.cursor()
		try:
		cursor.execute("""SELECT nbLiens FROM pagesTEST WHERE idPage = %s""", [ide]) # %s qui bug
		except:
			print("ERREUR : Indentifiant inexistant.")
		else:
		row = cursor.fetchone()
		while row :
			if row is not None:
				break
			row = cursor.fetchone()
		return row[0]

	def getPageRank(self, ide):
		cursor = self.conn.cursor()
		cursor.execute("""SELECT pRank FROM pagesTEST WHERE idPage = %s""", [ide])
		except:
			print("ERREUR : Indentifiant inexistant.")
		else:
		row = cursor.fetchone()
		while row :
			if row is not None:
				break
			row = cursor.fetchone()
		return row[0]

	def getId(self, addr):
		cursor = self.conn.cursor()
		cursor.execute("""SELECT idPage FROM pagesTEST WHERE adPage = %s """, [addr])
		except:
			print("ERREUR : Indentifiant inexistant.")
		else:
		row = cursor.fetchone()
		while row :
			if row is not None:
				break
			row = cursor.fetchone()
		return row[0]


"""Setters:"""
	def setAdresse(self, ide, adPage):
		cursor = self.conn.cursor()
		cursor.execute("""UPDATE pagesTEST SET adPage = %s WHERE idPage = %s """, (adPage, ide))
		self.conn.commit()

	def setNbLien(self, ide, nbLiens):
		cursor = self.conn.cursor()
		cursor.execute("""UPDATE pagesTEST SET nbLiens = %s WHERE idPage = %s """, (nbLiens, ide))
		self.conn.commit()

	def setPageRank(self, ide, pRank):
		cursor = self.conn.cursor()
		cursor.execute("""UPDATE pagesTEST SET pRank = %s WHERE idPage = %s """, (pRank, ide))
		self.conn.commit()

	def deco(self):
		self.conn.close()
