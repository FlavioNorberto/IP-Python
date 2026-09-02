# D² = (X1 - X2)² + (Z1 - Z2)²

x = int(input())
z = int(input())

H = ((x - 34)**2 + (z - 220)**2)**(1/2)
K = ((x - 0)**2 + (z - 0)**2)**(1/2)
S = ((x - 140)**2 + (z - 456)**2)**(1/2)

print(f'Distancia para Hogsmeade: {H:.2f}')
print(f'Distancia para Kakariko: {K:.2f}')
print(f'Distancia para Solitude: {S:.2f}')


#576+44100