def find_actor_with_most_movies(input_file, output_file):
    # Abrir o arquivo actors.csv e encontrar o ator/atriz com o maior número de filmes
    with open(input_file, 'r') as file:
        # Ler o cabeçalho
        header = next(file).strip().split(',')
        actor_index = header.index('Actor')
        num_movies_index = header.index('Number of Movies')

        max_movies_actor = ''
        max_movies = 0
        for line in file:
            # Dividir o texto em partes com base na vírgula
            parts = line.strip().split(',')
            actor = parts[actor_index]
            # Converter o número de filmes para float e arredondar para o inteiro mais próximo
            num_movies = int(round(float(parts[num_movies_index].strip())))
            if num_movies > max_movies:
                max_movies = num_movies
                max_movies_actor = actor

    # Escrever as informações no arquivo etapa-1.txt
    with open(output_file, 'w', encoding='utf-8-sig') as output:
        output.write(f"Ator/atrizes com o maior número de filmes: {max_movies_actor}\n")
        output.write(f"Quantidade de filmes: {max_movies}\n")
        

# Chamar a função com os parâmetros adequados
find_actor_with_most_movies('actors.csv', 'etapa-1.txt')
