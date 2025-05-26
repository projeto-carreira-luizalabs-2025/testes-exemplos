# language: pt

Funcionalidade: Processamento de Dados de API

  """
  Como cliente desejo acessar a API XPTO para acessar seus dados e testar
  seus valores.
  """

  Cenário: Leitura de dados de uma API e verificação de chave e valor
    Dado a API está disponível em "http://localhost:5000/sample"
    Quando eu faço uma requisição GET para a API
    Então a resposta deve ter um código de status 200
    E o JSON da resposta deve conter a chave "chave" com o valor "chave01"
    E o JSON da resposta deve conter a chave "valor" com o valor 1