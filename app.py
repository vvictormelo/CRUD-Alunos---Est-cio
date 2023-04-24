def program():
    print("\nSEJA BEM VINDO...\n")

    menuInicial()


def menuInicial():
    acao = 0
    while acao != 6:
        print("-=" * 15)
        print(f'{"CADASTRO ACADÊMICO":>24}')
        print("-=" * 15)
        print("\n1 - Cadastrar Aluno")
        print("2 - Alterar Aluno")
        print("3 - Buscar Aluno por matrícula")
        print(
            """4 - Relatórios: 
        4.1 - Listar todos os alunos 
        4.2 - Listar alunos aprovados 
        4.3 - Listar alunos reprovados por faltas
        4.4 - Listar dados completos do aluno de maior média 
        4.5 - Listar dados completos do aluno de menor média"""
        )
        print("5 - Configurações")
        print("6 - Sair")

        try:
            acao = float(input("\nInsira a ação desejada: "))
            match acao:
                case 1:
                    cadastroAluno()
                case 2:
                    alterarAluno()
                case 3:
                    buscarAluno()
                case 4.1:
                    listarAlunos()
                case 4.2:
                    buscarAluno()
                case 5:
                    configuraDisciplina()
                case 6:
                    acao = 6
                    print("Saindo...")
                    print("Até logo!!")
            if (acao > 6.0) or acao < 1.0:
                print("\nOops... Ação inválida. Tente novamente.")
        except ValueError:
            print("\nOops... Ação inválida. Tente novamente.")


def cadastroAluno():
    try:
        with open("dbalunos.txt", "a", encoding="utf-8") as dbalunos:
            print("\n-=-=-=-=-=-=Cadastro de Aluno-=-=-=-=-=-=")
            matriculaAluno = int(input("\nMatrícula do aluno: "))

            # for linha in dbalunos:
            #    linha = linha.strip()
            #    if matriculaAluno in linha:
            #        print("Matrícula já cadastrada. Tente novamente: ")

            nomeAluno = str(input("Nome do aluno: "))
            nota1Aluno = float(input("1ª nota: "))
            nota2Aluno = float(input("2ª nota: "))
            nota3Aluno = float(input("3ª nota: "))
            qtdFaltas = int(input("Quantidade de faltas: "))

            dbalunos.write("Matricula: " + str(matriculaAluno) + str("\n"))
            dbalunos.write("Nome: " + nomeAluno + str("\n"))
            dbalunos.write("Nota 1: " + str(nota1Aluno) + str("\n"))
            dbalunos.write("Nota 2: " + str(nota2Aluno) + str("\n"))
            dbalunos.write("Nota 3: " + str(nota3Aluno) + str("\n"))
            dbalunos.write("Faltas: " + str(qtdFaltas) + str("\n"))
            dbalunos.write(str("-") + str("\n"))
        print("\nAluno cadastrado com sucesso!\n")
    except PermissionError:
        print("\nVocê não possui permissão para acessar o arquivo. Contante o suporte.")


def alterarAluno():
    print("\n-=-=-=-=-=-=Alunos Cadastrados-=-=-=-=-=-=")
    try:
        with open("dbalunos.txt", "r", encoding="utf-8") as dbalunos:
            for linha in dbalunos.readlines():
                print(linha.strip("\n"))

    except PermissionError:
        print(
            "Você não possui credenciais para acessar o arquivo."
        )  # VERIFICAR EXCEPTS
    except FileNotFoundError:
        print("Arquivo não encontrado!")


def buscarAluno():  # MELHORAR A EXIBIÇÃO
    try:
        print("\n-=-=-=-=-=-=Buscar Aluno-=-=-=-=-=-=\n")
        matFind = str(input("Digite a matrícula: "))
        with open("dbalunos.txt", "r", encoding="utf-8") as dbalunos:
            for i, v in enumerate(dbalunos):
                if v == matFind + "\n":
                    print(f"\n{v}")
                    for linha in dbalunos:
                        if linha == "*\n":
                            break
                        else:
                            print(f"\n{linha}")
    except FileNotFoundError:
        print("Arquivo não encontrado!")
    except PermissionError:
        print("Você não possui credenciais para acessar o arquivo.")


def listarAlunos():
    try:
        with open("dbalunos.txt", "r", encoding="utf-8") as dbalunos:
            print("\n-=-=-=-=-=-=Alunos Cadastrados-=-=-=-=-=-=")
            for linha in dbalunos.readlines():
                print(linha.strip("\n"))
    except FileNotFoundError:
        print("Arquivo não encontrado!")
    except PermissionError:
        print("Você não possui credenciais para acessar o arquivo.")


def configuraDisciplina():
    try:
        with open("config.txt", "w", encoding="utf-8") as configuracao:
            print("\n-=-=-=-=-=-=-=Configuração-=-=-=-=-=-=-=\n")
            nomeDisciplina = str(input("Nome da disciplina: "))
            nomeProfessor = str(input("Nome do professor: "))
            cargaHorariaDisciplina = int(input("Carga horária da disciplina: "))
            anoDisciplina = int(input("Ano da disciplina: "))

            configuracao.write(nomeDisciplina + "\n")
            configuracao.write(nomeProfessor + "\n")
            configuracao.write(str(cargaHorariaDisciplina) + "\n")
            configuracao.write(str(anoDisciplina) + "\n")
            print("\nDisciplina cadastrada com sucesso!\n")
    except PermissionError:
        print("\nVocê não possui permissão para acessar o arquivo. Contante o suporte.")


if __name__ == "__main__":
    program()
