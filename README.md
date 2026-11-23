# Organizador de Tarefas

> Sistema de gerenciamento e histórico de tarefas via terminal (CLI) desenvolvido em Python.

---

## Sobre

O **Organizador de Tarefas** é uma aplicação de linha de comando desenvolvida em Python para organizar rotinas diárias, acompanhar tarefas pendentes e manter um histórico mensal de atividades concluídas. A ideia surgiu de uma sugestão de portfólio para aplicar fundamentos essenciais de programação na prática — estruturando a lógica de forma modular e salvando os dados de maneira persistente sem depender de interfaces complexas.

---

## Funcionalidades atuais

* Adicionar novas tarefas com registro automático de data de criação
* Concluir tarefas e atualizar status
* Listar tarefas pendentes
* Listar tarefas concluídas
* Visualizar todas as tarefas cadastradas
* Consultar histórico de tarefas concluídas filtrado por mês (`MM`)
* Persistência de dados em arquivo `JSON` (`tarefas.json`)
* Estrutura modularizada (`__main__.py`, `menu.py`, `tarefas.py`, `utils.py`)
* Menu interativo no terminal utilizando `match/case`
* Tratamento de erros e entradas inválidas com `try / except`
* Função dinâmica para ajustar a linha separadora de acordo com o tamanho do texto da tarefa

---

## Planejamento futuro

* Opção de confirmação antes de retornar ao menu principal para melhorar a experiência de leitura no terminal
* Exportação de relatórios ou integração futura com banco de dados

---

## Tecnologias

* Python
* JSON
* Git

---

## Objetivo

Este projeto foi criado para praticar lógica de programação, manipulação de arquivos e arquitetura modular em Python, construindo uma ferramenta funcional para o dia a dia enquanto evoluo meu portfólio como desenvolvedora.

---

## Status

EM DESENVOLVIMENTO. O projeto está ativo e recebendo melhorias contínuas de usabilidade e tratamento de exceções.