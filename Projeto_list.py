def menu_escolha():
    print("----- TO DO LIST -----")
    print("1 - Adicionar tarefas")
    print("2 - Lista de tarefas ")
    print("3 - Remover tarefa")
    print("4 - Sair")

tarefas = []

while True:
    menu_escolha()
    op = input("Informe a opcao desejada:")
    if op == '1':
        tarefa = input("Informe a tarefa:")
        tarefas.append(tarefa)
