s = '''99
151
61
134
112
70
75
41
119
137
158
50
167
60
116
117
62
82
31
3
72
88
165
34
8
14
27
108
166
71
51
42
135
122
140
109
1
101
2
77
85
76
143
100
127
7
107
13
148
118
56
159
133
21
154
152
130
78
54
104
160
153
95
49
19
69
142
63
11
12
29
98
84
28
17
146
161
115
4
94
24
126
136
91
57
30
155
79
66
141
48
125
162
37
40
147
18
20
45
55
83'''

from collections import defaultdict

l = [int(x) for x in s.split("\n")]

seq = sorted(l + [0,max(l)+3])

count = defaultdict(int)

for i in range(len(seq)-1):
    diff = seq[i+1] - seq[i]
    count[diff] = count[diff]+1
    print(seq[i],seq[i+1],diff, count)

print(seq)
print(count)

paths = defaultdict(int)
paths[0] = 1
for i in range(len(seq)):
    for j in range(i+1,len(seq)):
        if seq[j] <= seq[i]+3:
            paths[seq[j]] += paths[seq[i]]
        else:
            break

print(paths)