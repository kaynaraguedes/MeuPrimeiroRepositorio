nota = int(input("Digite a sua nota:" ))

if nota >= 9:
    print("Conceito A - Excelente")
else:
    if nota >= 7:
        print("Conceito B - Bom")
    else:
        if nota >= 5:
            print("Conceito C - Regular")
        else:
            print("Conceito D - Reprovado")


