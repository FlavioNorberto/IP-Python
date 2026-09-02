A = int(input())
L = int(input())
P = int(input())
H = int(input())

X = (A + L + abs(A - L)) / 2
Y = (X + P + abs(X - P)) / 2

M = Y*H

print(f'{M:.0f}')