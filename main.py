import time
import funcoes_entrada as func
import facil
import medio

def main():
    #dicionario_f = func.ler("entradas/entrada_f.txt", 'f')
    #dicionario_maquinas, dicionario_tarefas = func.ler("entradas/entrada_m.txt", 'm')
    #dicionario_d = func.ler("entradas/entrada_d.txt", 'd')
    #print(dicionario_maquinas)
    #print(dicionario_tarefas)

    dicionario_maquinas, dicionario_tarefas = func.ler("entradas/entrada_m.txt", 'm')
    maquinas_capacidades = dicionario_maquinas["processamento_id"]
    tarefas_tempos = dicionario_tarefas["tempo_tarefa"]

    solucao_medio, makespan_medio = medio.gls_para_escalonamento(tarefas_tempos, maquinas_capacidades)
    medio.imprimir_resultado_formatado(solucao_medio, makespan_medio, tarefas_tempos, maquinas_capacidades)


if __name__ == "__main__":
    main()
    