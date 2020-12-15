s = '''1000340
13,x,x,x,x,x,x,37,x,x,x,x,x,401,x,x,x,x,x,x,x,x,x,x,x,x,x,17,x,x,x,x,19,x,x,x,23,x,x,x,x,x,29,x,613,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,41'''

l = s.split("\n")

earliest = int(l[0])
routes = l[1].split(",")
route_nums = [int(x) for x in routes if x.isdigit()]

wait_times = [x-(earliest % x) for x in route_nums]

pos, min_wait = min(enumerate(wait_times), key=lambda x: x[1])

print(route_nums)
print(wait_times)
print(pos, min_wait)
print(route_nums[pos] * min_wait)

route_pos = [(i,int(x)) for i,x in enumerate(routes) if x.isdigit()]
simplified = sorted([(a % b, b) for a,b in route_pos],key=lambda c: c[1],reverse=True)
print(route_pos)
print(simplified)


value = 100000000000003+44
i = 1
increment = simplified[0][1]

# simplified = [(0,67),(1,7),(2,59),(3,61)]
# simplified = [(0,17),(2,13),(3,19)]
value = 1
i = 0
increment = 1

while i < len(simplified):
    if (simplified[i][1]-(value % simplified[i][1])) % simplified[i][1] == simplified[i][0]:
        increment = increment * simplified[i][1]
        i += 1
        continue
    else:
        # print((simplified[i][1]-(value % simplified[i][1])),simplified[i][0])
        value += increment

print(value)
print([value % x[1] for x in simplified])