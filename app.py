def program():
    print("\033[1;36m\nSEJA BEM VINDO...\n\033[m")

    acao = 0
    while acao != 6:
        print("-=" * 15)
        print(f'{"MENU - CADASTRO ACADÊMICO":>28}')
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
                    alterarAluno()  # falta implementar
                case 3:
                    buscarAluno()
                case 4.1:
                    listarAlunos()  # Ajustar exibição e inserir a média
                case 4.2:
                    alunosAprovados()  # falta implementar
                case 4.3:
                    alunosReprovadosFaltas()  # falta implementar
                case 4.4:
                    alunoMaxMedia()  # falta implementar
                case 4.5:
                    alunoMinMedia()  # falta implementar
                case 5:
                    configurarDisciplina()
                case 6:
                    acao = 6
                    print("\nSaindo...")
                    print("Até logo!!")

            if (acao > 6.0) or (acao < 1.0):
                print("\033[1;31m\nOops... Ação inválida. Tente novamente!\n\033[m")
        except ValueError:
            print("\033[1;31m\nOops... Ação inválida. Tente novamente!\n\033[m")


def cadastroAluno():
    try:
        with open("dbalunos.txt", "a", encoding="utf-8") as dbalunos:
            print("\n-=-=-=-=-=-=Cadastro de Aluno-=-=-=-=-=-=")
            # matriculaAluno = int(input("\nMatrícula do aluno: "))

            with open("dbalunos.txt", "r", encoding="utf-8") as dba:
                alunos = []

                for linha in dba.readlines():
                    alunos.append(linha.strip("\n"))

                checker = False

                while checker == False:
                    matriculaAluno = int(input("\nMatrícula do aluno: "))
                    for item in alunos:
                        if str(matriculaAluno) in item:
                            print(
                                "\033[1;31m\nMatrícula já inserida. Insira uma nova:\033[m"
                            )
                            matriculaAluno = int(input("\nMatrícula do aluno: "))
                            checker = False
                        elif str(matriculaAluno) not in item:
                            checker = True

            nomeAluno = str(input("Nome do aluno: "))
            nota1Aluno = float(input("1ª nota: "))
            nota2Aluno = float(input("2ª nota: "))
            nota3Aluno = float(input("3ª nota: "))
            qtdFaltas = int(input("Quantidade de faltas: "))

            aluno = [
                matriculaAluno,
                nomeAluno,
                nota1Aluno,
                nota2Aluno,
                nota3Aluno,
                qtdFaltas,
            ]

            dbalunos.write(str(aluno) + ";" + str("\n"))

        print("\033[1;32m\nAluno cadastrado com sucesso!\n\033[m")
    except PermissionError:
        print("\033[1;31m\nVocê não possui permissão para acessar o arquivo.\033[m")


def alterarAluno():
    print("\n-=-=-=-=-=-=Alterar Aluno-=-=-=-=-=-=")
    try:
        
    except PermissionError:
        print(
            "\033[1;31mVocê não possui credenciais para acessar o arquivo.\033[m"
        )  # VERIFICAR EXCEPTS
    except FileNotFoundError:
        print("\033[1;31mArquivo não encontrado!\033[m")


def buscarAluno():
    try:
        print("\033[1;34m\n-=-=-=-=-=-=Buscar Aluno-=-=-=-=-=-=\n\033[m")
        matFind = str(input("\033[1;34mDigite a matrícula: \033[m"))

        with open("dbalunos.txt", "r", encoding="utf-8") as dbalunos:
            aluno = []
            for linha in dbalunos.readlines():
                if matFind in linha:
                    aluno.append(
                        linha.strip("\n").strip("[").strip(";").strip("]").strip("'")
                    )

            for alun in aluno:
                listAluno = alun.split(", ")

        print(
            f"""\033[1;34m
        Nome: {listAluno[1]}
        Nota 1: {listAluno[2]}
        Nota 2: {listAluno[3]}
        Nota 3: {listAluno[4]}
        Média: {((float(listAluno[2]) + float(listAluno[3]) + float(listAluno[4])) / 3):.2f}
        Faltas: {listAluno[5]}
        \033[m"""
        )

    except FileNotFoundError:
        print("\033[1;31m\nArquivo não encontrado!\033[m")
    except PermissionError:
        print("\033[1;31m\nVocê não possui credenciais para acessar o arquivo.\033[m")
    except UnboundLocalError:
        print("\033[1;31m\nMatrícula não existente na base.\033[m")


def listarAlunos():
    try:
        with open("dbalunos.txt", "r", encoding="utf-8") as dbalunos:
            print("\n-=-=-=-=-=-=Alunos Cadastrados-=-=-=-=-=-=")
            for linha in dbalunos.readlines():
                print(linha.strip("\n"))
    except FileNotFoundError:
        print("\033[1;31mArquivo não encontrado!\033[m")
    except PermissionError:
        print("\033[1;31mVocê não possui credenciais para acessar o arquivo.\033[m")


def alunosAprovados():
    try:
        print("\033[1;34m\n-=-=-=-=-=-=Aluno Aprovados-=-=-=-=-=-=\n\033[m")

        with open("dbalunos.txt", "r", encoding="utf-8") as dbalunos:
            for i, v in enumerate(dbalunos):
                if v == matFind + "\n":
                    aluno = list()
                    aluno.append(matFind)
                    for linha in dbalunos:
                        if linha == "-\n":
                            break
                        else:
                            aluno.append(linha.strip())
    except FileNotFoundError:
        print("\033[1;31mArquivo não encontrado!\033[m")
    except PermissionError:
        print("\033[1;31mVocê não possui credenciais para acessar o arquivo.\033[m")


def configurarDisciplina():
    try:
        with open("config.txt", "x", encoding="utf-8") as configuracao:
            print("\n-=-=-=-=-=-=-=Configuração-=-=-=-=-=-=-=\n")
            nomeDisciplina = str(input("Nome da disciplina: "))
            nomeProfessor = str(input("Nome do professor: "))
            cargaHorariaDisciplina = int(input("Carga horária da disciplina: "))
            anoDisciplina = int(input("Ano da disciplina: "))

            configuracao.write(nomeDisciplina + "\n")
            configuracao.write(nomeProfessor + "\n")
            configuracao.write(str(cargaHorariaDisciplina) + "\n")
            configuracao.write(str(anoDisciplina) + "\n")
            print("\033[1;32m\nDisciplina cadastrada com sucesso!\n\033[m")
    except PermissionError:
        print("\033[1;31m\nVocê não possui permissão para acessar o arquivo.\033[m")
    except FileExistsError:
        print("\033[1;31m\nArquivo de configuração já criado e configurado.\033[m")


if __name__ == "__main__":
    program()
