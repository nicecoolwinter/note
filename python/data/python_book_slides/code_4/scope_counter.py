
# -*- coding: utf-8 -*-

def counter(n):
    li = [n]
    def bar(x):
        li[0] += x           # �bbar�̡A��a�ק�counter��li
        return li[0]
    return bar               # counter�^�ǡu�禡�v
    
c0 = counter(0)              # �W��c0�Pc100�����V�禡����
c100 = counter(100)

print(c0(1))         # �L�X1
print(c100(10))      # �L�X110

print(c0(1))         # �L�X2
print(c0(3))         # �L�X5
print(c100(20))      # �L�X130

####
print()

def counter(n):
    def bar(x):
        nonlocal n
        n += x   
        return n
    return bar 
    
c0 = counter(0) 
c100 = counter(100)
print(c0(1))         # �L�X1
print(c100(10))      # �L�X110
print(c0(1))         # �L�X2
print(c0(3))         # �L�X5
print(c100(20))      # �L�X130

