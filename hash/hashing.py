import hashlib
import os


def hash_pipe(file: str) -> str:
    """

    :param file: O arquivo para o qual queremos gerar o hash
    :return: A str com o identificador único gerado
    """
    # file = ".\myfile.txt"             # Location of the file (can be set a different way)
    block_size = 65536                  # The size of each read from the file

    file_hash = hashlib.sha256()        # Create the hash object, can use something other than `.sha256()` if you wish
    with open(file, 'rb') as f:         # Open the file to read it's bytes
        fb = f.read(block_size)         # Read from the file. Take in the amount declared above
        while len(fb) > 0:              # While there is still data being read from the file
            file_hash.update(fb)        # Update the hash
            fb = f.read(block_size)     # Read the next block from the file

    # print(file_hash.hexdigest())        # Get the hexadecimal digest of the hash
    return file_hash.hexdigest()


def gerar_hash(lista_arq: list, pasta: str) -> dict:
    """

    :param lista_arq: A lista de arquivos na qual iremos adicionar o hash
    :param pasta: A pasta onde estão os arquivos da lista
    :return: Um dictionary contendo nome do arquivo e hash
    """
    lista_ren = []
    # Adiciona o hash ao arquivo e devolve a lista
    for arq in lista_arq:
        chave = hash_pipe(os.path.join(pasta, arq))
        item = {'arquivo': arq, 'hash': chave}
        lista_ren.append(item)
    return lista_ren


def comparar_hashes(hash_orig: str, hash_ren: str) -> bool:
    """

    :param hash_orig: O hash original que será comparado
    :param hash_ren: O hash do arquivo que será renomeado
    :return: Bool
    """
    return hash_orig == hash_ren
