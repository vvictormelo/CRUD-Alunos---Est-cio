def program():
    print("\033[1;36m\nSEJA BEM VINDO...\n\033[m")

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
                    cadastroAluno()  # falta cadastrar validação matrícula
                case 2:
                    alterarAluno()  # falta implementar
                case 3:
                    buscarAluno()  # concluído
                case 4.1:
                    listarAlunos()  # Ajustar exibição
                case 4.2:
                    alunosAprovados()
                case 5:
                    configuraDisciplina()
                case 6:
                    acao = 6
                    print("Saindo...")
                    print("Até logo!!")
            if (acao > 6.0) or (acao < 1.0):
                print("\033[1;31m\nOops... Ação inválida. Tente novamente.\033[m")
        except ValueError:
            print("\033[1;31m\nOops... Ação inválida. Tente novamente.\033[m")


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
        print("\033[1;32m\nAluno cadastrado com sucesso!\n\033[m")
    except PermissionError:
        print(
            "\033[1;31m\nVocê não possui permissão para acessar o arquivo. Contante o suporte.\033[m"
        )


def alterarAluno():
    print("\n-=-=-=-=-=-=Alunos Cadastrados-=-=-=-=-=-=")
    try:
        with open("dbalunos.txt", "r", encoding="utf-8") as dbalunos:
            for linha in dbalunos.readlines():
                print(linha.strip("\n"))

    except PermissionError:
        print(
            "\033[1;31mVocê não possui credenciais para acessar o arquivo.\033[m"
        )  # VERIFICAR EXCEPTS
    except FileNotFoundError:
        print("\033[1;31mArquivo não encontrado!\033[m")


def buscarAluno():
    try:
        print("\033[1;34m\n-=-=-=-=-=-=Buscar Aluno-=-=-=-=-=-=\n\033[m")
        matFind = str(input("Digite a matrícula: "))

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

        print(
            f"""\033[1;34m
        Matrícula: {aluno[0]}
        Nome: {aluno[1]}
        Nota 1: {aluno[2]}
        Nota 2: {aluno[3]}
        Nota 3: {aluno[4]}
        Média: {((float(aluno[2]) + float(aluno[3]) + float(aluno[4])) / 3):.2f}
        Faltas: {aluno[5]}
        \033[m"""
        )
    except FileNotFoundError:
        print("\033[1;31mArquivo não encontrado!\033[m")
    except PermissionError:
        print("\033[1;31mVocê não possui credenciais para acessar o arquivo.\033[m")


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


# def alunosAprovados():


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
            print("\033[1;32m\nDisciplina cadastrada com sucesso!\n\033[m")
    except PermissionError:
        print(
            "\033[1;31m\nVocê não possui permissão para acessar o arquivo. Contante o suporte.\033[m"
        )


if __name__ == "__main__":
    program()
