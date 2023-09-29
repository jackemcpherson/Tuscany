# Tuscany

A personal finance application built with FastAPI, using a microservices architecture.

## Purpose

This project aims to create a microservices architecture for tracking expenses and deposits across multiple bank accounts. It currently supports basic CRUD operations for users and accounts.

## Directory Structure

```
Tuscany/
├── user_service/
├── account_service/
└── transaction_service/  # Coming soon
```

## Setup

1. Install the dependencies:

```bash
poetry install
```

2. Each microservice has its own FastAPI application and can be run individually. For example, to run the User Service:

```bash
uvicorn user_service.main:app --reload
```

To run the Account Service:

```bash
uvicorn account_service.main:app --reload
```

## Testing

Unit tests are available for each service under their respective \`tests\` directories. Run tests using \`pytest\`:

```bash
pytest tests/
```

## Recent Changes

- Added User Service for user CRUD operations.
- Added Account Service for account CRUD operations.

## Roadmap

- Implement Transaction Service for tracking transactions.
- Add authentication and authorization features.
