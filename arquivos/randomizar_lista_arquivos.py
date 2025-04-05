import random


def randomizar_lista(lista: set) -> set:
    """

    :param lista: O set que já passou pelo processo de trim_arquivo
    :return: A lista (na realidade um set) com os nomes de arquivos renumerados aleatoriamente
    """
    lista_arq: set[str] = set()
    for arquivo in lista:
        novo_numero = random.randint(1, 9999)  # Gera um novo número de renumeração aleatório
        novo_nome = f'{novo_numero:04} {arquivo}'
        lista_arq.add(novo_nome)
    return lista_arq
