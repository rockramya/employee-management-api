from fastapi import FastAPI

from app.api.employee_routes import router as employee_router


app = FastAPI(
    title="Employee Management API",
    description="REST API for managing employee records.",
    version="1.0.0",
)


app.include_router(employee_router)


@app.get("/")
def root():
    return {
        "message": "Employee Management API is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }