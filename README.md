# Trabalho Final - QA: Automação de Testes

Projeto de automação de testes desenvolvido para a disciplina de Teste e Qualidade de Software.

## Tecnologias Utilizadas

- Python 3.11+
- pytest
- requests (testes de API)
- Selenium (testes Web)
- webdriver-manager
- GitHub Actions (CI/CD)

## Estrutura do Projeto

trabalho-qa-final/
├── api_tests/          # Testes automatizados de API
│   ├── tests/
│   │   ├── test_pet.py
│   │   ├── test_store.py
│   │   └── test_user.py
│   └── requirements.txt
├── web_tests/          # Testes automatizados Web (Selenium)
│   ├── pages/
│   │   ├── login_page.py
│   │   ├── inventory_page.py
│   │   ├── cart_page.py
│   │   └── checkout_page.py
│   ├── tests/
│   │   └── test_e2e_compra.py
│   └── requirements.txt
└── .github/
└── workflows/
└── ci.yml

## Projetos

### 1. Automação de API - Swagger Petstore
- **Base URL:** https://petstore.swagger.io/v2
- **Cobertura:** Pet, Store e User (CRUD completo)
- **Total de testes:** 12

### 2. Automação Web - SauceDemo
- **URL:** https://www.saucedemo.com/
- **Fluxo E2E:** Login → Adicionar produto → Checkout → Confirmação
- **Design Pattern:** Page Object Model (POM)

## Como Executar

### Testes de API
```bash
cd api_tests
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
pytest tests/ -v
```

### Testes Web
```bash
cd web_tests
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
pytest tests/ -v
```

## CI/CD

O projeto possui pipeline configurada no GitHub Actions que executa automaticamente os testes de API e Web a cada push na branch `main`.

## Resultados

### API - 12/12 testes passando
![API Tests](https://github.com/joaomaa/trabalho-qa-final/actions/workflows/ci.yml/badge.svg)

### Web - Pipeline rodando em modo headless