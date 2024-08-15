nm = input("Digite o seu nome: ")
nt = float(input("Digite a nota desejada: "))
mt = input("Digite a matéria desejada: ")

if nt < 0 or nt > 10:
    print("Nota Inválida !")
elif nt >= 0 or nt <= 10:
    if nt >= 5.5 and nt <= 6.0:
        nt = 6
if nt >= 6:
    print(f"O aluno {nm} está aprovado com nota {nt} na disciplina {mt}")
else:
    print(f"O aluno {nm} está reprovado com nota {nt} na disciplina {mt}")