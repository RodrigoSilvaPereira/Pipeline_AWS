# Lista de animais
animais = ["gato", "cachorro", "tigre", "elefante", "girafa", "leão", "pinguim", "zebra", "macaco", "hipopótamo",
           "cobra", "aranha", "crocodilo", "gavião", "coruja", "abelha", "borboleta", "peixe", "urso", "panda"]

animais_ordenados = sorted(animais)

print("\n".join([animal for animal in animais_ordenados]))

with open("animais.csv", "w") as file:
    for animal in animais_ordenados:
        file.write(f"{animal}\n")
