# Declaração de Variáveis
qtdTurmas = 0
idturma = ''
qtdAluno = 0
Matricula = ''
freq = ''
contPres = 0
contAus = 0
porAus = 0.0
maiorAus = 0.0
menorAus = 100.0
maiorTA = ''
menorTA = ''
cont = 0

# Entrada de dados
qtdTurmas = int(input())  # Informe a qtd de Turmas

for i in range(0, qtdTurmas):
    # Entrada de dados
    idturma = input()  # Informe a turma
    qtdAluno = int(input())  # Informe a quantidade de Alunos
    while qtdAluno > 0:
        Matricula = input()  # Informe a Matrícula
        freq = input()  # Informe frequencia do Aluno Presente ou Ausente
        if freq == "P":
            contPres += 1
        elif freq == "A":
            contAus += 1
        qtdAluno -= 1
    porAus = contAus / ((contPres + contAus) / 100)
    if porAus > maiorAus:
        maiorAus = porAus
        maiorTA = idturma
    if porAus < menorAus:
        menorAus = porAus
        menorTA = idturma
    if porAus > 20.0:
        cont += 1
    qtdAluno = 0
    contAus = 0
    contPres = 0

    print("TURMA=%s AUSENCIA=%.2f%%" % (idturma, porAus))
print("TURMA COM MAIOR PORCENTAGEM DE AUSENCIA=%s AUSENCIA=%.2f%%" % (maiorTA, maiorAus))
print("TURMA COM MENOR PORCENTAGEM DE AUSENCIA=%s AUSENCIA=%.2f%%" % (menorTA, menorAus))
print(cont, "TURMAS COM PORCENTAGEM DE AUSENCIA SUPERIOR A 20%")
