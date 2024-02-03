notas = list(map(float, input().split()))
pesos = [2, 3, 4, 1]

soma_ponderada = sum(nota * peso for nota, peso in zip(notas, pesos))
soma_pesos = sum(pesos)
media = soma_ponderada / soma_pesos

print(f'Media: {media:.1f}')

if media >= 7.0:
    print('Aluno aprovado.')
elif media < 5.0:
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')
    nota_exame = float(input())
    print(f'Nota do exame: {nota_exame:.1f}')
    media_final = (media + nota_exame) / 2
    if media_final >= 5.0:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print(f'Media final: {media_final:.1f}')
