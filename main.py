import time
import funcoes_entrada as func
import facil

def main():
    #dicionario_f = func.ler("entradas/entrada_f.txt", 'f')
    dicionario_maquinas, dicionario_tarefas = func.ler("entradas/entrada_m.txt", 'm')
    #dicionario_d = func.ler("entradas/entrada_d.txt", 'd')
    print(dicionario_maquinas)
    print(dicionario_tarefas)

    #facil.main()

if __name__ == "__main__":
    main()
    