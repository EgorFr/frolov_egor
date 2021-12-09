# -- coding: utf-8 --
s = input()
if s.count('g') == 1:
    print(s.find('g'))
elif s.count('g') >= 2:
    print(s.find('g'), s.rfind('g'))