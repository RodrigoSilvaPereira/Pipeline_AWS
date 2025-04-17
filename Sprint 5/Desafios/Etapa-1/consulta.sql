WITH metrics AS (
    SELECT 
      COUNT(*) AS quantidade_registros,
      tipo_veiculo,
      COUNT(CASE WHEN tipo_infracao = '7455-0' THEN 1 ELSE NULL END) AS infracoes_velocidade,
      SUM(CASE WHEN tipo_infrator = 'Condutor' THEN 1 ELSE 0 END) AS quantidade_condutores,
      AVG(CAST(auinf_local_latitude AS FLOAT)) AS latitude_media,
      MAX(CAST(SUBSTR(cometimento, -4) AS INT)) AS ano_cometimento,
      SUBSTR(descricao, 1, 100) AS descricao_curta,
      MAX(date('now')) AS data_atual
    FROM 
      df
    WHERE 
      tipo_veiculo LIKE 'AUTOMOVEL%'
      AND tipo_infrator IN ('Condutor', 'Proprietário')
    GROUP BY 
      tipo_veiculo
    HAVING 
      quantidade_registros > 100
)
SELECT 
  quantidade_registros,
  tipo_veiculo,
  infracoes_velocidade,
  quantidade_condutores,
  latitude_media,
  ano_cometimento,
  descricao_curta,
  data_atual
FROM metrics ORDER BY quantidade_registros DESC;

/*
Esta consulta inclui:

- Dois operadores lógicos: AND e LIKE.
- Duas funções de agregação: COUNT() e SUM().
- Uma função condicional: CASE WHEN.
- Uma função de conversão: CAST().
- Uma função de data: date('now').
- Uma função de string: SUBSTR().

Essa consulta filtra os dados de acordo com a condição especificada, realiza agregações, converte tipos de dados, extrai parte de uma string e retorna a data atual.

*/