from django.test import TestCase

# Create your tests here.
import configparser
import json

def read_config(path, section, key):
    conf = configparser.ConfigParser()
    conf.read(path)
    value = conf.get(section, key)
    return {key: value}

# print(read_config("D:\\untitled\\config\\test.ini", "my", "name"))

# D:\\untitled\\config\\test.ini


a = '{"name": "susu", "age": "18", ad: 29}'
b = json.loads(a)
print(b)
print(type(b))
# print(a['name'])