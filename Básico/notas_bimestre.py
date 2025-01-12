nota_um = float(input("Informe a primeira nota: "))
nota_dois = float(input("Informe a segunda nota: "))
nota_tres = float(input("Informe a terceira nota: "))
nota_quatro = float(input("Informe a quarta nota: "))

soma_nota = nota_um + nota_dois + nota_tres + nota_quatro
dividir_nota = (soma_nota / 4)
media = round(dividir_nota, 1)

if media > 4.0 and media < 7.0:
    print(f"O aluno ficou em recuperação, a media foi {media}")
elif media >= 7.0:
    print(f"O aluno passou por média, a media foi {media}")
elif media <= 4:
    print(f"O aluno esta reprovado, a media foi {media}")