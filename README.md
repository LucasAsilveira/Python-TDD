# Python & TDD: Testes unitários


## Introdução

Este é um projeto de estudos, com o objetivo de criar alguns testes em cima de um código desenvolvido em Python, afim de conhecer um pouco mais de algumas ferramentas e conceitos na parte de testagem de código. Os testes unitários, visam de uma forma pratica garantir que cada funcionalidade da aplicação respeite as regras de negócio do projeto, recebendo determinadas informações e retornando determinados dados. Quando o projeto está em seu início, ainda pequeno é fácil julgar se o código respeita ou não as regras de negócio. Porém, conforme o projeto crescer, a hierarquia do projeto aumentar, existir mais módulos, classes e métodos, e surgir mais regras de negócio, logo cada funcionalidade terá que respeitar inúmeras regras.
Os testes unitário, que é o foco destes estudo, testa método ou pequena parte do código por vez.

## 1. Problema

 Temos uma pequena aplicação, desenvolvida para um Fintec chamada Bytebank(empresa inventada), esta aplicaçao possui uma classe que contem as informações dos funcionários. Mas sera que tudo esta funcionando como deveria, as regras de negócio foram cumpridas? Para isto iremos desenvolver um conjunto de testes visando garantir o cumprimento de todas as regras. 

## 2. Técnicas Usadas:

- Pytest: Para testar código iremos usar um Framework especializado em testes e um dos mais utilizados para esta linguagem o Pytest.
- Test-Driven Development: Iremos utilizar como lógico de testagem, começar pelo Testes -> Código -> Refatoração. Para executar novas funcoes pedidas na implementacao do programa e aplicar testes nas partes ja prontas do código.
- Given-When-Then: Metodologia agil para desenvolvimento de testes, GIVEN - Dado(contexto), WHEN - Quando(Ação), Then - Então(Desfecho).
- Pytest-cov:  Torna possível especificar o diretório onde está nosso arquivo que queremos realizar os testes, e rodando, fazer uma varredura no código e indicar se nosso código está 100% coberto por testes.

## 3.0 Etapas do projeto

Primeiro testamos os metodos ja existentes na classe bytebank. Utiliando o pytest, foram feito teste na regra de idade e logo ja descobrimos um erro, pois a regra de negócio exigia a entrada de data de nascimento dd/mm/aaaa. Corrigimos esta regra. 
Foram realizados 4 testes para todos os metodos e no final incluso uma nova regra onde seguindo a metodologia TDD fizemos primeiro o teste, depois foi desenvolvido o novo metodo para passar nestes teste e em seguida refatoramos o metodo, o metodo incluso foi para calcular uma bonificação ao funcionarios com um exception, para nao realizar o pagamento deste bonus caso o funcionario tivesse um bous maior do que 1000 Reais a receber. 
O codigo dos testes realizado pode ser encontrado nes link[https://github.com/LucasAsilveira/Python-TDD/blob/main/tests/test_bytebank.py] do repositorio do projeto.
Para garantir a cobertura de todos os testes foi usado o pytest-cov, ao rodar o teste de cobertura verificou que apenas uma função não estava coberta pelos testes, esta era a funcao string, que realmente não era necessitava de teste, assim foi configurado no arquivo .coveragerc, utilizando o exclude_lines, para que o converge ignorasse este metodo. 

## 4.0 Conclusão

Através deste programa simples pudemos aprender um pouco mais sobre testes unitários, vendo sua importancia e simplicidade e praticiadade de implementação. Como o objtivo de projeto de estudo era de introduzir o conceito de testagem e aprender um pouco mais este foi cumprido. Levando em consideraçao que dependendo da complexidade do projeto por vezes pode ser bem mais trabalhos implementar testes unitarios. 
