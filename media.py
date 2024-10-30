total = 0

for i in range(5):
    print("Prova", i+1, ": ", end="")
    num = float(input())
    total += num

media = total / (i+1)
print("\nMédia:", round(media/5, 2))
