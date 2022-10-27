# PILHA E NODE
# 2. Fazer um programa que trate o seguinte menu:
# • 1 - Empilhar elemento
# • 2 - Desempilhar elemento
# • 3 - Mostrar o topo
# • 4 - Imprimir tudo zerando a pilha
# • 5 – Sair

from Stack import Stack

pilha = Stack()

sair = 0

while (sair != 1):
    print("\n1 - Empilhar elemento")
    print("2 - Desempilhar elemento")
    print("3 - Mostrar o topo")
    print("4 - Imprimir tudo zerando a pilha")
    print("5 – Sair\n")
    res = input("Selecione o que deseja fazer: ")

    if res == '1':
        elm = input("Informe o elemento que deseja empilhar: ")
        pilha.push(elm)
        print("\nEmpilhou: " + str(elm))
    elif res == '2':
        elm = pilha.pop()
        print("\nDesempilhou: " + str(elm))
    elif res == '3':
        print("\nO elemento do topo da pilha é: " + str(pilha.peek()))
    elif res == '4':
        pilhalen = len(pilha)
        for i in range(0, pilhalen):
            pilha.pop()
        for i in range(0, pilhalen):
            pilha.push(0)
        print(repr(pilha))
    elif res == '5':
        print("\nObrigado!")
        sair = 1
    else:
        print("\nOpção inválida")
