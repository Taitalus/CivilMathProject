'''
Created on Sep 4, 2014

@author: lent400
'''
import math
from CivilMathProject.Equations.MathEquations import square, cube, quad, inverse

def find_A(A1,W):
    return A1+W

def find_C(M,W,A):
    numerator=2.0*M
    denominator=(A-W)*math.pi
    return numerator/denominator

def find_D(C,P1,W,A):
    part1=square(C)
    part2=cube((P1/3.0)/((A-W)*math.pi))
    return part1-part2

def find_condition_for_K(P1,W,A):
    return cube((P1/3.0)/((A-W)*math.pi))

def find_K(D):
    D=-D
    return math.sqrt(D)

def find_condition_1(P1,A,W):
    numerator=math.pow((P1/3.0), 1.5)
    denominator=4*math.sqrt((A-W)*math.pi)
    return numerator/denominator

def find_small_f(lamba):
    numerator=1.0-math.cos(lamba)
    deno_1=(2.0/3.0)*cube(math.sin(lamba))
    deno_2=(math.sin(2*lamba)*math.cos(lamba))/2.0
    deno_3=-(lamba*math.cos(lamba))
    return math.sqrt(numerator/(deno_1+deno_2+deno_3))

def find_capital_F(lamba):
    numerator=1.0-math.cos(lamba)
    deno_1=-(2.0/3.0)*cube(math.sin(lamba))*math.cos(lamba)
    deno_2=-(quad(math.sin(lamba))/16.0)
    deno_3=lamba/4
    return math.pow((numerator/(deno_1+deno_2+deno_3)), (1.0/3.0))

def find_condition_2(A,W,lamba):
    part_1=math.sqrt(A)*math.pow((1-(math.pi*W/A*square(find_small_f(lamba)))), 1.5)
    part_2=cube(find_small_f(lamba)/find_capital_F(lamba))
    return inverse(part_1)*part_2

def check_condition(P1,M,A,lamba,W):
    part_1=(P1/A)/math.pow((M/A),(2.0/3.0))
    part_2=square(find_small_f(lamba)/find_capital_F(lamba))
    part_3=math.pi*W/A*square(find_small_f(lamba))
    return part_1*part_2+part_3

def value_from_equation_1(C,K):
    part_1=2.0*math.pow(C,(1.0/3.0))
    part_2=math.pow((1+square(K/C)),(1.0/6.0))
    part_3=math.cos(math.atan(K/C)/3.0)
    return part_1*part_2*part_3 

def value_from_equation_2(C,D):
    part_1=math.pow((C+math.sqrt(D)),(1.0/3.0))
    part_2=math.pow((C-math.sqrt(D)),(1.0/3.0))
    return part_1+part_2 

def value_from_equation_3(M,A,lamba):
    return math.pow((M/A), (1.0/3.0))*find_capital_F(lamba)
  
def find_R_Formula2(P1,W,M,A1):
    A=find_A(A1,W)
    C=find_C(M,W,A)
    D=find_D(C,P1,W,A)
    condition_for_K=find_condition_for_K(P1,W,A)
    
    if square(C)<=cube(condition_for_K):
        K=find_K(D)
    lamba=math.pi
    condition_1=find_condition_1(P1,A,W)
    condition_2=find_condition_2(A,W,lamba)
    
    if M<=condition_1:
        R=value_from_equation_1(C, K)
        equation_no=1
    elif M>condition_1 and M<=condition_2:
        R=value_from_equation_2(C, D)
        equation_no=2
    else:
        lamba=math.pi
        while(lamba>0):
            if(check_condition(P1, M, A, lamba, W)==1.0):
                break
            else:
                lamba=lamba-0.005
        R=value_from_equation_3(M, A, lamba)
        equation_no=3
        
    result={
        'R':round(R,3),
        'equation':equation_no,
        'lambda':round(lamba,3)
    }
    return result