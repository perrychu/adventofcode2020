s = '''5,2,8,16,18,0,1'''
# s = '''1,2,3'''

l = [int(x) for x in s.split(",")]

memory = {}
for i,n in enumerate(l[:-1]):
    memory[n] = i+1

prev_num = l[-1]

for i in range (len(l), 30000000):
    if prev_num in memory:
        next_num = i-memory[prev_num]
    else:
        next_num = 0

    # print(memory)
    # print(prev_num)
    # print(i,next_num)

    if i == 2019: #part 1 answer
        print(i,next_num)

    memory[prev_num]=i
    prev_num = next_num

print(prev_num)