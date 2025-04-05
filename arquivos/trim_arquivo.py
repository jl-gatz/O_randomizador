import re


def trim_file(lista: set) -> set:
    """
    :type lista: object
    :param lista: A lista que queremos reordenar
    :return: Um set sem numeração no início dos arquivos
    """
    novo: set[str] = set()
    for arquivo in lista:
        nome_arquivo, extensao = arquivo.rsplit('.', 1)
        nome_arquivo = re.sub(r'^\d+', '', nome_arquivo).lstrip()
        novo_arquivo = f'{nome_arquivo}.{extensao}'
        novo.add(novo_arquivo)

    return novo
