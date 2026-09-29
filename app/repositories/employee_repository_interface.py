from abc import ABC, abstractmethod

from sqlalchemy.orm import Session

from app.models.employee import Employee
from app.schemas.employee import EmployeeCreate, EmployeeUpdate


class EmployeeRepositoryInterface(ABC):

    @abstractmethod
    def create(
        self,
        db: Session,
        employee_data: EmployeeCreate,
    ) -> Employee:
        pass

    @abstractmethod
    def get_all(
        self,
        db: Session,
    ) -> list[Employee]:
        pass

    @abstractmethod
    def get_by_id(
        self,
        db: Session,
        employee_id: int,
    ) -> Employee | None:
        pass

    @abstractmethod
    def get_by_email(
        self,
        db: Session,
        email: str,
    ) -> Employee | None:
        pass

    @abstractmethod
    def update(
        self,
        db: Session,
        employee: Employee,
        employee_data: EmployeeUpdate,
    ) -> Employee:
        pass

    @abstractmethod
    def delete(
        self,
        db: Session,
        employee: Employee,
    ) -> None:
        pass