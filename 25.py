s = '''12578151
5051300'''

l = [int(x) for x in s.splitlines()]

def loop(value, subject):
    v = value * subject
    v = v % 20201227
    return v

for target in l:
    value = 1
    subject = 7
    count = 0
    while value != target:
        value = loop(value,subject)
        count += 1
    print(count, value)

value = 1
for i in range(count):
    value = loop(value,l[0])
print(value)