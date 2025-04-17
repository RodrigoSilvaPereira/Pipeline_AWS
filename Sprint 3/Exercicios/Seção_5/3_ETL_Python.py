def find_actor_with_highest_average_gross(input_file, output_file):
    highest_average_actor = ''
    highest_average = 0

    with open(input_file, 'r', encoding='utf-8-sig') as file:  # Usando 'utf-8-sig' como codificador
        next(file)  # Ignorar o cabeçalho
        for line in file:
            parts = line.strip().split(',')
            actor = parts[0]
            average_gross = float(parts[3])
            if average_gross > highest_average:
                highest_average = average_gross
                highest_average_actor = actor

    with open(output_file, 'w') as output:
        output.write(f"Ator com a maior média de receita de bilheteria bruta por filme: {highest_average_actor}\n")
        output.write(f"Média de receita bruta por filme: {highest_average}\n")

find_actor_with_highest_average_gross('actors.csv', 'etapa-3.txt')
