/* E01
Apresente a query para listar todos os livros publicados após 
2014. Ordenar pela coluna cod, em ordem crescente, as linhas.
Atenção às colunas esperadas no resultado final: cod, titulo,
autor, editora, valor, publicacao, edicao, idioma */

SELECT l.cod, l.titulo, a.codautor AS autor, e.codeditora AS editora, l.valor, l.publicacao, l.edicao, l.idioma
FROM livro l
INNER JOIN autor a ON l.autor = a.codautor
INNER JOIN editora e ON l.editora = e.codeditora
WHERE l.publicacao > '2015-01-01'
ORDER BY l.cod ASC;

/* E02
Apresente a query para listar os 10 livros mais
caros.Ordenar as linhas pela coluna valor, em ordem
decrescente.  Atenção às colunas esperadas no resultado
final:  titulo, valor. */

SELECT titulo, valor
FROM livro
ORDER BY valor DESC
LIMIT 10;

/* E03
Apresente a query para listar as 5 editoras
com mais livros na biblioteca. O resultado
deve conter apenas as colunas quantidade, 
nome, estado e cidade. Ordenar as linhas pela 
coluna que representa a quantidade de livros em 
ordem decrescente.
*/

SELECT COUNT(l.cod) AS quantidade, e.nome, en.estado, en.cidade
FROM livro l
INNER JOIN editora e ON l.editora = e.codeditora
INNER JOIN endereco en ON e.endereco = en.codendereco
GROUP BY e.nome, en.estado, en.cidade
ORDER BY quantidade DESC
LIMIT 5;

/* E04
Apresente a query para listar a quantidade de livros publicada
 por cada autor. Ordenar as linhas pela coluna nome (autor), 
 em ordem crescente. Além desta, apresentar as colunas codautor,
  nascimento e quantidade (total de livros de sua autoria).
*/
SELECT a.codautor, a.nome, a.nascimento, COUNT(l.cod) AS quantidade
FROM autor a
LEFT JOIN livro l ON a.codautor = l.autor
GROUP BY a.codautor, a.nome, a.nascimento
ORDER BY a.nome ASC;

/* E05
Apresente a query para listar o nome dos autores que publicaram livros
 através de editoras NÃO situadas na região sul do Brasil. Ordene o 
 resultado pela coluna nome, em ordem crescente. Não podem haver nomes
  repetidos em seu retorno.
*/
SELECT DISTINCT a.nome
FROM autor a
INNER JOIN livro l ON a.codautor = l.autor
INNER JOIN editora e ON l.editora = e.codeditora
INNER JOIN endereco end ON e.endereco = end.codendereco
WHERE end.estado NOT IN ('RIO GRANDE DO SUL', 'PARANÁ')
ORDER BY a.nome ASC;

select * from endereco e ;


/* E06
Apresente a query para listar o autor com maior número de livros publicados.
 O resultado deve conter apenas as colunas codautor, nome, quantidade_publicacoes.
 */
SELECT
    a.codautor,
    a.nome,
    COUNT(*) AS quantidade_publicacoes
FROM
    autor a
JOIN
    livro l ON a.codautor = l.autor
GROUP BY
    a.codautor, a.nome
ORDER BY
    quantidade_publicacoes DESC
LIMIT 1;

/* E07
Apresente a query para listar o nome dos autores com 
nenhuma publicação. Apresentá-los em ordem crescente.
 */
SELECT nome
FROM autor
WHERE codautor NOT IN (SELECT DISTINCT autor FROM livro)
ORDER BY nome ASC;













