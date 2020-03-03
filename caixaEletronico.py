'''
Desenvolva um programa que simule a entrega de notas quando um cliente 
efetuar um saque em um caixa eletrônico. Os requisitos básicos são os 
seguintes:

Entregar o menor número de notas;
É possível sacar o valor solicitado com as notas disponíveis;
Saldo do cliente infinito;
Quantidade de notas infinito
Notas disponíveis de R$ 100,00; R$ 50,00; R$ 20,00, R$ 10,00, R$ 5,00 e 
R$ 2,00
'''

print('=' * 30)
print('{:^30}'.format('CAIXA ELETRONICO'))
print('=' * 30)
print('Notas disponiveis: 100, 50, 20, 10, 5 e 2')
saque = float(input('Valor do saque: R$ ').replace(',', '.'))
total = saque
cedula = 100
totalCedula = 0
while True:
    if total >= cedula:
        total -= cedula
        totalCedula += 1
    else:
        if totalCedula > 0:
            print(f'Total de {totalCedula} cédulas de R${cedula:.2f}')
        if cedula == 100:
            cedula = 50
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10 and total % 2 == 0:
            cedula = 2
        elif cedula == 10 and total % 2 == 1:
            cedula = 5
        totalCedula = 0
        if total == 0 or total == 1:
            break
print('=' * 30)
