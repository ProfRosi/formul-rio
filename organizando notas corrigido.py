def media(lista):
    soma = 0
    for nota in lista:
        soma += float(nota)
    return soma / len(lista)

def classificar(nota):
    if nota >= 7:
        return "Aprovado"
    elif nota >= 5:
        return "Recuperação"
    else:
        return "Reprovado"

# Dados de entrada 
entrada = [7.5, 4.0, 6.0, 8.2, 5.9, 3.5, 9.0]

# Calculando a média da turma
print(f"Média geral da turma: {media(entrada):.1f}")

# Exibindo a situação de cada aluno
numero = 1
for nota in entrada:
    print(f"Aluno {numero}: Nota = {nota:.1f}, Situação = {classificar(nota)}")
    numero += 1