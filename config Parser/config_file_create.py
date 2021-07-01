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
    'db_port': '3000'
}

config['files'] = {
    'use_cdn': 'false',
    'python_path': '${setting:package}/bin/python/${setting:python_v}'
}

config.set('files', 'stored', 'no')


with open('config.ini', 'w') as f:
    config.write(f)
