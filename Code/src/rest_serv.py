#!/usr/bin/python3
#-*- coding: utf-8 -*-


from libs.bottle import route, run, debug, template, request
import mysql
import mysql.connector
import sys
import urllib



@route('/<item>')
def show_id(item):
    conn = mysql.connector.connect(host="infoweb", user="E145425W", password="E145425W", database="E145425W")
    c = conn.cursor()
    print("select id_equip from equip_activ where id_activ = (SELECT idAct FROM activite WHERE nom = '"+str(item)+"' )")


    c.execute("select id_equip froSELECT idAct FROM activite WHERE nom = '"+str(item)+"' )") 
    result = c.fetchall()



    for row in result : 
    	c.execute("""select nom from equipement where id = """+str(row))
    	
    	tab = c.fetchall()

    c.close()
    if not result:
        return 'This item number does not exist!'
    else:
        return template('<b>Résultat : {{itemr}}</b>!', itemr=tab[0])


run(host='localhost', port=8080)