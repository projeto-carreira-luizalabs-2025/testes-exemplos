import httpx
from behave import *
import time


@given('a API está disponível em "{url}"')
def step_impl(context, url):
    context.api_url = url
    # XXX Poderia iniciar a aplicação aqui numa thread
    time.sleep(1)  # Dá um tempo para o servidor iniciar


@when("eu faço uma requisição GET para a API")
def step_impl(context):
    try:
        context.response = httpx.get(context.api_url)
    except httpx.TimeoutException as e:
        assert False, f"Não foi possível conectar à API: {e}"


@then("a resposta deve ter um código de status {status_code:d}")
def step_impl(context, status_code: int):
    assert (
        context.response.status_code == status_code
    ), f"Esperado status {status_code}, mas obteve {context.response.status_code}"


@then('o JSON da resposta deve conter a chave "{key}" com o valor "{value}"')
def step_impl(context, key, value):
    response_json = context.response.json()
    assert (
        key in response_json
    ), f"A chave '{key}' não foi encontrada no JSON da resposta."
    assert (
        str(response_json[key]) == value
    ), f"O valor da chave '{key}' esperado era '{value}', mas obteve '{response_json[key]}'"


@then('o JSON da resposta deve conter a chave "{key}" com o valor {value:d}')
def step_impl(context, key, value):
    response_json = context.response.json()
    assert (
        key in response_json
    ), f"A chave '{key}' não foi encontrada no JSON da resposta."
    assert (
        response_json[key] == value
    ), f"O valor da chave '{key}' esperado era '{value}', mas obteve '{response_json[key]}'"
