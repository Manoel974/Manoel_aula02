#Atividade 1
nm1 = int(input("Insira um número: "))
nm2 = int(input("Insira um número: "))

if nm1 > nm2:
    nmaior = nm1
else:
    nmaior = nm2

print(f"Dentre os números {nm1} e {nm2}, o número maior é {nmaior}.")

#Atividade 2
numero = int(input("Indique um número: "))

if numero % 2 == 0:
    msg = "É par!"
else:
    msg = "É impar!"

print(msg)
