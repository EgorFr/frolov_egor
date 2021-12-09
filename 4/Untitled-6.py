# -- coding: utf-8 --
s = input()
s = s[:s.find('f')] + s[s.rfind('f') + 1:]
print(s) 