s = "685974213"
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

def move(cups, index):
    cups, index, held = pickup(3, cups, index)
    print("holding", held, "remaining:", cups)
    print("current cup:", cups[index], "at index:", index)
    dest_index = get_dest_index(cups, index, held)
    print("inserting", held, "after", cups[dest_index], "at index:", dest_index)
    cups, index = insert(cups, index, dest_index, held)
    index += 1
    if index >= len(cups):
        index = 0
    return cups, index

for i in range(100):
    print("cups:",cups)
    print("current cup:", cups[index], "at index:", index)
    cups, index = move(cups,index)


print(cups)
print("current:", cups[index], "@", index)

first = cups.index(1)
print("Part 1:")
print("".join(map(str,cups[first+1:] + cups[:first])))