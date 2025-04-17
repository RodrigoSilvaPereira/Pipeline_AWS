# Entregas da Sprint Atual

Neste arquivo você irá encontrar entregas da Sprint corrente. Observe que existem 4 diretórios para analisar referente a autal sprint: **certificados**, **desafio** e **evidências**.

- O diretório **certificados** corresponde ao local onde você irá encontrar os certificados obtidos no decorrer da sprint.
- O diretório **evidências** você pode encontrar imagens ou vídeos demonstrando a execução/resultados de atividades, quando necessário.
- O diretório **desafio** é o local onde você irá encontrar a resolução do que se pede no desafio, todos recursos que são considerados importantes para a resolução do desafio você encontra aqui.

## Certificados

![Data & Analytics - PB - AWS - Novo - 9/10](Certificados/Data%20&%20Analytics%20-%20PB%20-%20AWS%20-%20Novo%20-%209.10.jpg)

## Desafio

Nesta seção, você encontrará a resolução do desafio proposto, juntamente com todos os recursos importantes para a sua execução.

### Resumo do Desafio

Nesta etapa do projeto, refinamos dados da camada "trusted" do Amazon S3, que envolviam dois arquivos Parquet de origens diferentes: TMDB e API. Utilizamos AWS Glue e Spark para realizar a junção desses dados com base em colunas de referência, transformando-os em um único arquivo Parquet na camada "refined". Este processo envolveu a leitura dos arquivos Parquet, a junção dos dados das fontes TMDB e API, a exploração da coluna "genero_filme" para desaninhar os gêneros de cada filme, seleção e renomeação de colunas para garantir consistência nos dados. O resultado foi armazenado de volta no S3, estruturado e pronto para ser utilizado em análises subsequentes utilizando serviços como Athena e QuickSight.

![Códigos e Dados](Desafio/)
