# Student Opportunity Tracker API

A RESTful API built with Python, FastAPI, and SQLite to help students manage opportunities such as scholarships, internships, jobs, and training programs.

## Project Overview

Finding and managing opportunities can be challenging for students. This project provides a simple backend system where opportunity information can be stored, retrieved, updated, and deleted.

I developed this project to strengthen my backend development skills and apply Python programming to a practical problem related to student opportunities.

## Technologies Used

- **Python** – Backend programming language
- **FastAPI** – Web framework for building APIs
- **SQLite** – Database for storing opportunity records
- **SQLAlchemy** – Object-relational mapping (ORM)
- **Pydantic** – Data validation and schemas
- **Pytest** – Automated testing

## Features

- Create new opportunities
- Retrieve all opportunities
- Retrieve a specific opportunity by ID
- Update existing opportunities
- Delete opportunities
- Validate submitted information
- Handle errors such as missing opportunities and invalid data
- Automated tests for API endpoints

## Opportunity Information

Each opportunity includes:

- ID
- Title
- Category (Scholarship, Internship, Job, or Training)
- Organization
- Deadline
- Status (Interested, Applied, Accepted, or Rejected)
- Description

## Project Structure

```text
student-opportunity-tracker/
│
├── tests/
│   └── test_opportunities.py
│
├── .gitignore
├── main.py
├── database.py
├── models.py
├── schemas.py
├── requirements.txt
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/bhgebrey-byte/student-opportunity-tracker.git
cd student-opportunity-tracker
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

### 3. Activate the environment

For macOS and Linux:

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Run the API

```bash
./.venv/bin/fastapi dev main.py
```

The API will be available at:

`http://127.0.0.1:8000`

Interactive API documentation:

`http://127.0.0.1:8000/docs`

## Running Automated Tests

Run the following command:

```bash
python -m pytest -v
```

The project includes automated tests covering CRUD operations, successful responses, missing opportunities, and invalid input.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Welcome message |
| POST | `/opportunities` | Create an opportunity |
| GET | `/opportunities` | Retrieve all opportunities |
| GET | `/opportunities/{id}` | Retrieve one opportunity |
| PUT | `/opportunities/{id}` | Update an opportunity |
| DELETE | `/opportunities/{id}` | Delete an opportunity |

## Learning Goals

This project is part of my journey into backend development. Through building it, I am practicing:

- REST API development
- Python programming
- Database design and integration
- Data validation
- Automated testing
- Git and GitHub version control

## Future Improvements

- Add user registration and authentication
- Add search and filtering by category
- Add pagination
- Introduce user-specific opportunity tracking
- Deploy the API online

---

**Author:** Beza Gebreyes  
**GitHub:** [bhgebrey-byte](https://github.com/bhgebrey-byte)