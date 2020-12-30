s = '''Player 1:
40
26
44
14
3
17
36
43
47
38
39
41
23
28
49
27
18
2
13
32
29
11
25
24
35

Player 2:
19
15
48
37
6
34
8
50
22
46
20
21
10
1
33
30
4
5
7
31
12
9
45
42
16'''

d1,d2 = [[int(y) for y in x.splitlines()[1:]] for x in s.split("\n\n")]

def play_round(d1,d2):
    if d1[0] > d2[0]:
        d1.append(d1.pop(0))
        d1.append(d2.pop(0))
    else:
        d2.append(d2.pop(0))
        d2.append(d1.pop(0))

def calc_score(deck):
    score = 0
    for i,c in enumerate(deck):
        score += (len(deck)-i)*c
    return score

while len(d1) > 0 and len(d2) > 0:
    play_round(d1,d2)

print("Part 1:")
print("P1:", calc_score(d1))
print("P2:", calc_score(d2))


# s = '''Player 1:
# 9
# 2
# 6
# 3
# 1

# Player 2:
# 5
# 8
# 4
# 7
# 10'''

d1,d2 = [[int(y) for y in x.splitlines()[1:]] for x in s.split("\n\n")]

def play_round_recurse(d1, d2):
    if len(d1) > d1[0] and len(d2) > d2[0]:
        result = play_game_recurse(d1[1:d1[0]+1],d2[1:d2[0]+1])
    else:
        result = d1[0] - d2[0]
    
    if result > 0:
        d1.append(d1.pop(0))
        d1.append(d2.pop(0))
    else:
        d2.append(d2.pop(0))
        d2.append(d1.pop(0))

def play_game_recurse(d1,d2):
    # print("New game:")
    # print("Player 1:", d1)
    # print("Player 2:", d2)
    state = set()
    
    while len(d1) > 0 and len(d2) > 0:
        if tuple(d1) in state:
            return 1
        state.add(tuple(d1))

        play_round_recurse(d1,d2)
    
    return len(d1) - len(d2)

play_game_recurse(d1,d2)

print("\nPart 2")
print("P1:", calc_score(d1))
print("P2:", calc_score(d2))