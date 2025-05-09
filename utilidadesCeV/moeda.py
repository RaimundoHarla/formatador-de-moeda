def aumentar(preço=0, taxa=0, formato=False):
    """Retorna o preço aumentado pela taxa percentual."""
    res = preço + (preço * taxa/100)
    return res if not formato else formatar(res)


def diminuir(preço=0, taxa=0, formato=False):
    """Retorna o preço diminuído pela taxa percentual."""
    res = preço - (preço * taxa/100)
    return res if not formato else formatar(res)


def dobro(preço=0, formato=False):
    """Retorna o dobro do preço."""
    res = preço * 2
    return res if not formato else formatar(res)


def metade(preço=0, formato=False):
    """Retorna a metade do preço."""
    res = preço / 2
    return res if not formato else formatar(res)


def formatar(preço=0, moeda='R$'):
    """Formata o valor como o real."""
    return f'{moeda}{preço:.2f}'.replace('.', ',')


def resumo(preço=0, taxaau=10, taxare=5):
    """
    Exibe um resumo formatado com análises do preço:
    dobro, metade, aumento e redução percentual.
    """
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: {formatar(preço)}')
    print(f'Dobro do preço: {dobro(preço, True)}')
    print(f'Metade do preço: {metade(preço, True)}')
    print(f'{taxaau}% de aumento: {aumentar(preço, taxaau, True)}')
    print(f'{taxare}% de redução: {diminuir(preço, taxare, True)}')
    print('-' * 30)
