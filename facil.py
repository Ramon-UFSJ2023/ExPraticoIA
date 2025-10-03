import time
import funcoes_entrada as func
import gls

# --------------------------------------------------------------------------
# FUNÇÕES DO ALGORITMO
# --------------------------------------------------------------------------

def calcular_makespan(solucao, tarefas_tempos):
    """
    Calcula o makespan (custo) de uma solução.
    """
    if not solucao: return 0
    tempos_por_maquina = [sum(tarefas_tempos.get(tarefa_id, 0) for tarefa_id in maquina) for maquina in solucao]
    return max(tempos_por_maquina) if tempos_por_maquina else 0

# <-- ALTERADO: A função agora implementa a heurística SPT (Shortest Processing Time)
def gerar_solucao_inicial_spt(tarefas_tempos, num_maquinas):
    """
    Gera uma solução inicial usando a heurística SPT (Shortest Processing Time).
    Ordena as tarefas da mais rápida para a mais demorada.
    """
    # Ordena as tarefas por tempo, da MENOR para a MAIOR
    # A única mudança foi remover o 'reverse=True'
    tarefas_ordenadas = sorted(tarefas_tempos.items(), key=lambda item: item[1]) # <-- ALTERADO

    solucao = [[] for _ in range(num_maquinas)]
    tempos_maquinas = [0] * num_maquinas
    for tarefa_id, tempo in tarefas_ordenadas:
        # Encontra a máquina com a menor carga atual
        idx_maquina_livre = min(range(num_maquinas), key=lambda i: tempos_maquinas[i])
        
        # Atribui a tarefa a essa máquina
        solucao[idx_maquina_livre].append(tarefa_id)
        tempos_maquinas[idx_maquina_livre] += tempo
        
    return solucao

def gls_para_escalonamento(tarefas_tempos, num_maquinas):
    """
    Executa a Busca Local Gulosa para o problema de escalonamento.
    """
    # 1. Geração da Solução Inicial com SPT (conforme solicitado)
    solucao_atual = gerar_solucao_inicial_spt(tarefas_tempos, num_maquinas) # <-- ALTERADO
    melhor_solucao = solucao_atual
    melhor_custo = calcular_makespan(solucao_atual, tarefas_tempos)
    
    print(f"Solução Inicial (SPT) com Makespan: {melhor_custo}") # <-- ALTERADO

    iteracao = 0
    melhoria_encontrada = True
    while melhoria_encontrada:
        iteracao += 1; print(f"\n--- Iteração {iteracao} ---"); melhoria_encontrada = False
        for idx_maq_origem in range(num_maquinas):
            for tarefa_id in solucao_atual[idx_maq_origem][:]:
                for idx_maq_destino in range(num_maquinas):
                    if idx_maq_origem == idx_maq_destino: continue
                    vizinho = [list(maquina) for maquina in solucao_atual]
                    vizinho[idx_maq_origem].remove(tarefa_id)
                    vizinho[idx_maq_destino].append(tarefa_id)
                    custo_vizinho = calcular_makespan(vizinho, tarefas_tempos)
                    if custo_vizinho < melhor_custo:
                        melhor_solucao = vizinho; melhor_custo = custo_vizinho; melhoria_encontrada = True
                        print(f"Melhoria encontrada! Movendo tarefa {tarefa_id} da máquina {idx_maq_origem} para {idx_maq_destino}.")
                        print(f"Novo Makespan: {melhor_custo}")
                        solucao_atual = melhor_solucao
                        break
                if melhoria_encontrada: break
            if melhoria_encontrada: break
    return melhor_solucao, melhor_custo

def imprimir_resultado_formatado(solucao, makespan, tarefas_tempos, execution_time):
    """
    Imprime o resultado final de forma organizada.
    """
    print("\n--- RESULTADO FINAL ---")
    print(f"a) Atribuição final de tarefas às máquinas:")
    for i, maquina in enumerate(solucao):
        tempo_total = sum(tarefas_tempos.get(tarefa_id, 0) for tarefa_id in maquina)
        print(f"   - Máquina {i}: {sorted(maquina)} (Tempo Total: {tempo_total})")
    print(f"\nb) Valor final do makespan: {makespan}")
    print(f"c) Tempo de execução do algoritmo: {execution_time:.4f} segundos")

# --------------------------------------------------------------------------
# FUNÇÃO PRINCIPAL DO SCRIPT
# --------------------------------------------------------------------------

def main():
    """
    Função principal que orquestra a solução do problema fácil.
    """
    # 1. Carregar os dados
    dicionario_f = func.ler("entradas/entrada_f.txt", 'f')
    solucao_primaria = gls.heuristica_generica(dicionario_f, 'f')


    if not dicionario_f:
        print("Não foi possível carregar os dados das tarefas. Encerrando.")
        return

    # 2. Definir parâmetros
    NUM_MAQUINAS = 5

    print("--- DADOS DE ENTRADA CARREGADOS ---")
    print(f"Total de tarefas: {len(dicionario_f)}")
    print(f"Número de máquinas: {NUM_MAQUINAS}\n")
    
    print("--- INICIANDO ALGORITMO GLS ---")
    start_time = time.time()
    
    # 3. Chamar a lógica do algoritmo
    solucao_final, makespan_final = gls_para_escalonamento(dicionario_f, NUM_MAQUINAS)
    
    end_time = time.time()
    execution_time = end_time - start_time
    
    # 4. Imprimir o resultado
    imprimir_resultado_formatado(solucao_final, makespan_final, dicionario_f, execution_time)

# --------------------------------------------------------------------------
# BLOCO DE EXECUÇÃO
# --------------------------------------------------------------------------

if __name__ == "__main__":
    main()