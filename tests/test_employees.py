def test_create_employee_duplicate_email(client):
    employee = {
        "name": "Duplicate Employee",
        "email": "duplicate@example.com",
        "department": "Engineering",
        "designation": "Developer",
    }

    first_response = client.post(
        "/api/employees",
        json=employee,
    )

    assert first_response.status_code == 201

    second_response = client.post(
        "/api/employees",
        json=employee,
    )

    assert second_response.status_code == 409
    assert second_response.json()["detail"] == (
        "Employee with this email already exists"
    )


def test_get_nonexistent_employee(client):
    response = client.get("/api/employees/999999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Employee not found"