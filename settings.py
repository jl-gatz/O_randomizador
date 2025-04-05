import os
import dotenv


dotenv_file = os.path.join(".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

# PASTA = os.environ['PASTA']
PASTA = '/home/luciano/Documentos/python-randomizador-teste'
ARQUIVOS = os.listdir(PASTA)
