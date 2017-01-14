
# -*- coding: utf-8 -*-

def sq(n): return n**2
def even(n): return n%2 == 0

def sq_even(n):
    return map(sq, filter(even, range(1, n)))

# 1��10�������ƥ���A�ۥ[�᪺�`�M    
print(sum(sq_even(10)))

# �ϥ�sum
def sum_sq_even(n):
    return sum(
               map(sq, 
                   filter(even, 
                       range(1, n))))
print(sum_sq_even(10))

# �ϥ�reduce
from functools import reduce
from operator import add
def sum_sq_even(n):
    return reduce(add,
               map(sq, 
                   filter(even, 
                       range(1, n))))
                       
print(sum_sq_even(10))

# �ϥβ��;��B�⦡
print(sum(n**2 for n in range(1, 10) if n%2 == 0))

