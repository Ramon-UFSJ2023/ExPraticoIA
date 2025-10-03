from collections import defaultdict


def heuristica_generica(atividades, tipo, maquinas_m):

    if tipo == 'f':
        
        maquinas = [[] for _ in range(5)]
        maquinas_indx = 0

        atividades_ordenadas = dict(sorted(atividades.items(), key=lambda item: item[1]))
        
        for atividade, tempo in atividades_ordenadas.items():

            maquinas[maquinas_indx].append(atividade, tempo)

            maquinas_indx = (maquinas_indx + 1) % 5

        return maquinas
    
    if tipo == 'm':

        maquinas = [[] for _ in range(6)]
        maquinas_indx = 0

        maquinas_ordenadas = sorted(maquinas_m.items(), key=lambda item: item[1])
        atividades_ordenadas = dict(sorted(atividades.items(), key=lambda item: item[1]))

        capacidade_restante = [cap for _, cap in maquinas_ordenadas]

        for atividade, tempo in atividades_ordenadas.items():

            tentativas = 0
            alocada = False

            while tentativas < 6:

                id_maquina = maquinas_ordenadas[maquinas_indx][0] - 1

                if capacidade_restante[id_maquina] - tempo >= 0:
                    
                    maquinas[id_maquina].append((atividade, tempo))
                    capacidade_restante[id_maquina] -= tempo
                    alocada = True
                    break

                maquinas_indx = (maquinas_indx + 1) % 6
                tentativas += 1

            if not alocada:
                print(f"Atividade {atividade} não coube em nenhuma máquina")

            maquinas_indx = (maquinas_indx + 1) % 6

        return maquinas


    
    if tipo == 'd':

        maquinas = [[] for _ in range(5)]
        maquinas_indx = 0

        atividades_ordenadas = ordenar_tarefas(atividade)

        for atividade, tempo in atividades_ordenadas.items():

            maquinas[maquinas_indx].append(atividade, tempo)

            maquinas_indx = (maquinas_indx + 1) % 5

        return maquinas



def ordenar_tarefas(tarefas):

    dict_tempo = {t: tempo for t, tempo, _ in tarefas}

    grafo = defaultdict(list)
    grau_entrada = defaultdict(int)

    for tarefa, _, dependentes in tarefas:
        for dep in dependentes:

            grafo[tarefa].append(dep)
            grau_entrada[dep] += 1

        if tarefa not in grau_entrada:
            grau_entrada[tarefa] = 0

    fila = [t for t in grau_entrada if grau_entrada[t] == 0]
    fila = sorted(fila, key=lambda t: dict_tempo[t])

    ordem = []
    while fila:

        atual = fila.pop(0)
        ordem.append(atual)

        for vizinho in grafo[atual]:

            grau_entrada[vizinho] -= 1

            if grau_entrada[vizinho] == 0:

                fila.append(vizinho)
                fila = sorted(fila, key=lambda t: dict_tempo[t])

    return ordem
