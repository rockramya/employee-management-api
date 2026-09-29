from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.employee_repository_interface import (
    EmployeeRepositoryInterface,
)
from app.schemas.employee import EmployeeCreate, EmployeeUpdate


class EmployeeService:

    def __init__(self, repository: EmployeeRepositoryInterface):
        self.repository = repository

    def create_employee(
        self,
        db: Session,
        employee_data: EmployeeCreate
    ):
        existing_employee = self.repository.get_by_email(
            db,
            employee_data.email
        )

        if existing_employee:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Employee with this email already exists"
            )

        return self.repository.create(
            db,
            employee_data
        )

    def get_all_employees(self, db: Session):
        return self.repository.get_all(db)

    def get_employee(
        self,
        db: Session,
        employee_id: int
    ):
        employee = self.repository.get_by_id(
            db,
            employee_id
        )

        if not employee:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Employee not found"
            )

        return employee

    def update_employee(
        self,
        db: Session,
        employee_id: int,
        employee_data: EmployeeUpdate
    ):
        employee = self.get_employee(
            db,
            employee_id
        )

        return self.repository.update(
            db,
            employee,
            employee_data
        )

    def delete_employee(
        self,
        db: Session,
        employee_id: int
    ):
        employee = self.get_employee(
            db,
            employee_id
        )

        self.repository.delete(
            db,
            employee
        )

        return {
            "message": "Employee deleted successfully"
        }