print("\033[1;34m\n-=-=-=-=-=-=Aluno Aprovados-=-=-=-=-=-=\n\033[m")
# matriculaAluno = int(input("\nMatrícula do aluno: "))
with open("dbalunos.txt", "r", encoding="utf-8") as dbalunos:
    checker = True

    while checker == True:
        matriculaAluno = int(input("\nMatrícula do aluno: "))
        for i, v in enumerate(dbalunos):
            if v == str(matriculaAluno) + "\n":
                print("\033[1;31m\nMatrícula já cadastrada. Tente novamente!\n\033[m")
                matriculaAluno = int(input("\nMatrícula do aluno: "))
            else:
                checker = False

            # aluno = list()
            # aluno.append(matFind)
            # for linha in dbalunos:
            #    if linha == "-\n":
            #        break
            #    else:
            #        aluno.append(linha.strip())

# if (((valor1 + valor2 + valor3) / 3) >= 6.0) and ((cargaHorariaDisciplina / qtdFaltas) >=)


# 1º - Colocar os dados do db em uma lista
# 2º - Trazer matrícula e nome do aluno aprovado, que tenha a média maior que
