
# -*- coding: utf-8 -*-

scores = (30, 45, 60, 80, 20)

def failed(score):
    return score < 60
    
# �D�X�Q���� 
sf = filter(failed, scores)

for s in sf:
    print(s)

#### �վ���ơA�}�ڸ����H�Q

def adjust(score):
    from math import sqrt
    
    return sqrt(score) * 10
    
print('')
for s in filter(failed, map(adjust, scores)):
    print(s)

#### �O�d����ƻP�վ�᪺����
print('')

for so, sn in filter(lambda item: item[1] < 60, zip(scores, map(adjust, scores))):
    print(so, sn)

