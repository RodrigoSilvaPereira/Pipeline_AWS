# Analise de Filmes Speculative

#Criação da Tabela de Métricas Principal (Tabela Fato)

CREATE TABLE IF NOT EXISTS tb_metricas_filme AS
SELECT
  ROW_NUMBER() OVER () as id_metrica_filme,
  "nome_genero_filme", 
  "nota_media_filme", 
  "titulo_filme",
  "numero_votos_filme", 
  "popularidade_filme", 
  "rendimento_filme", 
  year(try(parse_datetime("data_lancamento_filme", 'yyyy-MM-dd'))) as ano_lancamento_filme,
  "media_votos_filme", 
  "contagem_votos_filme"

FROM refined

# Criação da Tabela de Subgenero mais frequente

CREATE TABLE IF NOT EXISTS subgenero_frequente AS
SELECT 
    nome_genero_filme AS subgenero,
    COUNT(*) AS quantidade_filmes
FROM 
    tb_metricas_filme
GROUP BY 
    nome_genero_filme
ORDER BY 
    quantidade_filmes DESC;

# Criação da tabela de popularidade dos filmes

CREATE TABLE IF NOT EXISTS popularidade_filme AS
WITH ranked_filmes AS (
    SELECT 
        nome_genero_filme,
        titulo_filme,
        popularidade_filme,
        ROW_NUMBER() OVER (PARTITION BY titulo_filme ORDER BY popularidade_filme DESC) AS rank
    FROM 
        tb_metricas_filme
)
SELECT 
    nome_genero_filme,
    titulo_filme,
    popularidade_filme
FROM 
    ranked_filmes
WHERE 
    rank = 1
ORDER BY 
    popularidade_filme DESC;

# Criação da tabela de Média de Votos do subgenero Science Fiction

CREATE TABLE IF NOT EXISTS media_votos_subgenero AS
SELECT 
    AVG(media_votos_filme) AS media_votos,
    'Science Fiction' AS subgenero
FROM 
    tb_metricas_filme
WHERE 
    nome_genero_filme = 'Science Fiction';

# Criação da tabela de frequencia de lançamento

CREATE TABLE IF NOT EXISTS frequencia_lancamento AS
SELECT 
    ano_lancamento_filme AS ano_lancamento,
    COUNT(*) AS quantidade_filmes
FROM 
    tb_metricas_filme
WHERE 
    nome_genero_filme = 'Science Fiction'
GROUP BY 
    ano_lancamento_filme
ORDER BY 
    ano_lancamento_filme
LIMIT 44;

# Criação da tabela da métrica de popularidade

CREATE TABLE IF NOT EXISTS metrica_popularidade AS
SELECT 
    ano_lancamento_filme,
    AVG(popularidade_filme) AS media_popularidade
FROM 
    tb_metricas_filme
WHERE 
    nome_genero_filme = 'Science Fiction'
GROUP BY 
    ano_lancamento_filme
ORDER BY 
    ano_lancamento_filme
limit 44;