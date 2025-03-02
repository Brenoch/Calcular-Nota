Ap1 = float(input("Informe a nota da AP1: "))
Ac = float(input("Informe a nota da AC: "))
Ap2 = float(input("Informe a nota da AP2: "))

Total = (Ap1 + Ap2 + Ac) / 3
Faltante = Total *(70/100)

if Total >= 7:
    print("Você foi aprovado")
else:
    print("Você foi reprovado")

print(f"Você tirou {Total:.1f}")
