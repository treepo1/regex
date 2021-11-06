import re 

URL_ARQUIVO = 'cpfs.txt'

def main(URL):
    valida_arquivo(URL)



def valida_arquivo(arquivo):
    with open(arquivo, 'r') as lista_cpfs:
        for cpf in lista_cpfs:
            valida_cpf(cpf)



def valida_cpf(cpf):
    padrao = "^[0-9]{3}[.][0-9]{3}[.][0-9]{3}[-][0-9]{2}$"
    prog = re.compile(padrao)
    validacao = prog.match(cpf)
    if validacao == None:
        print("Cpf inválido!")
    else:
        print(f"Cpf {cpf} é valido")

main(URL_ARQUIVO)