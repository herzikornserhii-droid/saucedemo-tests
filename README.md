# SauceDemo Test Automation Portfolio

[![Tests](https://github.com/herzikornserhii-droid/saucedemo-tests/actions/workflows/tests.yml/badge.svg)](https://github.com/herzikornserhii-droid/saucedemo-tests/actions/workflows/tests.yml)

## Overview / Überblick

**EN:** End-to-end test automation portfolio built by a Manual QA Engineer (8+ years) transitioning into Test Automation. The project covers both UI and API testing, follows the Page Object Model, and runs automatically in CI on every push.

**DE:** End-to-End-Testautomatisierungs-Portfolio, erstellt von einem Manual QA Engineer (8+ Jahre) mit Wechsel in die Testautomatisierung. Das Projekt umfasst UI- und API-Tests, folgt dem Page Object Model und läuft bei jedem Push automatisch in der CI.

## Tech Stack

- **Language:** Python 3.13
- **UI Testing:** Playwright, pytest-playwright
- **API Testing:** requests
- **Framework:** pytest (fixtures, parametrization, xfail)
- **Architecture:** Page Object Model (POM)
- **CI/CD:** GitHub Actions
- **Secrets:** python-dotenv, GitHub Secrets

## Test Coverage / Testabdeckung

### UI Tests (saucedemo.com)
- Login: positive, negative, and parametrized scenarios
- Cart: add-to-cart and item count verification
- Checkout: full end-to-end purchase flow
- Bug detection: documented known bug via `xfail` (problem_user broken images)

### API Tests (reqres.in)
- **Full CRUD:** GET (200), POST (201), PUT (200), DELETE (204)
- **JSON body validation** of responses
- **Negative tests:** non-existent resource (404), missing required field (400)
- **Parametrized tests:** multiple user IDs validated against expected status codes

### CI/CD
- Automated test runs on every push and pull request via GitHub Actions
- Secure API key handling through environment variables and GitHub Secrets

## Project Structure

```
saucedemo-tests/
├── .github/workflows/    # CI/CD pipeline
├── pages/                # Page Objects (login, inventory, checkout)
├── tests/                # UI tests
│   └── api/              # API tests (CRUD, negative, parametrized)
├── conftest.py           # pytest fixtures
└── requirements.txt
```

## Getting Started / Erste Schritte

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
playwright install
```

Run all tests:

```bash
pytest
```

Note: API tests require a `REQRES_API_KEY` in a local `.env` file (see reqres.in).

## Author / Autor

**Serhii Herzikorn**
Manual QA Engineer (8+ years) → Test Automation
[LinkedIn](https://www.linkedin.com/in/serhii-herzikorn)