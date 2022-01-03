resp = 'Ss'
media = soma = maior = menor = c = 0

while resp in 'Ss':
    n = int(input('Digite um número: '))
    c = c + 1
    soma = n + soma
    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    resp = str(input('Quer continuar? [S/N] ').upper().strip())[0]
    if resp in 'Nn':
        media = soma / c
        print('Você digitou {} números e a média foi {:.2f}'.format(c, media))
        print('O maior número foi {} e o menor foi {}'.format(maior, menor))

