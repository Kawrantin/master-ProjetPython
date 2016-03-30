#!/usr/bin/python3
#-*- coding: utf-8 -*-


from libs.bottle import route, run, debug, template, request, static_file
import mysql
import mysql.connector
import sys
import urllib
import unittest



@route('/api/<item>') #contenu de l'url
def show_id(item):
    retour = ""
    ret = []
    conn = mysql.connector.connect(host="infoweb", user="E145425W", password="E145425W", database="E145425W") #connexion a la base de donnees
    c = conn.cursor()
<<<<<<< HEAD
    c.execute("SELECT e.nom FROM equipement e JOIN equip_activ ea ON e.id = ea.id_equip JOIN activite a ON ea.id_activ = a.idAct WHERE a.nom LIKE '%"+item+"%'") 
=======
    c.execute("SELECT e.nom FROM equipement e JOIN equip_activ ea ON e.id = ea.id_equip JOIN activite a ON ea.id_activ = a.idAct WHERE a.nom LIKE'%"+item+"%'")
    #on cherche le nom des equipements pour l'activite recherchee
>>>>>>> b899b8b934a384818951ae7111641fd8aa9d56c0
    result = c.fetchall()
    #cela nous renvoie un tableau des differentes reponses 
    for row in result:
    	if row[0] not in ret:
    		retour = retour + str(row[0]) + " | \n"
            #on ajoute a la reponse chaque valeur du tableau
    		ret.append(row[0])
    c.close()
    if not result:
        #si la valeur de la recherche n'est pas presente dans la base de donnees
        return 'This item number does not exist!'
    else:
        return template('Résultat :  <br> {{itemr}}', itemr=retour)


@route('/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./view') 

run(host='localhost', port=8080)


    

class TestServ(unittest.TestCase):
 
    def test_show_id(self):
        self.assertEqual(show_id('522938'),'This item number does not exist!')
        self.assertEqual(show_id('compak'),'Résultat :  <br> Pas de tir aux plateaux, ')


if __name__ == '__main__':
    unittest.main()
