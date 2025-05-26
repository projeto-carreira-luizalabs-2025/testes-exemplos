# testes exemplos

Nosso projeto exemplo sobre testes com o Python 🐍. 
(O texto a seguir foi gerado por IA 🤖)


Bem-vindo ao mundo dos testes em Python! Como desenvolvedor, entender e aplicar testes em seus projetos 
é fundamental para garantir a qualidade do seu código, facilitar a manutenção e impulsionar sua carreira. 
Este material irá guiá-lo pelos conceitos essenciais, a importância dos testes, como escrevê-los e as metodologias TDD e BDD.

## A Importância dos Testes Testing

Imagine que você está construindo um castelo de cartas. Cada carta representa uma parte do seu código. 
Se uma carta estiver mal posicionada (um bug 🪲), todo o castelo pode desmoronar. Os testes funcionam como uma 
rede de segurança, verificando se cada "carta" está firme e no lugar certo.

Por que testar é crucial?

- Garantia de Qualidade: Testes ajudam a identificar e corrigir bugs antes que cheguem aos usuários, garantindo um software mais estável e confiável.
- Facilita a Manutenção: Com testes, você pode fazer alterações e refatorações no código com mais segurança, sabendo que os testes irão alertá-lo se algo quebrar.
- Melhora o _projeto_ do Código: Escrever testes muitas vezes leva a um código mais modular, coeso e com responsabilidades bem definidas.
- Documentação Viva: Testes bem escritos servem como uma forma de documentação, demonstrando como o código deve se comportar.
- Confiança para Entregar: Ter uma suíte de testes robusta aumenta a confiança da equipe ao entregar novas funcionalidades ou correções.

## Como Escrever Testes em Python ✍️

Python oferece diversas ferramentas para escrever testes, sendo o [unittest](https://docs.python.org/3/library/unittest.html) 
(integrado à biblioteca padrão) e o [pytest](https://docs.pytest.org/en/stable/) (uma biblioteca de terceiros muito popular) os mais comuns. 
Vamos focar no pytest por sua simplicidade e poder.

### Instalando o pytest:

```bash
pip install pytest
```

### Escrevendo um Teste Simples:

Vamos supor que temos uma função soma em um arquivo chamado calculadora.py:


```python
# calculadora.py
def soma(a, b):
  return a + b
```

Agora, vamos criar um arquivo de teste chamado test_calculadora.py:

```python
# test_calculadora.py
from calculadora import soma

def test_soma_positivos():
  assert soma(2, 3) == 5

def test_soma_negativos():
  assert soma(-1, -1) == -2

def test_soma_misto():
  assert soma(5, -3) == 2
```

### Executando os Testes:

No terminal, navegue até o diretório do seu projeto e execute o comando:

```sh
pytest
```

O pytest encontrará automaticamente os arquivos e funções de teste (que começam com `test_`) e os executará, mostrando o resultado.

O pytest oferece recursos poderosos para tornar seus testes mais eficientes e organizados.

### Fixtures: Preparando o Cenário 🛠️

Fixtures são funções que o pytest executa antes (e às vezes depois) das suas funções de teste. Elas são usadas para fornecer dados, objetos ou qualquer estado necessário para os testes, evitando a repetição de código.

### Como definir e usar uma fixture:

```python
# test_calculadora.py
import pytest
from calculadora import soma

@pytest.fixture
def numeros_basicos():
  """Retorna um dicionário com números para testes."""
  return {"a": 2, "b": 3, "esperado": 5}

def test_soma_com_fixture(numeros_basicos):
  """Testa a soma usando dados de uma fixture."""
  assert soma(numeros_basicos["a"], numeros_basicos["b"]) == numeros_basicos["esperado"]
```

Neste exemplo, `numeros_basicos` é uma fixture. O pytest a executa e injeta seu resultado 
(o dicionário) como argumento na função `test_soma_com_fixture`.

### `conftest.py`: Compartilhando Fixtures 🤝

Se você precisar usar a mesma fixture em vários arquivos de teste, pode defini-la em um arquivo especial chamado 
`conftest.py` na raiz do seu diretório de testes. O `pytest` automaticamente descobre e disponibiliza essas 
fixtures para todos os testes.

```python
# conftest.py (na pasta de testes)
import pytest

@pytest.fixture(scope="session") # 'scope' define a frequência de execução
def dados_globais():
  """Fixture disponível para toda a sessão de testes."""
  print("\nConfigurando dados globais...")
  yield {"usuario": "admin", "senha": "123"}
  print("\nLimpando dados globais...")
```

### `pytest.raises`: Testando Exceções ⚠️

É crucial verificar se seu código lida corretamente com situações de erro, lançando as exceções esperadas. 
O `pytest.raises()` é um gerenciador de contexto que verifica se um bloco de código lança uma exceção específica.

```python
# test_calculadora.py
import pytest
from calculadora import divide

def test_divide_por_zero_lanca_excecao():
  """Verifica se a divisão por zero lança ValueError."""
  with pytest.raises(ValueError):
    divide(10, 0)

def test_divide_por_zero_mensagem_excecao():
  """Verifica a mensagem da exceção."""
  with pytest.raises(ValueError, match="Não é possível dividir por zero"):
    divide(10, 0)
```

O teste passa se a exceção `ValueError` for lançada dentro do bloco `with`. 
Você também pode usar `match` para verificar se a mensagem da exceção contém um texto específico.

## Uma espiada no unittest 🧐

O [unittest](https://docs.python.org/3/library/unittest.html)  
é o framework de testes embutido do Python e adota uma abordagem mais orientada a objetos, inspirada nos frameworks 
[xUnit](https://xunit.net/).

### Estrutura com Classes:

Com `unittest`, os testes são geralmente agrupados em classes que herdam de `unittest.TestCase`.

```python
import unittest
from calculadora import soma

class TestCalculadora(unittest.TestCase):

  def test_soma_simples(self):
    self.assertEqual(soma(1, 2), 3)

  def test_soma_negativa(self):
    self.assertEqual(soma(-1, -1), -2)

# Para rodar (geralmente via linha de comando):
# python -m unittest test_calculadora_unittest.py
```

### Métodos `setUp` e `tearDown`: Preparação e Limpeza 🧹

O `unittest` oferece métodos especiais que são executados antes e depois de cada teste (ou de toda a classe de testes), semelhantes às fixtures do pytest, mas com uma estrutura diferente:

- `setUp(self)`: Executado antes de cada método de teste (`test_*`). Útil para criar objetos ou estados que cada teste usará.
- `tearDown(self)`: Executado depois de cada método de teste. Útil para limpar recursos criados no setUp.
- `setUpClass(cls)`: Executado uma vez, antes de todos os testes da classe.
- `tearDownClass(cls)`: Executado uma vez, depois de todos os testes da classe.

```python
import unittest
# ... (import da calculadora)

class TestCalculadoraComSetup(unittest.TestCase):

    def setUp(self):
        print("\nExecutando setUp: Preparando para o teste...")
        # Poderia criar um objeto Calculadora aqui, por exemplo
        self.a = 10
        self.b = 5

    def tearDown(self):
        print("Executando tearDown: Limpando após o teste...")
        # Limpar recursos, se necessário

    def test_soma(self):
        self.assertEqual(soma(self.a, self.b), 15)

    def test_divide(self):
        self.assertEqual(divide(self.a, self.b), 2)
```

## Mocking: Simulando o Mundo Real 🎭

Ao testar uma unidade de código (como uma função), muitas vezes ela depende de outras partes do sistema ou de serviços externos (APIs, bancos de dados). Para isolar a unidade que você está testando e evitar dependências externas (que podem ser lentas ou instáveis), usamos _Mocks_.

Mocking é a prática de substituir essas dependências por objetos simulados (ou "falsos") que se comportam da maneira que você espera durante o teste.

### Por que usar Mocks?

- Isolamento: Testa apenas o código que você quer testar, sem interferência externa.
- Velocidade: Evita chamadas lentas a redes ou bancos de dados.
- Controle: Permite simular cenários específicos, como respostas de erro de uma API.
- Determinismo: Garante que seus testes produzam sempre o mesmo resultado.

### Ferramentas para Mocking:

O Python oferece o módulo `unittest.mock` (que pode ser usado com `pytest` também!), que é extremamente poderoso. Existem também bibliotecas como [pytest-mock](https://pytest-mock.readthedocs.io/en/latest/) que facilitam o uso de 
mocks com pytest.

### Conceito Básico (com unittest.mock):

Imagine uma função que busca dados de uma API:

```python
import requests

def buscar_dados_usuario(user_id):
  response = requests.get(f"https://api.exemplo.com/users/{user_id}")
  response.raise_for_status() # Lança exceção se houver erro HTTP
  return response.json()
```

Para testar `buscar_dados_usuario` sem chamar a API real, podemos "mocar" a função `requests.get()`:

```python
from unittest.mock import patch
import unittest
# ... (import da função buscar_dados_usuario)

class TestAPI(unittest.TestCase):

  @patch('requests.get') # 'patch' substitui o alvo durante o teste
  def test_buscar_dados_sucesso(self, mock_get):
    # Configura o mock para retornar um objeto com o método json()
    mock_response = mock_get.return_value
    mock_response.json.return_value = {"id": 1, "nome": "Fulano"}
    mock_response.raise_for_status.return_value = None # Não faz nada

    dados = buscar_dados_usuario(1)

    # Verifica se requests.get foi chamado com a URL correta
    mock_get.assert_called_once_with("https://api.exemplo.com/users/1")
    # Verifica se o resultado é o esperado
    self.assertEqual(dados, {"id": 1, "nome": "Fulano"})
```

Com o `patch`, substituímos `requests.get` por um objeto Mock. Podemos então configurar esse Mock para retornar o que quisermos e verificar se ele foi chamado como esperado.

## Tipos de Testes ⚙️

Existem vários tipos de testes, cada um com um foco específico. Os mais comuns são:

- Testes Unitários: Verificam a menor unidade de código isoladamente (geralmente uma função ou método). São rápidos de escrever e executar. Os exemplos acima são testes unitários.
- Testes de Integração: Verificam se diferentes partes do seu sistema (módulos, classes, serviços externos) funcionam corretamente juntas.
- Testes de Ponta a Ponta (End-to-End - E2E): Simulam o fluxo completo de um usuário interagindo com a aplicação, desde a interface até o banco de dados. São mais complexos e lentos.
- Testes de Aceitação: Verificam se o sistema atende aos requisitos do negócio e às expectativas do cliente.

## TDD: Desenvolvimento Orientado a Testes 💡

TDD (Test-Driven Development) é uma abordagem de desenvolvimento onde você escreve os testes antes de escrever o código da funcionalidade. O ciclo TDD é conhecido como "Red-Green-Refactor":

1. Red (Vermelho): Escreva um teste que falhe (porque a funcionalidade ainda não existe).
2. Green (Verde): Escreva o código mínimo necessário para fazer o teste passar.
3. Refactor (Refatorar): Melhore o código escrito (limpeza, otimização) sem alterar seu comportamento (garantido pelos testes).

### Benefícios do TDD:

- Garante que todo o código tenha cobertura de testes.
- Ajuda a pensar nos requisitos antes de codificar.
- Promove um design de código mais simples e focado.
- Reduz a depuração, pois os bugs são encontrados rapidamente.

## BDD: Desenvolvimento Orientado ao Comportamento 🗣️

BDD (Behavior-Driven Development) é uma extensão do TDD que foca no comportamento do sistema do ponto de vista do usuário ou do negócio. Ele usa uma linguagem natural (como o Gherkin) para descrever os cenários de teste, facilitando a comunicação entre desenvolvedores, testadores e stakeholders (pessoas de negócio).

### Estrutura Gherkin (Dado/Quando/Então):

```gherkin
Funcionalidade: Login de Usuário

  Cenário: Login bem-sucedido com credenciais válidas
    Dado que eu esteja na página de login
    Quando eu preencho o campo "usuário" com "meu_usuario"
    E eu preencho o campo "senha" com "minha_senha_segura"
    E eu clico no botão "Entrar"
    Então eu devo ser redirecionado para a página inicial
    E eu devo ver a mensagem "Bem-vindo, meu_usuario!"
```

### Benefícios do BDD:

- Melhora a comunicação e o alinhamento entre todas as partes interessadas.
- Foca no valor de negócio das funcionalidades.
- Cria uma documentação viva e compreensível.
- Incentiva a colaboração e a compreensão compartilhada.

## Cobertura de Código com `pytest-cov` 📊

Saber que seus testes passam é ótimo, mas como saber quanto do seu código esses testes realmente exercitam? É aí que entra a *cobertura de código*.

A cobertura de código é uma métrica que indica a porcentagem do seu código-fonte que foi executada durante a execução da sua suíte de testes. Ela ajuda a identificar partes do seu código que não estão sendo testadas e que, portanto, podem conter bugs ocultos.

*Atenção*: Uma alta cobertura (90-100%) é geralmente desejável, mas não garante a ausência de bugs. É possível executar uma linha de código sem testar todas as suas lógicas ou cenários de borda. Use a cobertura como um guia, não como um objetivo absoluto.

### Medindo a Cobertura com `pytest-cov`

O [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/) é um plugin para o pytest que integra a medição de cobertura de forma muito simples.

#### Instalação:

```bash
pip install pytest-cov
```

#### Executando Testes com Cobertura:

Para executar seus testes e gerar um relatório de cobertura no terminal, use a flag `--cov`:

```shell
pytest --cov=seu_modulo
```

Substitua `seu_modulo` pelo nome do diretório ou módulo Python que você deseja analisar (Nos nossos projetos estamos
usando `app`). Você verá um relatório no terminal mostrando a porcentagem de cobertura para cada arquivo.

### Gerando Relatórios Detalhados:

Para uma análise mais aprofundada, você pode gerar relatórios em formatos diferentes:

- Relatório HTML: Cria um site interativo onde você pode navegar pelos seus arquivos e ver exatamente quais linhas foram ou não cobertas.


```shell
pytest --cov=seu_modulo --cov-report=html
```

Isso criará um diretório `htmlcov`. Abra o arquivo `index.html` em seu navegador.

- Relatório XML: Este formato é muito útil para integração com ferramentas de análise de qualidade de código, como o SonarQube.

```shell
pytest --cov=seu_modulo --cov-report=xml
```

Isso criará um arquivo coverage.xml no seu diretório.

#### Integrando com SonarQube 📡

O [SonarQube](https://www.sonarsource.com/products/sonarqube/) é uma plataforma open-source líder para 
inspeção contínua da qualidade do código. Ele realiza análises estáticas para detectar bugs, 
"code smells" (maus cheiros no código) e vulnerabilidades de segurança. Além disso, ele rastreia métricas como cobertura de testes, duplicação de código e complexidade.

Enviar seus relatórios de cobertura para o SonarQube permite que você e sua equipe tenham uma visão centralizada e histórica da qualidade do seu projeto Python.

#### Passos para Enviar a Cobertura para o SonarQube:

1. Gere o Relatório de Cobertura: Como vimos acima, gere o relatório no formato XML:

```shell
pytest --cov=seu_modulo --cov-report=xml
```

Certifique-se de que o arquivo `coverage.xml` foi criado.

2. Instale e Configure o SonarScanner: O SonarScanner é a ferramenta de linha de comando que analisa seu projeto e envia os resultados para o servidor SonarQube. Você precisará baixá-lo do site oficial do SonarQube e garantir que ele esteja acessível no seu `PATH` ou que você use o caminho completo para executá-lo.

3. Crie o arquivo `sonar-project.properties`: Na raiz do seu projeto, crie um arquivo chamado `sonar-project.properties`. Este arquivo diz ao SonarScanner como analisar seu projeto. Um exemplo básico para um projeto Python seria:

```properties
# Identificação única do projeto no SonarQube
sonar.projectKey=meu-projeto-python-unico
sonar.projectName=Meu Projeto Python Incrível

# Versão do projeto (opcional, mas recomendado)
sonar.projectVersion=1.0

# Onde está o código-fonte
sonar.sources=.

# Idioma do projeto
sonar.language=py

# Caminho para o relatório de cobertura gerado pelo pytest-cov
# Certifique-se de que o caminho está correto!
sonar.python.coverage.reportPaths=coverage.xml

# Endereço do seu servidor SonarQube
sonar.host.url=http://localhost:9000 # Ou o endereço do seu servidor

# Token de autenticação (gere no seu perfil do SonarQube)
# É mais seguro passar isso via linha de comando ou variável de ambiente
# sonar.login=seu_token_aqui

# Codificação dos arquivos
sonar.sourceEncoding=UTF-8
```

Importante: Nunca faça o _commit_ de tokens ou senhas diretamente no seu sonar-project.properties em repositórios públicos. Use variáveis de ambiente ou passe o token via linha de comando (-Dsonar.login=seu_token_aqui).

4. Execute o SonarScanner: Navegue até a raiz do seu projeto (onde está o sonar-project.properties) no terminal e execute o comando do SonarScanner:

```
pysonar-scanner -Dsonar.login=seu_token_aqui
```

Após a execução, o SonarScanner enviará a análise e o relatório de cobertura para o seu servidor SonarQube. Você poderá então acessar a interface web do SonarQube para ver os resultados detalhados, incluindo a métrica de cobertura de testes integrada com outras análises de qualidade.

## Conclusão ✨

Aprender sobre testes e incorporá-los ao seu fluxo de trabalho é um passo crucial na sua jornada como desenvolvedor Python. Comece com testes unitários simples, explore diferentes tipos de testes e experimente as abordagens TDD e BDD. Lembre-se: testes não são um custo adicional, mas um investimento na qualidade e na sustentabilidade do seu software. Bons testes! 🚀

## Projeto local

Seguem instruções rápidas:

```shell
# Instalando o ambiente virtual
make build-venv
# Iniciando o venv
source venv/bin/activate
# Instalando os pacotes locais
make requirements-dev

# Testes locais
make test

# Cobertura
make coverage

# Sonar
export SONAR_TOKEN=<informeseutoken>
pysonar-scanner -Dsonar.projectVersion=$(date '+%Y%m%d-%H%M%S')
```