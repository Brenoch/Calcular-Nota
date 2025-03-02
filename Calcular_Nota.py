Ap1n = float(input("Informe a nota da AP1: "))
Acn = float(input("Informe a nota da AC: "))
Ap2n = float(input("Informe a nota da AP2: "))

pesoap1 = 0.4
pesoap2 = 0.4
pesoac = 0.2
media = 7.0

Ap1 = Ap1n * pesoap1
Ap2 = Ap2n * pesoap2
Ac = Acn * pesoac

pAp1 = 0.4 * Ap1n * 10
pAp2 = 0.4 * Ap2n * 10
pAc = 0.2 * Acn * 10
pTotal = pAp1 + pAp2 + pAc

NotaAprov = (media - Ap1 - Ac) * 0.4


Total = Ap1 + Ap2 + Ac

if Total >= 7:
    print("Você foi aprovado")
else:
    print("Você foi reprovado")
if NotaAprov >= 0:
    print(f"Falta {NotaAprov:.1f} para aprovação")
else:
    print("")


print(f"Você tirou {Total:.1f}")
input()