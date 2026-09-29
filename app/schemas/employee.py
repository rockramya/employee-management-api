from pydantic import BaseModel, ConfigDict, EmailStr


class EmployeeBase(BaseModel):
    name: str
    email: EmailStr
    department: str
    designation: str


class EmployeeCreate(EmployeeBase):
    pass


class EmployeeUpdate(EmployeeBase):
    pass


class EmployeeResponse(EmployeeBase):
    id: int

    model_config = ConfigDict(from_attributes=True)