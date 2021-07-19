'''
[Python]
[Postgres-SQL]
Autor: Torres Molina Emmanuel O.
Version: 1.1
 
Descripcion:
Funcion que levanta los datos
de un archivo del tip .ini
Ejemplo: config.ini
'''

__author__ = "Emmanuel Torres Molina"
__email__ = "emmaotm@gmail.com"
__version__ = "1.1"

from configparser import ConfigParser


def config (section, filename='config.ini'):
    
    # Read the config file.
    parser = ConfigParser()
    parser.read(filename)

    # Read the section.
    config_params = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            config_params[param[0]] = param[1]

    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return config_params
