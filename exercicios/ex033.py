n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
n3 = float(input('Digite um último número: '))
maior = 0
menor = 0
if n1 > n2 and n1 > n3:
    maior = n1
if n1 < n2 and n1 < n3:
    menor = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n2 < n1 and n2 < n3:
    menor = n2
if n3 > n1 and n3 > n2:
    maior = n3
if n3 < n1 and n3 < n2:
    menor = n3
print(f'O maior numero é {maior:.1f} e o menor número é {menor:.1f}.')