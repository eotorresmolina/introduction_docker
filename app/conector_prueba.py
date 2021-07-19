'''
[Python]
[Postgres-SQL]
Autor: Torres Molina Emmanuel O.
Version: 1.1
 
Descripcion:
Ejemplo para probar lo conexión a una
DDBB de PostgresSQL y a su vez para probar
el funcionamiento de los containers en Docker.
'''

__author__ = "Emmanuel Torres Molina"
__email__ = "emmaotm@gmail.com"
__version__ = "1.1"


import psycopg2
import os
from config import config


scriptdir = os.path.dirname(os.path.realpath(__file__))
filename = 'config.ini'
filedir_config = os.path.join(scriptdir, filename)

# Obtengo los parámetros para realizar la
# conexión con la Base de Datos.
param = config(section='server', filename=filedir_config)
host = param['host']
port = param['port']

# Obtengo los parámetros para realizar la
# conexión a la Base de Datos.
param_db = config(section='db', filename=filedir_config)
user = param_db['user']
pswrd = param_db['password']

# Realizo la conexión.
conn = psycopg2.connect(host=host, port=port, user=user, password=pswrd)

c = conn.cursor()   # Obtengo el cursor.

query = '''
            SELECT *
            FROM table_test;
        '''

c.execute(query)

results_query = c.fetchall()
c.close()
conn.close()

print('\nLos registros devueltos por la query son:\n {}'.format(results_query))

print('\nVisualizandolos mejor:')
print('(id, language, framework, version)')
for registro in results_query:
    print(registro)
print('\n')

