'''
Created on Aug 30, 2014

@author: lent400
'''
def square(X):
    return X*X
def cube(X):
    return square(X)*X
def quad(X):
    return cube(X)*X
def inverse(X):
    if X!=0:
        return 1.0/X