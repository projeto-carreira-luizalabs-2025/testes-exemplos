# Sonaqube

Qualidade com o Sonarqube, para isto execute em um terminal:

```shell
# Inicie desta pasta o docker-compose,
# o comando abaixo está sendo executado da raiz do projeto
docker-compose -f ./devtools/quality/docker-compose-sonarqube.yml up
```

⚠ Este Sonar *não* possui _volumes_ persistentes tal como temos em outros repositórios exemplos.

Acessando depois de subir:

> http://localhost:9000

Depois de acessar, vão te obrigar a mudar a senha `admin`. Sugestão, deixa
como `senha`.

Não se esqueçam de gerar o token.
