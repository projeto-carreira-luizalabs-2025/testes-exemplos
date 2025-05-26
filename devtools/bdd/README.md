# Como o BDD se encaixa em Testes Python?

Em Python, ferramentas como o [behave](https://github.com/behave/behave) e o 
[pytest-bdd](https://pytest-bdd.readthedocs.io/en/stable/) permitem que você traduza esses cenários *Gherkin* em código de teste executável. 
A beleza do BDD é que os mesmos cenários que descrevem o comportamento esperado também se tornam os testes automatizados. 
Isso garante que o código implementado realmente atende às definições de negócio.

## Benefícios do BDD:

- Melhora a comunicação: Facilita o entendimento mútuo entre as partes interessadas.
- Documentação viva: Os testes BDD atuam como uma documentação sempre atualizada do comportamento do sistema.
- Foco no valor de negócio: Garante que o desenvolvimento esteja alinhado com as necessidades do negócio.
- Testes mais claros e legíveis: Facilita a manutenção e a depuração dos testes.
- Menos bugs: A clareza das especificações reduz a chance de erros e retrabalho.

## Exemplo de Script BDD com behave e Leitura de API

Vamos criar um exemplo prático que simula a leitura de dados de uma API, utilizando o `behave`.

1. Instale o behave: Nós já colocamos no [Makefile](../../Makefile), que está no raiz para fazer isto
para nós.

```shell
make requirements-dev
```
2. Crie a estrutura de diretórios: Tal como fizemos aqui:

- [features](./features/): Código _Gherkin_.
- [steps](./features/steps): Código Python.


3. [features/api_data.feature](./features/api_data.feature) (Cenário Gherkin):

Aqui temos o cenário para consultar a API.

4. [features/steps/api_data_steps.py](./features/steps/api_data_steps.py) (Implementação dos Steps):

O _passos_ para executar os cenários de testes.

5. Como Executar:

Execute a aplicação API em um terminal:

```shell
make run-api
```

Em outro terminal, navegue até a pasta `bdd` 
e execute o comando do `behave` (com o `venv`ativo):

```shell
cd devtools/bdd

behave
```

Você verá o behave executando o cenário e verificando a resposta da API.

Este exemplo mostra como o BDD, por meio de ferramentas como o `behave`, 
permite que você escreva testes que são ao mesmo tempo especificações de comportamento 
e testes automatizados. Ao adotar o BDD, sua equipe estará mais alinhada, o código será 
mais robusto e a entrega de valor de negócio será otimizada.


### Observações Importantes:

O `behave` reconhece automaticamente as palavras-chave Gherkin traduzidas para o português quando você especifica 

```
# language: pt. 
```

As palavras-chave que você pode usar são:

- Funcionalidade (Feature)
- Cenário (Scenario)
- Esquema do Cenário (Scenario Outline)
- Contexto (Background)
- Dado (Given)
- Quando (When)
- Então (Then)
- E (And)
- Mas (But)
- Exemplos (Examples)

Sobre concordância: Certifique-se de que a frase exata que você usa no seu arquivo `.feature` 
(por exemplo, "`Dada a API disponível`") corresponda exatamente à string que você passa para o decorador no seu arquivo de steps 

```python
@dado('que a API está disponível em "{url}"').
```

( ⚠️ Não testamos a tradução do decorador!)

O documento [pytest-bdd.md](./pytest-bdd.md) mostra o mesmo exemplo com o `pytest-bdd`.