import funcoes_entrada as func

def calcular_makespan(solucao, tarefas_tempos, maquinas_capacidades):
    if not solucao:
        return 0

    tempos_por_maquina = []
    for i, maquina in enumerate(solucao):
        id_maquina = i + 1
        capacidade = maquinas_capacidades.get(id_maquina, 1)
        if capacidade == 0: continue

        tempo_total_maquina = sum(tarefas_tempos.get(tarefa_id, 0) / capacidade for tarefa_id in maquina)
        tempos_por_maquina.append(tempo_total_maquina)

    return max(tempos_por_maquina) if tempos_por_maquina else 0

def gerar_solucao_inicial(tarefas_tempos, maquinas_capacidades):
    num_maquinas = len(maquinas_capacidades)
    solucao = [[] for _ in range(num_maquinas)]
    tempos_maquinas = [0] * num_maquinas

    tarefas_ordenadas = sorted(tarefas_tempos.items(), key=lambda item: item[1], reverse=True)

    for tarefa_id, tempo_tarefa in tarefas_ordenadas:
        melhor_maquina = -1
        menor_tempo_resultante = float('inf')

        for i in range(num_maquinas):
            id_maquina = i + 1
            capacidade = maquinas_capacidades.get(id_maquina, 1)
            if capacidade == 0: continue

            tempo_adicional = tempo_tarefa / capacidade
            tempo_resultante = tempos_maquinas[i] + tempo_adicional

            if tempo_resultante < menor_tempo_resultante:
                menor_tempo_resultante = tempo_resultante
                melhor_maquina = i
        
        if melhor_maquina != -1:
            solucao[melhor_maquina].append(tarefa_id)
            tempos_maquinas[melhor_maquina] = menor_tempo_resultante

    return solucao

def gls_para_escalonamento(tarefas_tempos, maquinas_capacidades):
    num_maquinas = len(maquinas_capacidades)
    solucao_atual = gerar_solucao_inicial(tarefas_tempos, maquinas_capacidades)
    melhor_solucao = [list(m) for m in solucao_atual]
    melhor_custo = calcular_makespan(solucao_atual, tarefas_tempos, maquinas_capacidades)
    
    print(f"Solução Inicial com Makespan: {melhor_custo}")

    iteracao = 0
    melhoria_encontrada = True
    while melhoria_encontrada:
        iteracao += 1
        print(f"--- Iteração {iteracao} ---")
        melhoria_encontrada = False
        
        for idx_maq_origem in range(num_maquinas):
            for tarefa_id in list(solucao_atual[idx_maq_origem]):
                for idx_maq_destino in range(num_maquinas):
                    if idx_maq_origem == idx_maq_destino:
                        continue

                    vizinho = [list(maquina) for maquina in solucao_atual]
                    vizinho[idx_maq_origem].remove(tarefa_id)
                    vizinho[idx_maq_destino].append(tarefa_id)
                    
                    custo_vizinho = calcular_makespan(vizinho, tarefas_tempos, maquinas_capacidades)
                    
                    if custo_vizinho < melhor_custo:
                        melhor_solucao = vizinho
                        melhor_custo = custo_vizinho
                        solucao_atual = [list(m) for m in melhor_solucao]
                        melhoria_encontrada = True
                        print(f"Melhoria! Movendo tarefa {tarefa_id} da máquina {idx_maq_origem+1} para {idx_maq_destino+1}. Novo Makespan: {melhor_custo}")
                        break
                if melhoria_encontrada:
                    break
            if melhoria_encontrada:
                break

    return melhor_solucao, melhor_custo

def imprimir_resultado_formatado(solucao, makespan, tarefas_tempos, maquinas_capacidades):
    print("\n--- RESULTADO FINAL ---")
    print("a) Atribuição final de tarefas às máquinas:")
    for i, maquina in enumerate(solucao):
        id_maquina = i + 1
        capacidade = maquinas_capacidades.get(id_maquina, 1)
        tempo_total = sum(tarefas_tempos.get(tarefa_id, 0) / capacidade for tarefa_id in maquina) if capacidade > 0 else 0
        print(f"   - Máquina {id_maquina} (Capacidade: {capacidade}): {sorted(maquina)} (Tempo Total: {tempo_total:.2f})")
    print(f"\nb) Valor final do makespan: {makespan:.2f}")