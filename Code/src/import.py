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


	fname = "data/activite.csv"
	file1 = open(fname, "r")

	fname2 = "data/equipements.csv"
	file2 = open(fname2, "r")

	fname3 = "data/installations.csv"
	file3 = open(fname3, "r")

	# try:
	# 	reader = csv.reader(file1, delimiter=',', quotechar='"')
	# 	for row in reader:
	# 		try:
	# 			if row[4] not in codesAct:
	# 				gp.insertActivite(row[4], row[5])
	# 				codesAct.append(row[4])
	# 		except RuntimeError as e:
	# 			print("ERREUR : " + e.strerror)
	#
	# except RuntimeError as e:
	# 	print("ERREUR : " + e.strerror)
	#
	#
	# try:
	# 	reader3 = csv.reader(file3, delimiter=',', quotechar='"')
	# 	for row in reader3:
	# 		try:
	# 			if row[1] not in idIns:
	# 				gp.insertInstall(row[1],row[0],row[7],row[4],row[2],row[10],row[9])
	# 				idIns.append(row[1])
	# 		except RuntimeError as e:
	# 			print("ERREUR : " + e.strerror)
	# except RuntimeError as e:
	# 	print("ERREUR : " + e.strerror)
	#
	#
	# try:
	# 	reader2 = csv.reader(file2, delimiter=',', quotechar='"')
	# 	for row in reader2:
	# 		try:
	# 			if row[4] not in idEqu:
	# 				gp.insertEquip(row[4], row[5], row[2])
	# 				idEqu.append(row[4])
	# 		except RuntimeError as e:
	# 			print("ERREUR : " + e.strerror)
	# except RuntimeError as e:
	# 	print("ERREUR : " + e.strerror)


	try:
		reader = csv.reader(file1, delimiter=',', quotechar='"')
		for row in reader:
			try:
				gp.insertEquipActiv(row[2], row[4])
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

# import csv
# fname = "data/activite.csv"
# # file1 = open(fname, "r")

# # fname2 = "data/equipements.csv"
# # file2 = open(fname2, "r")

# # fname3 = "data/installations.csv"
# # file3 = open(fname3, "r")

# with open(fname, 'rt') as f:

#	 reader = csv.reader(f, delimiter=',', quotechar='"')
#	 for row in reader:
#		 act = Activite(row[1], row[0])
#		 print(act)

# f.close();
#	 # reader2 = csv.reader(file2, delimiter=',', quotechar='"')
#	 # for row in reader2:
#	 #	 print (row)

#	 # reader3 = csv.reader(file3, delimiter=',', quotechar='"')
#	 # for row in reader3:
#	 #	 print (row)
