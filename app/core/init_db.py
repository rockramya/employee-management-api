from app.core.database import Base, engine
from app.models.employee import Employee


def initialize_database() -> None:
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    initialize_database()
    print("Database tables created successfully.")