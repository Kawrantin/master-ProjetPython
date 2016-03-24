
#!usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
from GestionBDD import *


def main():
	gp = GestionBDD()
	gp.newTables()
	codesAct = []
	idEqu = []
	idIns = []
	idEA = []

	"""
	Ouverture des fichiers CSV
	"""
	fname = "data/activite.csv"
	file1 = open(fname, "r")

	fname2 = "data/equipements.csv"
	file2 = open(fname2, "r")

	fname3 = "data/installations.csv"
	file3 = open(fname3, "r")


	"""
	On parcourt chaques fichiers et on appelle les fonctions d'ajout de ligne dans la base de données.
	L'identifiant de chaque ligne ajoutée est enregistrée dans une liste ( idAct, idEqu, idIns ou idEA ) Donc, avant chaque ajout dans la
	base de données, on vérifie que l'identifiant de la ligne n'existe pas déjà dans la liste.
	On entoure chaque insertion d'exception pour pouvoir afficher les erreurs.
	"""
	try:
		reader = csv.reader(file1, delimiter=',', quotechar='"')
		for row in reader:
			try:
				if row[4] not in codesAct:
					gp.insertActivite(row[4], row[5])
					codesAct.append(row[4])
			except RuntimeError as e:
				print("ERREUR : " + e.strerror)

	except RuntimeError as e:
		print("ERREUR : " + e.strerror)


	try:
		reader3 = csv.reader(file3, delimiter=',', quotechar='"')
		for row in reader3:
			try:
				if row[1] not in idIns:
					gp.insertInstall(row[1],row[0],row[7],row[4],row[2],row[10],row[9])
					idIns.append(row[1])
			except RuntimeError as e:
				print("ERREUR : " + e.strerror)
	except RuntimeError as e:
		print("ERREUR : " + e.strerror)


	try:
		reader2 = csv.reader(file2, delimiter=',', quotechar='"')
		for row in reader2:
			try:
				if row[4] not in idEqu:
					gp.insertEquip(row[4], row[5], row[2])
					idEqu.append(row[4])
			except RuntimeError as e:
				print("ERREUR : " + e.strerror)
	except RuntimeError as e:
		print("ERREUR : " + e.strerror)

	file1.close()
	file1 = open(fname, "r")

	try:
		reader4 = csv.reader(file1, delimiter=',', quotechar='"')
		for row in reader4:
			try:
				if (""+row[2] +","+ row[4]) not in idEA:
					gp.insertEquipActiv(row[2], row[4])
					print (row[2] + " " + row[4])
					idEA.append(""+row[2]+","+ row[4])
			except RuntimeError as e:
				print("ERREUR : " + e.strerror)

	except RuntimeError as e:
		print("ERREUR : " + e.strerror)


	# """
	# Fin du programme on ferme toute les connections.
	# """
	finally:
		file1.close()
		file2.close()
		file3.close()
		gp.deco()

"""
Appel du main
"""
if (__name__=="__main__"):
	main()
