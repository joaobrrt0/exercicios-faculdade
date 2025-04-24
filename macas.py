num_macas = int(input("Diga quantas maçãs você comprou: "))
if num_macas < 12:
    macas = 0.30
    print(f"Você comprou {num_macas} maçãs e gastará: R${num_macas * macas:.2f}")
else:
    macas = 0.25
    print(f"Você comprou {num_macas} maçãs e gastará: R${num_macas * macas:.2f}")
