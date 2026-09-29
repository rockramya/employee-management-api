from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.api.dependencies import get_employee_service
from app.core.database import get_db
from app.schemas.employee import (
    EmployeeCreate,
    EmployeeResponse,
    EmployeeUpdate,
)
from app.services.employee_service import EmployeeService


router = APIRouter(
    prefix="/api/employees",
    tags=["Employees"],
)


@router.post(
    "",
    response_model=EmployeeResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_employee(
    employee_data: EmployeeCreate,
    db: Session = Depends(get_db),
    employee_service: EmployeeService = Depends(get_employee_service),
):
    return employee_service.create_employee(
        db,
        employee_data,
    )


@router.get(
    "",
    response_model=list[EmployeeResponse],
)
def get_employees(
    db: Session = Depends(get_db),
    employee_service: EmployeeService = Depends(get_employee_service),
):
    return employee_service.get_all_employees(db)


@router.get(
    "/{employee_id}",
    response_model=EmployeeResponse,
)
def get_employee(
    employee_id: int,
    db: Session = Depends(get_db),
    employee_service: EmployeeService = Depends(get_employee_service),
):
    return employee_service.get_employee(
        db,
        employee_id,
    )


@router.put(
    "/{employee_id}",
    response_model=EmployeeResponse,
)
def update_employee(
    employee_id: int,
    employee_data: EmployeeUpdate,
    db: Session = Depends(get_db),
    employee_service: EmployeeService = Depends(get_employee_service),
):
    return employee_service.update_employee(
        db,
        employee_id,
        employee_data,
    )


@router.delete(
    "/{employee_id}",
    status_code=status.HTTP_200_OK,
)
def delete_employee(
    employee_id: int,
    db: Session = Depends(get_db),
    employee_service: EmployeeService = Depends(get_employee_service),
):
    return employee_service.delete_employee(
        db,
        employee_id,
    )