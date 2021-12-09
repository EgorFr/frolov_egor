# -- coding: utf-8 --
s = input()
sB = s[:s.find('l')]
sM = s[int(s.find('h')):int(s.rfind('l') + 1)]
sA = s[s.rfind('l') + 1:]
print(sB + sM[::-1] + sA) 