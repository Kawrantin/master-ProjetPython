"""Creation des tables, Une seul execution."""

import csv
import mysql.connector 

conn = mysql.connector.connect(host="infoweb",user="E145425W",password="E145425W", database="E145425W") #MySQL
cursor = conn.cursor()

# Une installation compose de plusieurs equipements, un equipement regroupe plusieurs activitees & une activitee peut s'effectuee sur 
# plusieurs equipement
cursor.execute("""
CREATE TABLE IF NOT EXISTS installation (
    id varchar(50) DEFAULT NULL,
    nom varchar(50) DEFAULT NULL,
    adresse varchar(50) DEFAULT NULL,
    codePostal INTEGER DEFAULT NULL,
    ville varchar(50) DEFAULT NULL,
    latitude INTEGER DEFAULT NULL,
    longitude INTEGER DEFAULT NULL,
    PRIMARY KEY(numInstall))""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS equipement (
	id varchar(50) DEFAULT NULL,
    nom varchar(50) DEFAULT NULL,
	id_installation INTEGER DEFAULT NULL,
    PRIMARY KEY(idEqu))
	FORE KEY()""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS activite (
	idAct int(5) NOT NULL AUTO_INCREMENT,
	nom varchar(50) DEFAULT NULL,
    PRIMARY KEY(idAct))""")

# reader = csv.reader(open("installations.csv","rb")) #CSV
# for row in reader:
# 	user = (row[2], row[1], row[7], row[8], row[5], row[3], row[11], row[10])
# 	cursor.execute("""INSERT INTO installation (numInstall, nomInstall, numAdresse, adresse, codePostal, ville, latitude, longitude) 
# 	VALUES(%s, %s, %s, %s, %s, %s, %s, %s,)""", user)
# 	print (user)





conn.close()