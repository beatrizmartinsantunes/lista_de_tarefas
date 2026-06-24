"""
Gerenciador de Tarefas (To-Do List) em terminal
Mini projeto de 3 aulas — Python puro

Este arquivo cresce ao longo das 3 aulas. Cada bloco abaixo está marcado
com a aula em que deve ser implementado:

    # ===== AULA 1 =====
    # ===== AULA 2 =====
    # ===== AULA 3 =====

Leia o arquivo AULA1.md (depois AULA2.md, depois AULA3.md) para saber
exatamente o que fazer em cada parte. Procure os comentários "# TODO"
-- é ali que vocês vão escrever código. Não apague as docstrings, elas
explicam o que cada função deve fazer.
"""

import csv
import os

# ===== AULA 3 =====
ARQUIVO_TAREFAS = "tarefas.csv"
CAMPOS_CSV = ["titulo", "concluida", "prioridade"]

# Lista que vai guardar todas as tarefas.
# Cada tarefa é um dicionário com as chaves: "titulo", "concluida", "prioridade"
tarefas = []


# =====================================================================
# ===== AULA 1 — Fundação do sistema =====
# =====================================================================

def adicionar_tarefa(titulo, prioridade="media"):
    tarefa = {'titulo': titulo, 'concluida': False, 'prioridade': prioridade} # False pq ainda não foi concluida. Isso é o dicionário
    #Dicionário com as chaves, média pq sempre começa com média, mas o usuário pode alterar a prioridade
    tarefas.append(tarefa) # adiciona o dicionário na lista de tarefas
    print(f"Tarefa '{titulo}' adicionada com prioridade '{prioridade}'") # exibe a mensagem de confirmação
    """
    Cria uma nova tarefa e adiciona à lista `tarefas`.

    A tarefa deve ser um dicionário com as chaves:
        - "titulo": o texto recebido no parâmetro `titulo`
        - "concluida": deve começar como False
        - "prioridade": o texto recebido no parâmetro `prioridade`

    Depois de adicionar, exiba uma mensagem confirmando que a tarefa
    foi criada (pode usar print).
    """
    # TODO (Aula 1): crie o dicionário da tarefa ✓
    # TODO (Aula 1): adicione o dicionário à lista `tarefas` ✓
    # TODO (Aula 1): exiba uma mensagem de confirmação ✓
    # TODO (Aula 3): depois de implementar salvar_tarefas(), chame-a aqui
    pass


def listar_tarefas():
    if len(tarefas) == 0: # tarefas.count siginifica que conta quantos elementos tem na lista
            print("Nenhuma tarefa cadastrada")
            return
    else:
        for index, tarefa in enumerate(tarefas, start=1): # index número da linha posição
            status = "X" if tarefa ["concluida"] else " "
            print(f"{index}. [{status}] {tarefa['titulo']} (prioridade: {tarefa['prioridade']})") 

    """
    Exibe todas as tarefas cadastradas na lista `tarefas`.

    Regras:
        - Se a lista estiver vazia, exiba uma mensagem avisando que
          não há tarefas cadastradas e pare a função (return).
        - Caso contrário, para cada tarefa, exiba o número dela na lista
          (começando em 1), se está concluída ou não, o título e a
          prioridade. Dica: use enumerate(tarefas, start=1).

    Sugestão de formato de saída para cada linha:
        1. [ ] Estudar Python (prioridade: alta)
        2. [X] Lavar a louça (prioridade: baixa)
    """
    # TODO (Aula 1): trate o caso de lista vazia ✓
    # TODO (Aula 1): percorra a lista de tarefas e exiba cada uma formatada ✓
    pass


# =====================================================================
# ===== AULA 2 — Lógica e manipulação de tarefas =====
# =====================================================================

def concluir_tarefa(indice):
    if indice < 1 or indice > len(tarefas): # len(tarfas) tamanho da lista, de quantas tarefas tem na lista
        print("Numero de tarefa invalido.")
        return
    else:
        for index, tarefa in enumerate(tarefas, start=1):
            if index == indice:
                tarefa["concluida"] = True
                print(f'Tarefa "{index}. {tarefa["titulo"]}" concluida!')

    """
    Marca como concluída a tarefa na posição `indice` (começando em 1).

    Regras:
        - Se `indice` for menor que 1 ou maior que o tamanho da lista,
          exiba uma mensagem de erro ("Numero de tarefa invalido.") e
          pare a função (return).
        - Caso contrário, altere a chave "concluida" da tarefa para True
          e exiba uma mensagem confirmando a conclusão.

    Lembre-se: o índice exibido para o usuário começa em 1, mas listas em
    Python começam em 0. Você vai precisar ajustar isso (indice - 1).
    """
    # TODO (Aula 2): valide o índice recebido✓
    # TODO (Aula 2): marque a tarefa como concluída✓
    # TODO (Aula 2): exiba uma mensagem de confirmação✓
    # TODO (Aula 3): depois de implementar salvar_tarefas(), chame-a aqui
    pass


def remover_tarefa(indice):
    if indice < 1 or indice > len(tarefas):
        print("Numero de tarefa invalido.")
        return
    elif indice >= 1 and indice <= len(tarefas):
        for index, tarefa in enumerate(tarefas, start=1):
            if index == indice:
                tarefa_removida = tarefas.pop(indice - 1) # pop apaga a tarefa da lista e guarda na variável tarefa_removida e diminui o indice para ficar correto, pois o índice do usuário começa em 1 e o índice da lista começa em 0
                print(f'Tarefa "{indice}. {tarefa_removida["titulo"]}" removida!')

                
    """
    Remove da lista a tarefa na posição `indice` (começando em 1).

    Regras:
        - Mesma validação de índice de concluir_tarefa().
        - Use o método tarefas.pop(indice - 1) para remover e guardar
          a tarefa removida ao mesmo tempo.
        - Exiba uma mensagem confirmando qual tarefa foi removida.
    """
    # TODO (Aula 2): valide o índice recebido  ✓
    # TODO (Aula 2): remova a tarefa da lista usando pop() ✓
    # TODO (Aula 2): exiba uma mensagem de confirmação ✓
    # TODO (Aula 3): depois de implementar salvar_tarefas(), chame-a aqui
pass


def editar_tarefa(indice, novo_titulo):
    if indice < 1 or indice > len(tarefas):
        print("Numero de tarefa invalido.")
        return
    elif indice >= 1 and indice <= len(tarefas):
        for index, tarefa in enumerate(tarefas, start=1):
            if index == indice:
                tarefa["titulo"] = novo_titulo
                print(f'Tarefa atualizada {indice}. {tarefa["titulo"]}')
                

    """
    [DESAFIO] Atualiza o título de uma tarefa existente.

    Regras:
        - Mesma validação de índice das funções anteriores.
        - Atualize apenas a chave "titulo" da tarefa, sem alterar as
          outras informações (concluida, prioridade).
        - Exiba uma mensagem confirmando a atualização.
    """
    # TODO (Aula 2): valide o índice recebido ✓
    # TODO (Aula 2): atualize o título da tarefa ✓
    # TODO (Aula 2): exiba uma mensagem de confirmação ✓
    # TODO (Aula 3): depois de implementar salvar_tarefas(), chame-a aqui
    pass


# =====================================================================
# ===== AULA 3 — Persistência (CSV) e finalização =====
# =====================================================================

def salvar_tarefas():
    """
    Salva a lista `tarefas` no arquivo CSV definido em ARQUIVO_TAREFAS.

    Use csv.DictWriter dentro de um bloco `with open(...)`.

    Passos:
        1. Abra o arquivo em modo de escrita ("w"), com newline=""
           e encoding="utf-8"
        2. Crie um csv.DictWriter passando o arquivo e fieldnames=CAMPOS_CSV
        3. Chame writer.writeheader() para escrever a linha de cabeçalho
        4. Chame writer.writerows(tarefas) para escrever todas as tarefas
    """
    # TODO (Aula 3): abra o arquivo em modo de escrita
    # TODO (Aula 3): crie o csv.DictWriter com fieldnames=CAMPOS_CSV
    # TODO (Aula 3): escreva o cabeçalho e as linhas
    pass


def carregar_tarefas():
    """
    Carrega as tarefas do arquivo CSV para a lista `tarefas`, caso o
    arquivo já exista.

    Regras:
        - Use `global tarefas` no início da função, já que vamos
          substituir a lista inteira.
        - Se o arquivo não existir, apenas mantenha `tarefas` como uma
          lista vazia (dica: os.path.exists(ARQUIVO_TAREFAS)).
        - Se existir, abra o arquivo e use csv.DictReader para ler cada
          linha como um dicionário.
        - Atenção: tudo que vem do CSV é texto (string)! A coluna
          "concluida" vai vir como a string "True" ou "False", não como
          um valor booleano. Vocês precisam converter isso de volta:
              linha["concluida"] = linha["concluida"] == "True"
    """
    global tarefas
    # TODO (Aula 3): verifique se o arquivo existe, senão mantenha tarefas = []
    # TODO (Aula 3): abra o arquivo e use csv.DictReader para ler as linhas
    # TODO (Aula 3): converta a coluna "concluida" de string para booleano
    # TODO (Aula 3): monte a lista `tarefas` com os dicionários lidos
    pass


def listar_pendentes():
    """
    [DESAFIO] Exibe apenas as tarefas que ainda não foram concluídas.

    Dica: list comprehension ajuda bastante aqui:
        pendentes = [t for t in tarefas if not t["concluida"]]
    """
    # TODO (Aula 3): filtre as tarefas não concluídas
    # TODO (Aula 3): exiba a lista filtrada (mensagem se estiver vazia também)
    pass


# =====================================================================
# Menu e função principal
# =====================================================================

def exibir_menu():
    """
    Exibe as opções do menu principal no terminal.

    Opções esperadas (versão final, Aula 3):
        1. Adicionar tarefa
        2. Listar tarefas
        3. Concluir tarefa
        4. Remover tarefa
        5. Editar tarefa
        6. Listar pendentes
        7. Sair

    Na Aula 1 vocês só vão ter as opções 1, 2 e Sair. Vão completando
    as outras opções nas aulas seguintes.
    """
    print("=== GERENCIADOR DE TAREFAS ===")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Concluir tarefa")
    print("4. Remover tarefa")
    print("5. Editar tarefa") 
    print("7. Sair")
    # TODO (Aula 1): adicione a opção "Sair" (vai virar a opção 7 ao final) ✓
    # TODO (Aula 2): adicione as opções 3 (Concluir), 4 (Remover), 5 (Editar) ✓
    # TODO (Aula 3): adicione a opção 6 (Listar pendentes) e renumere "Sair" para 7


def main():
    """
    Função principal do programa.

    Versão final esperada (Aula 3):
        - Antes do loop começar, chame carregar_tarefas() para recuperar
          as tarefas salvas anteriormente.
        - Exiba o menu em loop (while True).
        - "1": pedir o título da tarefa e chamar adicionar_tarefa()
        - "2": chamar listar_tarefas()
        - "3": listar tarefas, pedir o número da tarefa a concluir e
          chamar concluir_tarefa(). Use try/except para tratar entradas
          que não são números (ValueError).
        - "4": o mesmo fluxo, mas chamando remover_tarefa()
        - "5": pedir o número da tarefa e o novo título, chamar
          editar_tarefa()
        - "6": chamar listar_pendentes()
        - "7": exibir mensagem de despedida e encerrar o loop (break)
        - qualquer outra opção: avisar que é inválida

    Vão completando esse fluxo aula a aula — na Aula 1 só "1", "2" e
    sair (que será a última opção, mas pode comecar como "3").
    """
    # TODO (Aula 3): chame carregar_tarefas() antes do loop começar

    while True:
        exibir_menu()
        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            titulo = input("Titulo da tarefa: ")
            adicionar_tarefa(titulo)

        elif opcao == "2":
            listar_tarefas()

        elif opcao == "3":
            listar_tarefas()
            indice = int(input("Numero da tarefa a concluir: "))
            concluir_tarefa(indice)

        elif opcao == "4":
            listar_tarefas()
            indice = int(input("Numero da tarefa a remover: "))
            remover_tarefa(indice)

        elif opcao == "5":
            listar_tarefas()
            indice = int(input("Numero da tarefa a editar: "))
            novo_titulo = input("Novo titulo da tarefa: ")
            editar_tarefa(indice, novo_titulo)

        elif opcao == "7":
            print("Saindo do programa.")
            break

        # TODO (Aula 1): implemente a opção de Sair (com break) ✓
        # TODO (Aula 2): implemente as opções de concluir, remover e editar
        #                (cada uma com try/except para ValueError) ✓
        # TODO (Aula 3): implemente a opção de listar pendentes e
        #                renumere a opção de sair

        else:
            print("Opcao invalida, tente novamente.\n")


if __name__ == "__main__":
    main()
