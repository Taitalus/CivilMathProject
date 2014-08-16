'''
Created on Aug 16, 2014

@author: lent400
'''
from django.shortcuts import render
def home(request):
    return render(request,'index.html',{})