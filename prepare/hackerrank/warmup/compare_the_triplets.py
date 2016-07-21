import sys

a0, a1, a2 = raw_input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]

b0, b1, b2 = raw_input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]

points_a = int(a0 > b0) + int(a1 > b1) + int(a2 > b2)
points_b = int(a0 < b0) + int(a1 < b1) + int(a2 < b2)

print (points_a, points_b)




