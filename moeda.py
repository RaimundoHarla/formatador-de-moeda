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
