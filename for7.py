ini = int(input("Digite o número inicial:"))
fim = int(input("Digite o número final:"))
total = 0

for num in range(ini, fim+1):
    total += num
print("A soma dos números de", ini ,"a", fim, "é", total)

