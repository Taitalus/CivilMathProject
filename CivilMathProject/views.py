'''
Created on Aug 16, 2014

@author: lent400
'''
import MathEquations
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.utils import simplejson
from django.http.response import HttpResponse
def home(request):
    return render_to_response('index_new.html',{},context_instance=RequestContext(request))

def Calculate(request):
    if request.method=="GET":
        P1=request.GET['P1']
        W=request.GET['W']
        MX=request.GET['MX']
        MY=request.GET['MY']
        A1=request.GET['A1']
        R=request.GET['R']
        print P1
        print W
        print MX
        print MY
        print A1
        print R 
        
        L=MathEquations.find_L(float(P1),float(W),float(MX),float(MY),float(A1),float(R))
                
        message=simplejson.dumps(L)
        return HttpResponse(message,mimetype='application/json')    