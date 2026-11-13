from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from main import app, get_db
from database import Base

# Create a separate temporary database for testing
SQLALCHEMY_DATABASE_URL = "sqlite://"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool
)

TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base.metadata.create_all(bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def setup_function():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["status"] == "running"
    
def test_create_opportunity():
    opportunity_data = {
        "title": "Mastercard Foundation Scholarship",
        "category": "Scholarship",
        "organization": "Example University",
        "deadline": "2027-02-15",
        "status": "Interested",
        "description": "Graduate scholarship opportunity."
    }

    response = client.post("/opportunities", json=opportunity_data)

    assert response.status_code == 201
    assert response.json()["title"] == "Mastercard Foundation Scholarship"
    assert response.json()["id"] == 1
    
def test_get_opportunities():
    opportunity_data = {
        "title": "Junior Data Analyst Internship",
        "category": "Internship",
        "organization": "Example Technology Company",
        "deadline": "2027-03-15",
        "status": "Interested",
        "description": "Entry-level data analysis internship."
    }

    client.post("/opportunities", json=opportunity_data)

    response = client.get("/opportunities")

    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["title"] == "Junior Data Analyst Internship"
    
def test_get_single_opportunity():
    opportunity_data = {
        "title": "Python Developer Internship",
        "category": "Internship",
        "organization": "ABC Technology",
        "deadline": "2027-04-15",
        "status": "Interested",
        "description": "Python development internship."
    }

    create_response = client.post(
        "/opportunities",
        json=opportunity_data
    )

    opportunity_id = create_response.json()["id"]

    response = client.get(f"/opportunities/{opportunity_id}")

    assert response.status_code == 200
    assert response.json()["id"] == opportunity_id
    assert response.json()["title"] == "Python Developer Internship"
    
def test_update_opportunity():
    opportunity_data = {
        "title": "Python Developer Internship",
        "category": "Internship",
        "organization": "ABC Technology",
        "deadline": "2027-04-15",
        "status": "Interested",
        "description": "Python development internship."
    }

    create_response = client.post(
        "/opportunities",
        json=opportunity_data
    )

    opportunity_id = create_response.json()["id"]

    updated_data = {
        "title": "Advanced Python Developer Internship",
        "category": "Internship",
        "organization": "ABC Technology",
        "deadline": "2027-05-15",
        "status": "Applied",
        "description": "Updated internship opportunity."
    }

    response = client.put(
        f"/opportunities/{opportunity_id}",
        json=updated_data
    )

    assert response.status_code == 200
    assert response.json()["title"] == "Advanced Python Developer Internship"
    assert response.json()["status"] == "Applied"
    
def test_delete_opportunity():
    opportunity_data = {
        "title": "Data Science Internship",
        "category": "Internship",
        "organization": "ABC Technology",
        "deadline": "2027-06-15",
        "status": "Interested",
        "description": "Data science internship."
    }

    create_response = client.post(
        "/opportunities",
        json=opportunity_data
    )

    opportunity_id = create_response.json()["id"]

    response = client.delete(
        f"/opportunities/{opportunity_id}"
    )

    assert response.status_code == 200
    assert response.json()["message"] == "Opportunity deleted successfully"

    get_response = client.get(
        f"/opportunities/{opportunity_id}"
    )

    assert get_response.status_code == 404
    
def test_get_nonexistent_opportunity():
    response = client.get("/opportunities/999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Opportunity not found"
    
def test_create_opportunity_with_invalid_data():
    opportunity_data = {
        "title": "AI",
        "category": "Scholarship",
        "organization": "Example University",
        "deadline": "2027-02-15",
        "status": "Interested"
    }

    response = client.post(
        "/opportunities",
        json=opportunity_data
    )

    assert response.status_code == 422