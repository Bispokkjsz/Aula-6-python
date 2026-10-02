# 1 - mostrar todas as tarefas
# 2 - mostrar tarefas concluidas
# 3 - mostrar tarefas pendentes
# 4 - mostrar tarefas por prioridades 
# 5 - cadastrar tarefa nova
# 6 - finalizar tarefa 
# 7 - remover tarefa
# 0 - sair

tarefas = [
    {"titulo": "estudar", "concluido": "sim", "prioridade": "alta" },
    {"titulo": "ler", "concluido": "nao", "prioridade": "baixa" },
    {"titulo": "esportes", "concluido": "sim", "prioridade": "alta" },
    {"titulo": "video games", "concluido": "nao", "prioridade": "baixa" },
]

def mostrar():
    for tarefa in tarefas:
        if tarefa ["concluido"] == "sim":
           status = "✅"
        else:
            tarefa["concluido"] == "nao"
            status = "❌"
        print(f"{tarefa["titulo"]},{status},{tarefa["prioridade"]}")

def concluidas():
    for tarefa in tarefas:
        if tarefa["concluido"] == "sim":
            print(tarefa)

def pendentes():
    for tarefa in tarefas:
        if tarefa["concluido"] == "nao":
            print(tarefa)

def prioridades():
   prioridade = str(input("Qual a sua prioridade(baixa/alta): "))
   for tarefa in tarefas:
       if tarefa["prioridade"] == prioridade:
           print(tarefa)

def cadastrar():
    titulo = str(input("Qual a nova tarefa que vc quer adicionar: "))
    prioridade = str(input("Qual a prioridade da sua tarefa(baixa/alta): "))

    nova_tarefa = {
        "titulo": titulo,
        "prioridade": prioridade,
    }
    tarefas.append(nova_tarefa)
    print(tarefas)

def finalizar():
    finalizando = str(input("Qual tarefa voce gostaria de finalizar: "))
    for tarefa in tarefas:
        if tarefa["titulo"] == finalizando:
            tarefa["concluido"] = "sim"
            print(tarefa)

def remover():
    nome_tarefa = str(input("Qual tarefa voce gostaria de excluir: "))
    for tarefa in tarefas:
        if tarefa["titulo"] == nome_tarefa:
            tarefas.remove(tarefa)
            print(tarefa)

    
while True:
    print("1 - Mostrar todas as tarefas")
    print("2 - mostrar todas as tarefas concluidas")
    print("3 - mostrar todas as tarefas pendentes")
    print("4 - mostrar todas as tarefas com prioridade")
    print("5 - cadastrar uma tarefa nova")
    print("6 - finalizar tarefa")
    print("7 - remover alguma tarefa")
    print("0 - Sair")

    opcao = input("Escolha uma opcao: ")

    if opcao == "1":
        mostrar()
    elif opcao == "2":
        print("---> SUAS TAREFAS CONCLUIDAS FORAM: <---")
        concluidas()
    elif opcao == "3":
        print("--> SUAS TAREFAS PENDENTES SÃO: <---")
        pendentes()
    elif opcao == "4":
        prioridades()
    elif opcao == "5":
        print("---> VOCE ADICIONOU NOVAS TAREFAS: <---")
        cadastrar()
    elif opcao == "6":
        finalizar()
    elif opcao == "7":
        remover()
    elif opcao == "0":
        print("Saindo do Sistema...")
        break
    else:
        print("opcao invalida, tente novamente!")
        break