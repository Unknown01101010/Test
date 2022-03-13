# Test

calculator

from time import sleep


print('''

███████████████████████████████
███ Calculadora by unkwown  ███
███████████████████████████████

''')

n1 = int(input('Me diga o primeiro valor: ')) #Primeira variáveis para o usuário colocar.
n2 = int(input('Me diga o segundo valor: ')) #Segunda Variável para o usuário colocar.
n3 = 0 #Acumulador de dados
c = n1 #Variavel que possa mudar o valor de n1 dentro de um IF
f = 1 #Multiplicador para o Fatorial

while n3 != 9: #Laço de Repetiçã0
    print()
    n3 = int(input('''
    █████████████████████████████████████
    ███ [1] Soma.                     ███
    ███ [2] Subtração.                ███
    ███ [3] Multiplicação.            ███
    ███ [4] Divisão.                  ███
    ███ [5] Fatorial. (primeiro Valor)███
    ███ [6] Maior/menor que.          ███
    ███ [7] Potência.                 ███
    ███ [8] Outros números.           ███
    ███ [9] Desligar o Sistema        ███
    █████████████████████████████████████
    
    Me diga sua operação: ''')) #Terceira Variável para o usuário colocar.

    if n3 == 1: #Soma
        print()
        print('{} + {} = {}'.format(n1,n2,n1+n2))

    elif n3 == 2: #Subtração
        print()
        print('{} - {} = {}'.format(n1,n2,n1-n2))

    elif n3 == 3: #multiplicação
        print()
        print('{} * {} = {}'.format(n1,n2,n1*n2))

    elif n3 == 4: #divisão
        print()
        print('{} / {} = {}'.format(n1,n2,n1/n2))

    elif n3 == 5: #Fatorial
        print()
        while c > 0:
            print(c,end='')
            print(' x ' if c > 1 else ' = ',end='')
            f *= c
            c -= 1
        print(f,end='')

    elif n3 == 6: #maior ou menor que
        print()
        if n1 > n2:
            print('{} é maior que {}'.format(n1,n2))
        if n1 < n2:
            print('{} é menor que {}'.format(n1,n2))
        if n1 == n2:
            print('{} e {} tem valores iguais.'.format(n1,n2))

    elif n3 == 7: #potência
        print()
        print('{} ** {} = {}'.format(n1,n2,n1**n2))

    elif n3 == 8: #Colocar outros números.
        print()
        n1 = int(input('Me diga o primeiro valor: ')) #Variáveis para o usuário colocar.
        n2 = int(input('Me diga o segundo valor: ')) #Segunda Variável para o usuário colocar.

print()
print('Desligando o sistema.')
sleep(1)
print('Até mais!')
