s = ' We are not what we should be! We are not what we need to be. But at least we are not what we used to be (Football Coach) '
l = s.strip()
s = l

print(l, '\n', l.count(" ") + 1)

while (l.find('.') > 0) or (l.find('!') > 0) or (l.find('(') > 0) or (l.find(')') > 0):
    l1 = l.find(".")
    s1 = l[0:l1]
    s2 = l[l1:]
    s = s1.strip('.') + s2.strip('.')
    l = s
    l1 = l.find('!')
    s1 = l[0:l1]
    s2 = l[l1:]
    s = s1.strip('!') + s2.strip('!')
    l = s
    l1 = l.find('(')
    s1 = l[0:l1]
    s2 = l[l1:]
    s = s1.strip('(') + s2.strip('(')
    l = s
    l1 = l.find(')')
    s1 = l[0:l1]
    s2 = l[l1:]
    s = s1.strip(')') + s2.strip(')')
    l = s
print(s)

print(*sorted(s.split()))











