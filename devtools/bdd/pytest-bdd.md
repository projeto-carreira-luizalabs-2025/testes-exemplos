# Cenários com o pytest-bdd

O [pytest-bdd](https://pytest-bdd.readthedocs.io/en/stable/) 
é outra excelente escolha para BDD em Python, e ele se integra de forma muito natural com o 
[pytest](https://docs.pytest.org/en/stable/), a ferramenta de teste mais popular do ecossistema Python. 
A principal diferença é que ele utiliza os fixtures do pytest para gerenciar o estado e os dados entre os passos.

Vamos recriar o mesmo exemplo de cenário com pytest-bdd.

## Exemplo de Cenário com `pytest-bdd`

1. Instale o pytest-bdd:

```shell
pip install pytest-bdd httpx pytest
```

2. Crie a estrutura de diretórios:

```
features/
├── api_data.feature
tests/
└── test_api_data.py
```

3. `features/api_data.feature` (Cenário Gherkin - pode ser em português ou inglês):

Manteremos o idioma em português.


```Gherkin

# language: pt
Funcionalidade: Processamento de Dados de API

  Cenário: Leitura de dados de uma API e verificação de chave e valor
    Dado que a API está disponível em "http://localhost:5000/sample"
    Quando eu faço uma requisição GET para a API
    Então a resposta deve ter um código de status 200
    E o JSON da resposta deve conter a chave "chave" com o valor "chave1"
    E o JSON da resposta deve conter a chave "valor" com o valor 1
```

4. `tests/test_api_data.py` (Implementação dos Steps com `pytest-bdd`):

A grande diferença aqui é como os passos são definidos e como o estado é compartilhado. 
Usaremos *fixtures* para injetar dados e objetos (como a URL da API ou a resposta) nos passos. 

(Nota: O código não foi testado!)

```python
import requests
import json
from pytest_bdd import scenario, given, when, then, parsers
import time
import pytest

# Define o cenário a ser testado. O caminho é relativo ao diretório onde pytest é executado.
# Para isso funcionar, o 'features' precisa estar acessível pelo pytest (ex: na raiz do projeto ou configurado no pytest.ini)
@scenario('../features/api_data.feature', 'Leitura de dados de uma API e verificação de chave e valor')
def test_api_data_processing():
    """Cenário de teste para processamento de dados da API."""
    pass

# --- Fixtures para os testes ---


@pytest.fixture
def api_url_fixture():
    """Fixture que fornece a URL da API"""

    # Poderíamos subir o servidor aqui? "Sim"

    return "http://localhost:5000/sample"

# --- Implementação dos passos ---

@given(parsers.parse('que a API está disponível em "{url}"'))
def api_disponivel(api_url_fixture, url):
    """Verifica se a URL da API corresponde à fixture."""
    assert api_url_fixture == url
    

@when('eu faço uma requisição GET para a API')
def faco_requisicao_get(api_url_fixture):
    """Faz a requisição GET para a API e armazena a resposta."""
    try:
        return httpx.get(api_url_fixture)
    except Exception as e:
        pytest.fail(f"Não foi possível conectar à API: {e}")

@then(parsers.parse('a resposta deve ter um código de status {status_code:d}'))
def verifica_status_code(faco_requisicao_get, status_code):
    """Verifica o código de status da resposta."""
    response = faco_requisicao_get # O retorno do passo 'when' é injetado aqui
    assert response.status_code == status_code, \
        f"Esperado status {status_code}, mas obteve {response.status_code}"

@then(parsers.parse('o JSON da resposta deve conter a chave "{key}" com o valor "{value}"'))
def verifica_json_string(faco_requisicao_get, key, value):
    """Verifica se o JSON da resposta contém a chave com o valor string."""
    response = faco_requisicao_get
    response_json = response.json()
    assert key in response_json, f"A chave '{key}' não foi encontrada no JSON da resposta."
    assert str(response_json[key]) == value, \
        f"O valor da chave '{key}' esperado era '{value}', mas obteve '{response_json[key]}'"

@then(parsers.parse('o JSON da resposta deve conter a chave "{key}" com o valor {value:d}'))
def verifica_json_int(faco_requisicao_get, key, value):
    """Verifica se o JSON da resposta contém a chave com o valor inteiro."""
    response = faco_requisicao_get
    response_json = response.json()
    assert key in response_json, f"A chave '{key}' não foi encontrada no JSON da resposta."
    assert response_json[key] == value, \
        f"O valor da chave '{key}' esperado era '{value}', mas obteve '{response_json[key]}'"
```

5. Como Executar:

No diretório "raiz" do BDD

```shell
pytest
```

Você verá o `pytest`  executando o cenário definido no `.feature` e usando os passos implementados em `test_api_data.py`.

## Principais Diferenças e Vantagens do pytest-bdd:

- Integração com `pytest`: O pytest-bdd aproveita toda a infraestrutura do pytest, incluindo suas fixtures, plugins, e a capacidade de rodar testes em paralelo. 
Isso é uma grande vantagem se você já usa pytest para outros tipos de testes.
- Fixtures: No pytest-bdd, o estado e os dados entre os passos são passados através de fixtures. No exemplo acima:
  - api_url_fixture: Retorna a URL da API.
  - Poderíamos ter outra para iniciar o servidor FastAPI.
  - O retorno do passo `@when (faco_requisicao_get)` é automaticamente injetado nos passos @then que o recebem como argumento. Isso facilita a passagem de dados.
- decorador `@scenario`: Você usa o decorador `@scenario` para vincular um teste (uma função Python) a um cenário específico no seu arquivo `.feature`.
- `parsers.parse`: Para extrair dados de strings nos seus cenários Gherkin (como a URL, códigos de status, chaves e valores), você usa `parsers.parse`.
- Sem `context`: Ao contrário do `behave`, o `pytest-bdd` não usa um objeto context global para compartilhar o estado. Tudo é feito via injeção de dependência de fixtures.

Ambas as ferramentas (`behave` e `pytest-bdd`) são excelentes para implementar BDD em Python. A escolha entre elas muitas vezes se resume 
à sua preferência pessoal e ao seu ecossistema de testes existente. Se você já utiliza pytest extensivamente, o `pytest-bdd` provavelmente será uma integração mais suave.