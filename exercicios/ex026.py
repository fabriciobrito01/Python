nome = str(input('Qual seu nome? ')).upper().strip()
print('A letra A aparece {} vezes.'.format(nome.count('A')))
print('A letra A aparece pela primeira vez na posição {}.'.format(nome.find('A')+1))
print('A letra A aparece pela últimas vez na posição {}.'.format(nome.rfind('A')+1))