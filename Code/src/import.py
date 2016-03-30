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


	fname = "data/activite.csv"
	file1 = open(fname, "r")

	fname2 = "data/equipements.csv"
	file2 = open(fname2, "r")

	fname3 = "data/installations.csv"
	file3 = open(fname3, "r")




	try:
		reader = csv.reader(file1, delimiter=',', quotechar='"')
		for row in reader:
			try:
				if (""+row[2] +","+ row[4]) not in idEA:
					gp.insertEquipActiv(row[2], row[4])
					print (row[2] + " " + row[4])
					idEA.append(""+row[2]+","+ row[4])
			except RuntimeError as e:
				print("ERREUR : " + e.strerror)

	except RuntimeError as e:
		print("ERREUR : " + e.strerror)



	finally:
		 file1.close()
		 file2.close()
		 file3.close()

if (__name__=="__main__"):
	main()

