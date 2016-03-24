#!/usr/bin/python3
#-*- coding: utf-8 -*-


from libs.bottle import route, run, debug, template, request, static_file
import mysql
import mysql.connector
import sys
import urllib



@route('/api/<item>')
def show_id(item):
    retour = ""
    ret = []
    conn = mysql.connector.connect(host="infoweb", user="E145425W", password="E145425W", database="E145425W")
    c = conn.cursor()
    c.execute("SELECT e.nom FROM equipement e JOIN equip_activ ea ON e.id = ea.id_equip JOIN activite a ON ea.id_activ = a.idAct WHERE a.nom LIKE '%"+[item]+"%'") 
    result = c.fetchall()

    for row in result:
    	if row[0] not in ret:
    		retour = retour + str(row[0]) + ", "
    		ret.append(row[0])
    c.close()
    if not result:
        return 'This item number does not exist!'
    else:
        return template('Résultat :  <br> {{itemr}}', itemr=retour)

@route('/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./view')

run(host='localhost', port=8080)

