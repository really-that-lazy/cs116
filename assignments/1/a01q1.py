# Question 1:
import math

def quotient(a, b):
	return a//b;

## f1: Nat, Nat -> Nat
def f1(x, y):
    return quotient((y*5)**2, x)

## f2: Nat, Nat -> Int
def f2(a, b):
    return ((a+b)**(a%10))

## f3: Nat -> Num
def f3(n):
    return ((math.sqrt(2*math.pi*n))*((n/math.e)**(n-1)))
