# Desafio Final: Projeto em Docker

Bem-vindo ao Desafio Final do Curso de Docker! Este projeto demonstra suas habilidades na criação e gerenciamento de contêineres Docker.

## Etapas do Projeto:

### Etapa 1: Construção da Imagem e Execução do Container

Nesta etapa, o desafio é construir uma imagem a partir de um arquivo Dockerfile que execute o código "carguru.py". Após a construção da imagem, o objetivo é executar um container a partir dessa imagem.

[Ver Etapa 1](Etapa-1/Comandos.ipynb)

### Etapa 2: Reutilização de Containers

Na segunda etapa, investigamos se é possível reutilizar containers Docker. Se for possível, você deve apresentar o comando necessário para reiniciar um dos containers parados em seu ambiente Docker. Caso não seja possível, justifique sua resposta.

[Ver Etapa 2](Etapa-2/ReutilizandoContainer.ipynb)

### Etapa 3: Criação de Container Interativo

Nesta etapa final, o desafio é criar um container que permita receber input durante sua execução. Você deve seguir as seguintes instruções:

1. Criar um novo script Python que implementa o seguinte algoritmo:
   - Receber uma string via input.
   - Gerar o hash da string através do algoritmo SHA-1.
   - Imprimir o hash na tela, utilizando o método hexdigest.
   - Retornar ao primeiro passo.

2. Criar uma imagem Docker chamada "mascara-dados" que execute o script Python criado anteriormente.
3. Iniciar um container a partir da imagem "mascara-dados", enviando algumas palavras para mascaramento.
4. Registrar o conteúdo da etapa.

[Ver Etapa 3](Etapa-3/Comandos.ipynb)