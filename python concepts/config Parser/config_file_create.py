# THIS FILE IS TO USED TO CREATE AN DEFAULT CONFIG FILE WHILE RUN
# USING THE FILE OPEN METHOD WITH CONFIG WRITE FUNCTION

import configparser

config = configparser.ConfigParser()

config['DEFAULT'] = {
    'compressed': 'yes',
    'compression_ratio': '8'
}

config['setting'] = {
    'debug': 'true',
    'secret': 'XMY',
    'log_path': '/myapp/log',
    'python_v': '3',
    'package': '/usr/local'
}

config['data_base'] = {
    'db_name': 'myapp',
    'db_host': 'localhost',
    'db_port_no': '80',
    'db_port': '3000+%(data_base: db_port_no)s'
}

config['files'] = {
    'use_cdn': 'false',
    'python_path': '${setting:package}/bin/python/${setting:python_v}'
}

config.set('files', 'stored', 'no')
# the above line creates an key value pair in the files sections


with open('config.ini', 'w') as f:
    config.write(f)
