
# -*- coding: utf-8 -*-

def fib_memo():
    memo = {0: 0, 1: 1}
    def sub(n):
        if n not in memo: 
            memo[n] = sub(n-1) + sub(n-2) 
        return memo[n]
    return sub
fib_m = fib_memo()

def odd(n): return n%2 != 0

def odd_fibs(n):
    r = range(0, n+1)
    
    return filter(lambda x: x[1]%2 != 0, zip(r, map(fib_m, r)))
    
#
for item in odd_fibs(10):
    print(item)
    
# print�ǤJmap�A�L�@��
def show(n):
    map(print, odd_fibs(n))
show(10)

# �]��map�O���N��
print('')

list(map(print, odd_fibs(10)))

# ���n���g�k�G�B��print
print('')

print(*odd_fibs(10), sep='\n')


# ��Jlist

def odd_fibs(n):
    r = range(0, n+1)
    return list(filter(lambda x: x[1]%2 != 0, zip(r, map(fib_m, r))))
    
print('')
print(odd_fibs(10))

# ��Jlist�A�ϥ�reduce
from functools import reduce

def odd_fibs(n):
    r = range(0, n+1)
    return reduce(lambda x, y: x + [y],
                  filter(lambda x: x[1]%2 != 0, 
                         zip(r, 
                             map(fib_m, r))),
                  [])
    
print('')
print(odd_fibs(10))
