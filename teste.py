import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.formatmoeda(p)} é {moeda.formatmoeda(moeda.metade(p))}')
print(f'O dobro de {moeda.formatmoeda(p)} é {moeda.formatmoeda(moeda.dobro(p))}')
print(f'Aumentando 10%, temos {moeda.formatmoeda(moeda.aumentar(p, 10))}')
print(f'Diminuindo 20%, temos {moeda.formatmoeda(moeda.diminuir(p, 20))}')
