# Ambiente de execução do randomizador de arquivos.
import os
from arquivos.randomizar_lista_arquivos import randomizar_lista
from arquivos.renomear_arquivo import decouple_lista, renomear_arquivo, renomear_trim
from arquivos.trim_arquivo import trim_file
from hash.hashing import gerar_hash
from settings import PASTA, ARQUIVOS

if __name__ == '__main__':
    pasta = PASTA
    renomear_trim(ARQUIVOS, pasta)
    lista_arq = os.listdir(pasta)
    lista_ren = []

    # lista_teste = ['0000 Cat Power-Maybe Not.flv', '0001 David Bowie - Lets Dance.mp4', '0004 Autoramas -  - Verdugo.ogg', '0003 Alice in Chains - Down in a Hole (MTV Unplugged).mp3', '0002 Beirut -  - The Gulag Orkestar.mp3']

    # Execução
    lista_ren = gerar_hash(lista_arq, pasta)
    lista_trim = trim_file(lista_arq)
    lista_rand = randomizar_lista(lista_trim)

    # print(f'Eu sou a lista randômica! {lista_rand}')
    # print(f'Eu sou a lista original com hashes! {lista_ren}')

    for e in lista_rand.copy():
        elem = decouple_lista(lista_rand)
        ren = renomear_arquivo(lista_ren, elem, pasta)
        print(f'{e} resultou em {ren}')
