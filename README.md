# Employee Management REST API

A production-style Employee Management REST API built with Python and FastAPI. The project demonstrates RESTful CRUD operations, MySQL database integration, layered architecture, dependency injection, SOLID principles, validation, and automated testing.

## Features

- RESTful CRUD APIs for employee management
- FastAPI framework
- MySQL relational database
- SQLAlchemy ORM
- Pydantic request/response validation
- Repository and Service layer architecture
- Dependency Injection
- Repository abstraction for Dependency Inversion
- Duplicate email validation
- Proper HTTP status codes and error handling
- Swagger/OpenAPI documentation
- Automated tests using pytest
- Separate test database
- Environment-based database configuration

## Tech Stack

- Python 3.11+
- FastAPI
- SQLAlchemy
- MySQL
- PyMySQL
- Pydantic
- pytest
- HTTPX

## Architecture

The application follows a layered architecture:

```text
Client
   |
   v
FastAPI Routes
   |
   v
Service Layer
   |
   v
Repository Interface
   |
   v
Repository Implementation
   |
   v
SQLAlchemy ORM
   |
   v
MySQL

Project Structure
employee-management-api/
│
├── app/
│   ├── api/
│   │   ├── dependencies.py
│   │   ├── employee_routes.py
│   │   └── __init__.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   ├── database.py
│   │   ├── init_db.py
│   │   └── __init__.py
│   │
│   ├── models/
│   │   ├── employee.py
│   │   └── __init__.py
│   │
│   ├── repositories/
│   │   ├── employee_repository.py
│   │   ├── employee_repository_interface.py
│   │   └── __init__.py
│   │
│   ├── schemas/
│   │   ├── employee.py
│   │   └── __init__.py
│   │
│   ├── services/
│   │   ├── employee_service.py
│   │   └── __init__.py
│   │
│   ├── main.py
│   └── __init__.py
│
├── tests/
│   ├── conftest.py
│   ├── test_employees.py
│   └── __init__.py
│
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
API Endpoints

Base URL:

http://127.0.0.1:8000
Method	Endpoint	Description
POST	/api/employees	Create employee
GET	/api/employees	Get all employees
GET	/api/employees/{id}	Get employee by ID
PUT	/api/employees/{id}	Update employee
DELETE	/api/employees/{id}	Delete employee
GET	/health	Health check
Example Request
Create Employee
{
  "name": "Ramya Kulkarni",
  "email": "ramya@example.com",
  "department": "Engineering",
  "designation": "Software Engineer"
}
Response
{
  "name": "Ramya Kulkarni",
  "email": "ramya@example.com",
  "department": "Engineering",
  "designation": "Software Engineer",
  "id": 1
}
HTTP Status Codes
Status	Meaning
200	Successful request
201	Employee created
404	Employee not found
409	Duplicate email
422	Validation error
Setup
1. Clone the repository
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd employee-management-api
2. Create a virtual environment

Windows:

python -m venv venv
venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
4. Configure environment variables

Create a .env file based on .env.example.

DATABASE_URL=mysql+pymysql://root:password@localhost:3306/employee_db
TEST_DATABASE_URL=mysql+pymysql://root:password@localhost:3306/employee_test_db

Create the databases in MySQL:

CREATE DATABASE employee_db;
CREATE DATABASE employee_test_db;
5. Initialize the database
python -m app.core.init_db
6. Start the application
uvicorn app.main:app --reload

The API will be available at:

http://127.0.0.1:8000
API Documentation

FastAPI automatically provides interactive Swagger documentation:

http://127.0.0.1:8000/docs

Alternative ReDoc documentation:

http://127.0.0.1:8000/redoc
Running Tests

Run the complete test suite:

pytest -v

The project includes automated tests covering:

Employee creation
Get all employees
Get employee by ID
Update employee
Delete employee
Duplicate email handling
Non-existent employee handling

The tests use a separate MySQL test database so application data is isolated from test data.

SOLID Principles
Single Responsibility Principle

Different layers have separate responsibilities:

Routes handle HTTP requests and responses.
Services contain business logic.
Repositories handle database operations.
Models represent database entities.
Schemas handle request/response validation.
Dependency Inversion Principle

EmployeeService depends on the EmployeeRepositoryInterface abstraction rather than directly depending on the concrete repository implementation.

This makes the service easier to test and allows the repository implementation to be replaced without changing business logic.

Dependency Injection

FastAPI's dependency injection system provides:

Database sessions
Employee service instances

This avoids unnecessary global dependencies and improves testability.

Configuration

Database connections are configured through environment variables:

DATABASE_URL
TEST_DATABASE_URL

This allows the application to switch between different databases without changing application code.

Future Improvements

Possible extensions include:

Authentication and authorization
Pagination and filtering
Search employees by department
Docker support
CI/CD with GitHub Actions
Database migrations with Alembic
Structured application logging
API versioning
Author

Ramya Kulkarni