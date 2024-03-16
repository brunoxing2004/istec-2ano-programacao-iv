precoSemIva = float(input("Insira preço sem IVA: "))

precoFinal = ((precoSemIva / 100) * 23) + precoSemIva

print("Preço final com IVA a 23%: " + str(round(precoFinal, 2)) + "€")