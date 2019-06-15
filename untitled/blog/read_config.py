from django.test import TestCase

# Create your tests here.
import configparser


def read_config(path, section, key):
    conf = configparser.ConfigParser()
    conf.read(path)
    value = conf.get(section, key)
    return {key: value}

print(read_config("D:\\untitled\\config\\test.ini", "my", "name"))

# D:\\untitled\\config\\test.ini
