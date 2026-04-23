alunos = []
users = {}

print('---CADASTRO---')
while True:
    user = input("usuário: ").strip().lower()
    if user in users:
        print("usuário já existe")
    else:
        senha = input("senha: ")
        users[user] = senha
        break

while True:
    input("\naperte ENTER para ir para a tela de login")

    # LOGIN
    while True:
        print("\n---LOGIN---")
        usuario = input("usuário: ").strip().lower()
        password = input("senha: ")

        if usuario in users and users[usuario] == password:
            print("bem-vindo,", usuario, "!")
            break
        else:
            print("usuário e/ou senha incorreto(s)")
            res = input("não possui cadastro ou esqueceu a senha? (s/n): ").lower()

            if res == "s":
                print('\n---CADASTRO---')
                while True:
                    user = input("novo usuário: ").strip().lower()
                    if user in users:
                        print("usuário já existe")
                    else:
                        senha = input("senha: ")
                        users[user] = senha
                        print("cadastro realizado!")
                        break

    # MENU PRINCIPAL
    while True:
        print("\n---TELA DE ESCOLHA---")
        print("1 - lista de alunos")
        print("2 - calculadora")
        print("3 - bloco de notas")
        print("sair - sair")

        escolha = input("digite: ").lower()

        # SAIR DO SISTEMA
        if escolha == "sair":
            print("encerrando sistema...")
            break

        # LISTA DE ALUNOS
        elif escolha == "1":
            while True:
                print("\n---FUNÇÕES---")
                print("1 - adicionar aluno")
                print("2 - remover aluno")
                print("3 - remover por índice")
                print("4 - ver lista")
                print("5 - limpar lista")
                print("sair - voltar")

                ent = input("digite: ").lower()

                if ent == "sair":
                    break

                elif ent == "1":
                    aluno = input("nome do aluno: ").lower()
                    alunos.append(aluno)

                elif ent == "2":
                    aluno = input("nome do aluno: ").lower()
                    if aluno in alunos:
                        alunos.remove(aluno)
                    else:
                        print("aluno não encontrado")

                elif ent == "3":
                    try:
                        indice = int(input("índice: "))
                        if 0 <= indice < len(alunos):
                            alunos.pop(indice)
                        else:
                            print("índice inválido")
                    except ValueError:
                        print("digite um número válido")

                elif ent == "4":
                    if not alunos:
                        print("lista vazia")
                    else:
                        for i, aluno in enumerate(alunos):
                            print(i, "-", aluno)

                elif ent == "5":
                    alunos.clear()
                    print("lista apagada")

                else:
                    print("opção inválida")

        # CALCULADORA
        elif escolha == "2":
            while True:
                print("\n---CALCULADORA---")
                print("1 - adição")
                print("2 - subtração")
                print("3 - multiplicação")
                print("4 - divisão")
                print("sair - voltar")

                ope = input("operação: ").lower()

                if ope == "sair":
                    break

                if ope not in ["1", "2", "3", "4"]:
                    print("opção inválida")
                    continue

                try:
                    num1 = float(input("primeiro número: "))
                    num2 = float(input("segundo número: "))
                except ValueError:
                    print("digite apenas números")
                    continue

                if ope == "1":
                    print(num1, "+", num2, "=", num1 + num2)

                elif ope == "2":
                    print(num1, "-", num2, "=", num1 - num2)

                elif ope == "3":
                    print(num1, "*", num2, "=", num1 * num2)

                elif ope == "4":
                    if num2 == 0:
                        print("não pode dividir por zero")
                    else:
                        print(num1, "/", num2, "=", num1 / num2)

        else:
            print("opção inválida")
