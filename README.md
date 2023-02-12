# Python & TDD: Testes unitários

## Introdução
Este é um projeto de estudos, com o objetivo de criar alguns testes em cima de um código desenvolvido em Python, afim de conhecer um pouco mais de algumas ferramentas e conceitos na parte de testagem de código. Os testes unitários, visam de uma forma pratica garantir que cada funcionalidade da aplicação respeite as regras de negócio do projeto, recebendo determinadas informações e retornando determinados dados. Quando o projeto está em seu início, ainda pequeno é fácil julgar se o código respeita ou não as regras de negócio. Porém, conforme o projeto crescer, a hierarquia do projeto aumentar, existir mais módulos, classes e métodos, e surgir mais regras de negócio, logo cada funcionalidade terá que respeitar inúmeras regras.
Os testes unitário, que é o foco destes estudo, testa método ou pequena parte do código por vez.

## 1. Problema
 Temos uma pequena aplicação, desenvolvida para um Fintec chamada Bytebank(empresa inventada), esta aplicaçao possui uma classe que contem as informações dos funcionários. Mas sera que tudo esta funcionando como deveria, as regras de negócio foram cumpridas? Para isto iremos desenvolver um conjunto de testes visando garantir o cumprimento de todas as regras. 

## 2. Técnicas Usadas:
- Pytest: Para testar código iremos usar um Framework especializado em testes e um dos mais utilizados para esta linguagem o Pytest.
- Test-Driven Development: Iremos utilizar como lógico de testagem, começar pelo Testes -> Código -> Refatoração. Para executar novas funcoes pedidas na implementacao do programa e aplicar testes nas partes ja prontas do código.
-
