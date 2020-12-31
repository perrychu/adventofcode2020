s = "685974213"
# s = "389125467"
moves = 100
cups = [int(i) for i in s]
index = 0

def pickup(n, cups, index):
    i = index+1
    held = []
    pop_front = False
    for c in range(n):
        if i < len(cups):
            held.append(cups.pop(i))
        else:
            i = 0
            held.append(cups.pop(i))
            pop_front = True

        if pop_front:
            index -= 1
    
    return cups, index, held

def get_dest_index(cups, index, held):
    dest_val = cups[index] - 1
    if dest_val < 1:
        dest_val = max(cups)
    while dest_val in held:
        dest_val -= 1
        if dest_val < 1:
            dest_val = max(cups)

    return cups.index(dest_val)

def insert(cups, index, insert_index, held):
    if insert_index < index:
        index += len(held)
    return (cups[:insert_index+1] + held + cups[insert_index+1:]), index

def move(cups, index, debug=False):
    cups, index, held = pickup(3, cups, index)
    if debug:
        print("holding", held, "remaining:", cups)
        print("current cup:", cups[index], "at index:", index)
    dest_index = get_dest_index(cups, index, held)
    if debug:
        print("inserting", held, "after", cups[dest_index], "at index:", dest_index)
    cups, index = insert(cups, index, dest_index, held)
    index += 1
    if index >= len(cups):
        index = 0
    return cups, index

debug = False
for i in range(moves):
    if debug:
        print("cups:",cups)
        print("current cup:", cups[index], "at index:", index)
    cups, index = move(cups, index, debug)


print(cups)
print("current:", cups[index], "@", index)

first = cups.index(1)
print("Part 1:")
print("".join(map(str, cups[first+1:] + cups[:first])))




def pickup_dict(n, cups, current):
    held = []
    next = cups[current]
    for _ in range(n):
        held.append(next)
        next = cups[next]
    cups[current] = next
    return cups, held

def get_dest_dict(current, held):
    dest_val = current - 1
    if dest_val < 1:
        dest_val = max(cups.keys())
    while dest_val in held:
        dest_val -= 1
        if dest_val < 1:
            dest_val = max(cups.keys())
    return dest_val

def insert_dict(cups, after_val, held):
    next = cups[after_val]
    cups[after_val] = held[0]
    cups[held[-1]] = next

def move_dict(cups, current, debug=False):
    if debug:
        print("current cup:", current)
    cups, held = pickup_dict(3, cups, current)
    dest_val = get_dest_dict(current, held)
    if debug:
        print("inserting", held, "after", dest_val)
    insert_dict(cups, dest_val, held)

    current = cups[current]

    return cups, current

def print_dict(cups, current):
    l = []
    for _ in range(len(cups)):
        l.append(current)
        current = cups[current]
    return l

debug = False
moves = 10000000
cups = {x:x+1 for x in range(1,1000001)}
recorded = [int(x) for x in s]
for i in range(len(recorded)-1):
    cups[recorded[i]] = recorded[i+1]
cups[recorded[i+1]] = len(recorded)+1
cups[len(cups)] = recorded[0]

# debug = True
# s = "389125467"
# recorded = [int(x) for x in s]
# cups = {recorded[i]:recorded[i+1] for i in range(len(recorded)-1)}
# cups[recorded[-1]] = recorded[0]

current = recorded[0]

# print("starting numbers:", recorded)
# for x in range(1,13):
#     print(x, cups[x])
# for x in range(999996,1000001):
#     print(x,cups[x])

for i in range(moves):
    if debug:
        print("cups:",print_dict(cups, current))
    cups, current = move_dict(cups, current, debug)

print("Part 2:")
print("1", cups[1], cups[cups[1]])
print(cups[1] * cups[cups[1]])