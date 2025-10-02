def ler(path, dificulty):
    
    dados = {}

    try:
        with open(path, 'r') as arquivo:

            next(arquivo)

            if dificulty == 'f':
                for linha in arquivo:
                    dados_linha = linha.strip().split()
                    id_tarefa = int(dados_linha[0])
                    tempo_processamento = int(dados_linha[1])
                    dados[id_tarefa] = tempo_processamento

            elif dificulty == 'm':
                maquinas = {
                    "processamento_id": {}
                }
                tarefas = {
                    "tarefa_id": {},
                    "tempo_tarefa": {}
                }
                for numero_linha, linha in enumerate(arquivo, 1):
                        dados_linha = linha.strip().split()
                        if numero_linha < 6:
                            id_maquina = int(dados_linha[0])
                            tempo_processamento = int(dados_linha[1])

                            maquinas["processamento_id"][id_maquina] = tempo_processamento
                        else:
                            id_tarefa = int(dados_linha[0])
                            tempoTarefa = int(dados_linha[1])

                            tarefas["tarefa_id"][id_tarefa] = id_tarefa
                            tarefas["tempo_tarefa"][id_tarefa] = tempoTarefa
                return maquinas, tarefas




            elif dificulty == 'd':
                for linha in arquivo:
                    dados_linha = linha.strip().split('   ')
                    id_tarefa, tempo_processamento, prioridades = dados_linha
                    id_tarefa = int(id_tarefa)
                    tempo_processamento = int(tempo_processamento)
                    
                    if "Prioridade:" in prioridades:
                        prioridades = list(map(int, prioridades.split('[')[1].split(']')[0].split(', ')))
                    else:
                        prioridades = []

                    dados[id_tarefa] = {
                        'tempo_processamento': tempo_processamento,
                        'prioridades': prioridades
                    }
            else:
                print("Erro: Tipo de entrada inválido.")

        return dados

    except FileNotFoundError:
        print(f"Erro: O arquivo '{path}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Exemplo de uso:
# caminho_f = 'caminho/do/arquivo_tarefas.txt'
# tarefas = carregar_dados(caminho_f, 'f')
# print(tarefas)

# caminho_m = 'caminho/do/arquivo_maquinas.txt'
# maquinas = carregar_dados(caminho_m, 'm')
# print(maquinas)

# caminho_d = 'caminho/do/arquivo_prioridades.txt'
# tarefas_com_prioridades = carregar_dados(caminho_d, 'd')
# print(tarefas_com_prioridades)
