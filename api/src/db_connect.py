import json
import os
import mysql.connector

def load_config(filepath=None):
    filepath = filepath or os.path.dirname(__file__) +'/../config/configuration.json'
    with open(filepath, 'r') as config_file:
        return json.load(config_file)

def conndect_to_db(config):
    return mysql.connector.connect(
                host=config['host'],
                user=config['user'],
                password=config['password'],
                database=config['db_name'],
                port=config['port'],
                )