def calculate_average_gross(input_file, output_file):
    # Inicializar a soma e o contador
    total_gross = 0
    movie_count = 0

    # Abrir o arquivo actors.csv
    with open(input_file, 'r') as file:
        # Ignorar o cabeçalho
        next(file)
        for line in file:
            # Dividir a linha em partes
            parts = line.strip().split(',')
            # Obter o valor da receita bruta do filme
            gross = float(parts[-1].strip())
            # Adicionar à soma
            total_gross += gross
            # Incrementar o contador de filmes
            movie_count += 1

    # Calcular a média
    average_gross = total_gross / movie_count

    # Escrever a média no arquivo especificado
    with open(output_file, 'w', encoding='utf-8-sig') as output:
        output.write(f"Média da receita bruta dos principais filmes: ${average_gross:.2f} milhões\n")



calculate_average_gross('actors.csv', 'etapa-2.txt')