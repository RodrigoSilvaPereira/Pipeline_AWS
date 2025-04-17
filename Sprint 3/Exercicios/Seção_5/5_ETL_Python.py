def sort_actors_by_total_gross(input_file, output_file):
    # Lista para armazenar tuplas de (nome do ator, receita total bruta)
    actors_gross = []

    # Abrir o arquivo actors.csv
    with open(input_file, 'r', encoding='utf-8') as file:
        # Ignorar o cabeçalho
        next(file)
        for line in file:
            parts = line.strip().split(',')
            actor = parts[0]
            try:
                total_gross = float(parts[1])
            except ValueError:
                # Se houver um erro ao converter para float, ignore esta linha
                continue
            actors_gross.append((actor, total_gross))

    # Ordenar a lista de atores pela receita total bruta em ordem decrescente
    sorted_actors = sorted(actors_gross, key=lambda x: x[1], reverse=True)

    # Escrever as informações no arquivo Etapa-5.txt
    with open(output_file, 'w', encoding='utf-8') as output:
        for actor, total_gross in sorted_actors:
            output.write(f"{actor} - {total_gross} milhões\n")

# Chamar a função com os parâmetros adequados
sort_actors_by_total_gross('actors.csv', 'Etapa-5.txt')
