'''
Created on Aug 16, 2014

@author: lent400
'''
import CivilMathProject.Equations.Formula1 as Formula1
from django.shortcuts import render_to_response
from django.template.context import RequestContext
import simplejson
from django.http.response import HttpResponse
from CivilMathProject.Equations import Formula2
def home(request):
    return render_to_response('index_new.html',{},context_instance=RequestContext(request))
def formula1(request):
    return render_to_response('formula-01.html',{},context_instance=RequestContext(request))
def formula2(request):
    return render_to_response('formula-02.html',{},context_instance=RequestContext(request))
def formula3(request):
    return render_to_response('formula-03.html',{},context_instance=RequestContext(request))	
def CalculateFormula1(request):
    if request.method=="GET":
        P1=request.GET.get(u'P1','')
        W=request.GET.get(u'W','')
        MX=request.GET.get(u'MX','')
        MY=request.GET.get(u'MY','')
        A1=request.GET.get(u'A1','')
        R=request.GET.get(u'R','')
        P1=unicode(P1)
        W=unicode(W)
        MX=unicode(MX)
        MY=unicode(MY)
        A1=unicode(A1)
        R=unicode(R) 
        
        L=Formula1.find_L_formula1(float(P1),float(W),float(MX),float(MY),float(A1),float(R))
                
        message=simplejson.dumps(L)
        return HttpResponse(message,content_type='application/json')    
    
def CalculateFormula2(request):
    if request.method=="GET":
        P1=request.GET.get(u'P1','')
        W=request.GET.get(u'W','')
        M=request.GET.get(u'M','')
        A1=request.GET.get(u'A1','')
        P1=unicode(P1)
        W=unicode(W)
        M=unicode(M)
        A1=unicode(A1)
        
        R=Formula2.find_R_Formula2(float(P1), float(W), float(M), float(A1))
                
        message=simplejson.dumps(R)
        return HttpResponse(message,content_type='application/json')    