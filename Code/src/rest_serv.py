from libs.bottle import route, template, run

@route('/hello/<name>/<nom>')
def index(name, nom):
    return template('<b>Hello {{name}}</b>! <br> <b>Hello {{nom}}</b>! ', name=name, nom=nom)

run(host='infoweb', port=8080)

import _mysql
import sys

try:
    con = _mysql.connect('infoweb', 'E145425W', 'E145425W', 'E145425W')
        
    con.query("SELECT VERSION()")
    result = con.use_result()
    
    print "MySQL version: %s" % \
        result.fetch_row()[0]
    
except _mysql.Error, e:
  
    print "Error %d: %s" % (e.args[0], e.args[1])
    sys.exit(1)

finally:
    
    if con:
        con.close()