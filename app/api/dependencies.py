from app.repositories.employee_repository import EmployeeRepository
from app.services.employee_service import EmployeeService


def get_employee_service() -> EmployeeService:
    repository = EmployeeRepository()
    return EmployeeService(repository)