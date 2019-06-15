from django.shortcuts import render

# Create your views here.

# coding:utf-8
import json
from django.http import HttpResponse
from django.http import JsonResponse
from config.test import read_config

def config(request):
    return_dict = {}
    a = read_config("D:\\untitled\\config\\test.ini", "my", "name")
    b = read_config("D:\\untitled\\config\\test.ini", "my", "age")
    return_dict.update(a)
    return_dict.update(b)
    print(type(return_dict))
    print(type(json.dumps(return_dict)))
    return JsonResponse(return_dict)
