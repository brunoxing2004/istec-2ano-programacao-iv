totalEleitores = int(input("Insira total eleitores: "))

votosNulos = int(input("Insira total votos nulos: "))

votosBrancos = int(input("Insira total votos brancos: "))

votosValidos = int(input("Insira total votos válidos: "))

percentagemVotosNulos = (votosNulos / totalEleitores) * 100

percentagemVotosBrancos = (votosBrancos / totalEleitores) * 100

percentagemVotosValidos = (votosValidos / totalEleitores) * 100

# return (votos / total_eleitores) * 100
'''
print(percentagemVotosNulos)
print(percentagemVotosBrancos)
print(percentagemVotosValidos)
'''

print("Percentagem votos nulos: ", percentagemVotosNulos)
print("Percentagem votos brancos: ", percentagemVotosBrancos)
print("Percentagem votos válidos: ", percentagemVotosValidos)
