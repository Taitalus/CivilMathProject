'''
Created on Aug 30, 2014

@author: lent400
'''
import math
from CivilMathProject.Equations.MathEquations import *

def find_beta(MX,MY):
    return math.atan(MX/MY)

def find_meu(R):
    return math.atan(R)

def find_t(beta):
    temp1=math.tan(beta)
    temp2=1.0/temp1
    return (temp1+temp2)

def find_g(beta,meu):
    return (math.sin(beta)*math.sin(meu)/math.cos(beta-meu))

def find_h(beta,meu):
    return (math.cos(beta)*math.cos(meu)/math.cos(beta-meu))

def find_q(beta,meu):
    if((beta+meu)*180/math.pi<=90):
        return (math.sin(meu)/(math.cos(beta)*math.cos(beta-meu)))
    else:
        return (math.cos(meu)/(math.sin(beta)*math.cos(beta-meu)))

def find_u(beta,meu):
    return (math.sin(meu)*math.cos(meu)/square((1/math.cos(beta-meu))))

def find_i(q,g,t):
    i=q/12.0
    i=i-((q/2.0)*g)
    i=i+((q+(t/4.0))*square(g))
    i=i-(2.0*((q+t)*cube(g))/3.0)
    i=i+((t/2.0)*quad(g))
    return i

def find_m(u,i):
    return (u/(2.0*i))

def find_a(A1,W):
    return (A1+W)

def find_M(MX,MY):
    return math.sqrt((square(MX))+(square(MY)))

def find_c(m,M,W,a,u):
    c=(m*M)/2.0
    temp=(1.0-(W/a))*u*a
    c=c/temp
    return c
    
def find_D(C,P1,W,a,u):
    numerator=P1/3.0
    denominator=((1.0-(W/a))*u*a)
    temp=cube((numerator/denominator))
    D=square(C)-temp
    return D

def find_K(D):
    D=-D
    return math.sqrt(D)

def find_small_f(lamba,t,g,q,h):
    numerator=lamba;
    deno_part1=t*((-(cube(lamba))/6.0)+(square(lamba)/2.0))
    deno_part2=(q*(-g+h))+(t*((square(g)/2.0)-h+(square(h)/2.0)))*lamba
    deno_part3=(q*((square(g)/2.0)-(square(h)/2.0)))+(t*(-(cube(g)/3.0)+(square(h)/2.0)-(cube(h)/3.0)))
    denominator=deno_part1+deno_part2+deno_part3
    return math.sqrt(numerator/denominator)

def find_capital_F(lamba,t,g,q,h):
    numerator=lamba
    deno_part1=t*((quad(lamba)/12.0)-(cube(lamba)/4.0)+(square(lamba)/4.0))
    deno_part2=lamba*((q*((square(g)/2.0)-(g/2.0)+(h/2.0)-(square(h)/2.0)))+(t*(-(cube(g)/3.0)+(square(g)/4.0)-(h/2.0)+(3.0*square(h)/4.0)-(cube(h)/3.0))))
    deno_part3=(q*(-(cube(g)/3.0)+(square(g)/4.0)-(square(h)/4.0)+(cube(h)/3.0))+t*((quad(g)/4.0)-(cube(g)/6.0)+(square(h)/4.0)-(cube(h)/2.0)+(quad(h)/4.0)))
    number=numerator/(deno_part1+deno_part2+deno_part3)
    return math.pow(number, (1/3.0))
    
def equation_two_for_small_f(lamba,t,g,q):
    numerator=lamba
    deno_part1=(q/2.0)*square(lamba)
    deno_part2=lamba*((square(g)*t/2.0)-(g*q))
    deno_part3=(-(cube(g)*t/3.0)+(square(g)*q/2.0))
    number=numerator/(deno_part1+deno_part2+deno_part3)
    return math.sqrt(number)

def equation_two_for_capital_F(lamba,t,g,q):
    numerator=lamba
    deno_part1=(-q/6.0)*cube(lamba)
    deno_part2=(q/4.0)*square(lamba)
    deno_part3=lamba*((-cube(g)*t/3.0)+(square(g)*q/2.0)+(square(g)*t/4.0)-(g*q/2))
    deno_part4=((quad(g)*t/4.0)-(cube(g)*q/3.0)-(cube(g)*t/6.0)+(square(g)*q/4))
    number=numerator/(deno_part1+deno_part2+deno_part3+deno_part4)
    return math.pow(number, (1/3.0))

def equation_three_for_small_f(lamba,t):
    numerator=6.0*lamba
    denominator=t*cube(lamba)
    return math.sqrt(numerator/denominator)

def equation_three_for_capital_F(lamba,t):
    numertor=12.0*lamba
    denominator=t*(-quad(lamba)+cube(lamba))
    return math.pow((numertor/denominator),1/3.0)
    
def find_condition_1(P1,m,a,W,u):
    numerator=math.pow(P1/3.0,(3.0/2.0))*2.0/m
    denominator=math.sqrt((a-W)*u)
    return (numerator/denominator)

def find_condtion_2(P1,a,u,W,lamba,t,g,q,h):
    small_f_of_lamba=find_small_f(lamba,t,g,q,h)
    capital_f_of_lamba=find_capital_F(lamba, t, g, q, h)
    
    numerator=math.pow(P1,(3.0/2.0))*cube(small_f_of_lamba)
    denominator=math.sqrt(a)* math.pow((1-(u*W*square(small_f_of_lamba)/a)),(3.0/2.0))*cube(capital_f_of_lamba)
    return (numerator/denominator)
    
def test_condition(P1,a,M,u,W,small_f,capital_F):
    part_1_numerator=P1/a*square(small_f)
    part_1_denominator=math.pow((M/a), (2.0/3.0))*square(capital_F)
    part_1=part_1_numerator/part_1_denominator
    part_2=(u*W*square(small_f)/a)
    if(math.floor(part_1+part_2)==1):
        return capital_F
    else:
        return False
    
def from_equation_1(C,K):
    numerator= 2.0*(pow(C,(1/3.0)))*(pow((1.0+(square(K)/square(C))),(1.0/6.0)))*math.cos(math.atan(K/C)/3.0)
    return numerator

def from_equation_2(C, D):
    part1=math.pow((C+math.sqrt(D)),1/3.0)
    part2=math.pow((C-math.sqrt(D)),1/3.0)
    return part1+part2

def from_equation_3(M,a,capital_F):
    return math.pow((M/a), (1/3.0))*capital_F    
    
def find_condition_for_k(P1,W,a,u):
    numerator=(P1/3.0)
    denominator=(1-(W/a))*u*a
    return math.pow((numerator/denominator),3.0)
    
def find_L_formula1(P1,W,MX,MY,A1,R):
    print P1
    print W
    print MX
    print MY
    print A1
    print R 
    
    #finding the necessary things needed for the calculation
    beta=find_beta(MX, MY)
    meu=find_meu(R)
    t=find_t(beta)
    
    if((beta+meu)*180/math.pi<=90):
        g=find_g(beta, meu)
        h=find_h(beta, meu)
        condition_of_angle=1
    else:
        g=find_h(beta, meu)
        h=find_g(beta,meu)
        condition_of_angle=2
    q=find_q(beta, meu)
    u=find_u(beta, meu)
    i=find_i(q, g, t)
    m=find_m(u, i)
    
    a=find_a(A1, W)
    M=find_M(MX, MY)
    
    C=find_c(m, M, W, a, u)
    D=find_D(C, P1, W, a, u)
    condition_for_k=find_condition_for_k(P1,W,a,u)
    if square(C)<=condition_for_k:
        K=find_K(D)
    
    #find the condition Criteria
    value_of_lamba=1.0
    condition_1=find_condition_1(P1,m,a,W,u)
    condition_2=find_condtion_2(P1,a,u,W,value_of_lamba,t,g,q,h) #value of lambda

    #Logic Part Starts here
    if (M <= condition_1):
        L=from_equation_1(C,K)
        equation_no="1"
    elif M>condition_1 and M<=condition_2:
        L=from_equation_2(C, D)
        equation_no="2"
    else:
        lamba=1.0
        while lamba>0:
            print lamba
            if lamba<=1.0 and lamba>h:
                small_f_of_lambda=find_small_f(lamba, t, g, q, h)
                capital_f_of_lambda=find_capital_F(lamba, t, g, q, h)
            if lamba<=h and lamba>g:
                small_f_of_lambda=equation_two_for_small_f(lamba, t, g, q)
                capital_f_of_lambda=equation_two_for_capital_F(lamba, t, g, q)
            if lamba<=g and lamba>0:
                small_f_of_lambda=equation_three_for_small_f(lamba, t)
                capital_f_of_lambda=equation_three_for_capital_F(lamba, t)
            
            capital_F=test_condition(P1, a, M, u, W, small_f_of_lambda, capital_f_of_lambda)
            
            if capital_F==False:
                if lamba>h and round((lamba-0.005),3)<=h:
                    lamba=h
                elif lamba>g and round((lamba-0.005),3)<=g:
                    lamba=g
                else:
                    lamba=round((lamba-0.005),3)
            else:
                if lamba<=1.0 and lamba>h:
                    value_of_lamba=lamba
                    equation_no=3.1
                if lamba<=h and lamba>g:
                    value_of_lamba=lamba
                    equation_no=3.2
                if lamba<=g and lamba>0:
                    value_of_lamba=lamba
                    equation_no=3.3
                break
        L=from_equation_3(M,a,capital_F)    
        print value_of_lamba
        print equation_no
    print L
    L=round(L,3)
    result={
            'L':L,
            'lambda':value_of_lamba,
            'equation':equation_no,
            'condition':condition_of_angle
    }
    return result