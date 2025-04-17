def count_top_movies(input_file, output_file):
    # Dicionário para armazenar a contagem de cada filme
    movie_count = {}

    # Abrir o arquivo actors.csv
    with open(input_file, 'r', encoding='utf-8') as file:
        # Ignorar o cabeçalho
        next(file)
        for line in file:
            parts = line.strip().split(',')
            top_movie = parts[4]
            # Incrementar a contagem do filme
            movie_count[top_movie] = movie_count.get(top_movie, 0) + 1

    # Ordenar os filmes por contagem (decrescente) e nome (crescente)
    sorted_movies = sorted(movie_count.items(), key=lambda x: (-x[1], x[0]))

    # Escrever as informações no arquivo Etapa-4.txt
    with open(output_file, 'a', encoding='utf-8') as output:
        for movie, count in sorted_movies:
            output.write(f"O filme {movie} aparece {count} vez(es) no dataset.\n")

# Chamar a função com os parâmetros adequados
count_top_movies('actors.csv', 'Etapa-4.txt')
