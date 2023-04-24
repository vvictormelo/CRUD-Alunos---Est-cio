print("\n-=-=-=-=-=-=Buscar Aluno-=-=-=-=-=-=\n")
# matFind = str(input("Digite a matrícula: "))
matFind = "202208646697"
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
