s = '''...#..#.
.....##.
##..##.#
#.#.##..
#..#.###
...##.#.
#..##..#
.#.#..#.'''

# s = '''.#.
# ..#
# ###'''

from collections import defaultdict

def initialize_3d(string):
    for y,line in enumerate(s.splitlines()):
        for x,char in enumerate(line):
            if char == "#":
                state[(0,y,x)] = 1
            else:
                state[(0,y,x)] = 0

def initialize_4d(string):
    for y,line in enumerate(s.splitlines()):
        for x,char in enumerate(line):
            if char == "#":
                state[(0,0,y,x)] = 1
            else:
                state[(0,0,y,x)] = 0

def check_cell(coord):
    if coord in state:
        return state[coord]
    else:
        return 0

#generalized for n dimensions
def activate_neighbors(coord, accum=[]):
    if len(coord) == 0:
        state[tuple(c for c in accum)]
    else:
        for ci in range(coord[0]-1,coord[0]+2):
            a = accum.copy()
            a.append(ci)
            activate_neighbors(coord[1:], a)

    # z,y,x = coord
    # for xi in range(x-1,x+2):
    #     for yi in range(y-1,y+2):
    #         for zi in range(z-1,z+2):
    #             state[(zi,yi,xi)]

def count_neighbors_3d(coord):
    z,y,x = coord
    count = 0
    for zi in range(z-1,z+2):
        for yi in range(y-1,y+2):
            for xi in range(x-1,x+2):
                if (xi != x) or (yi != y) or (zi != z):
                    count += check_cell((zi,yi,xi))
    return count

def count_neighbors_4d(coord):
    w,z,y,x = coord
    count = 0
    for wi in range(w-1,w+2):
        for zi in range(z-1,z+2):
            for yi in range(y-1,y+2):
                for xi in range(x-1,x+2):
                    if (xi != x) or (yi != y) or (zi != z) or (wi != w):
                        count += check_cell((wi,zi,yi,xi))
    return count

def print_state_3d(state):
    cells = sorted(state.keys())

    minx, miny, minz = 0,0,0
    maxx, maxy, maxz = 0,0,0
    for cz, cy, cx in cells:
        minz = min(minz, cz)
        miny = min(miny, cy)
        minx = min(minx, cx)
        maxz = max(maxz, cz)
        maxy = max(maxy, cy)
        maxx = max(maxx, cx)

    print("***")
    print("mins:",minz, miny, minx)
    print("maxs:",maxz, maxy, maxx)
    print("actives:",len(cells))
    print("***")

    line = []
    for zi in range(minz, maxz+1):
        print("\nz = ",zi)
        for yi in range(miny, maxy+1):
            for xi in range(minx, maxx+1):
                line.append(str(check_cell((zi,yi,xi))))
            print("".join(line))
            line = []

    print("".join(line))
    print()

def print_state_4d(state):
    cells = sorted(state.keys())

    minx, miny, minz, minw = 0,0,0,0
    maxx, maxy, maxz, maxw = 0,0,0,0
    for cw, cz, cy, cx in cells:
        minw = min(minw, cw)
        minz = min(minz, cz)
        miny = min(miny, cy)
        minx = min(minx, cx)
        maxw = max(maxw, cw)
        maxz = max(maxz, cz)
        maxy = max(maxy, cy)
        maxx = max(maxx, cx)

    print("***")
    print("mins:",minw, minz, miny, minx)
    print("maxs:",maxw, maxz, maxy, maxx)
    print("actives:",len(cells))
    print("***")

    line = []
    for wi in range(minw, maxw+1):
        for zi in range(minz, maxz+1):
            print("\nw = ", wi, "z = ", zi)
            for yi in range(miny, maxy+1):
                for xi in range(minx, maxx+1):
                    line.append(str(check_cell((wi,zi,yi,xi))))
                print("".join(line))
                line = []

    print("".join(line))
    print()

state = defaultdict(int)
initialize_3d(s)
print(state)
print_state_3d(state)

for cycle in range(6):
    #activate neighbors of alive cells
    for cell in [x for x in state.keys()]:
        activate_neighbors(cell)

    new_state = defaultdict(int)
    #check all active cells, save alive cells in new iteration
    for cell in state:
        count = count_neighbors_3d(cell)
        if state[cell] == 0 and count == 3:
            new_state[cell] = 1
        elif state[cell] == 1 and count >= 2 and count <= 3:
            new_state[cell] = 1

    state = new_state
    # print_state_3d(state)

print(len(state))


state = defaultdict(int)
initialize_4d(s)
print(state)
print_state_4d(state)

for cycle in range(6):
    print("starting cycle", cycle)

    #activate neighbors of alive cells
    for cell in [x for x in state.keys()]:
        activate_neighbors(cell)

    new_state = defaultdict(int)
    #check all active cells, save alive cells in new iteration
    for cell in state:
        count = count_neighbors_4d(cell)
        if state[cell] == 0 and count == 3:
            new_state[cell] = 1
        elif state[cell] == 1 and count >= 2 and count <= 3:
            new_state[cell] = 1

    state = new_state
    # print_state_4d(state)

print(len(state))

