alunos = []
users = {}
print('---CADASTRO---')
user = input("usuário: ")
senha = input("senha: ")
users[user] = senha
while True:
    while True:
        print("---LOGIN---")
        usuario = input("usuário: ")
        password = input("senha: ")
        if usuario in users and users[usuario] == password:
            print("bem-vindo " , usuario , "!")
            break
        else:
            print("usuário e/ou senha incorreto(s)")
            res = input("você não possui cadastro ou esqueceu a senha? (responda com s/n): ").lower()
            if res == "s":
                print('---CADASTRO---')
                user = input("usuário: ")
                senha = input("senha: ")
                users[user] = senha
    while True:
        print("---FUNÇÕES: " \
        "\n1 PARA ADICIONAR UM ALUNO NA LISTA" \
        "\n2 PARA REMOVER" \
        "\n3 PARA REMOVER POR ÍNDICE" \
        "\n4 PARA VER A LISTA DE ALUNOS" \
        "\n5 PARA APAGAR TUDO" \
        "\n'SAIR' PARA SAIR---")
        ent = input("digite: ").lower()
        match ent:
            case "sair":
                print("saindo...")
                break
            case "1":
                aluno = input("adicione o aluno: ")
                alunos.append(aluno)
            case "2":
                aluno = input("remova o aluno desejado: ").lower()
                if aluno not in alunos:
                    print("aluno não encontrado")
                else:
                    alunos.remove(aluno)
            case "3":
                aluno = int(input("digite o índice: "))
                if aluno not in alunos:
                    ("aluno não encontrado")
                else:
                    alunos.pop(aluno)
            case "4":
                print(alunos)
            case "5":
                alunos.clear()
                print("lista vazia")
            case _:
                print("entrada inválida")
