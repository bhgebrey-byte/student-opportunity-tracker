
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models
from database import engine, Base, SessionLocal
from schemas import OpportunityCreate, OpportunityResponse


# Create database tables if they do not exist
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Student Opportunity Tracker API",
    description="An API for managing student opportunities",
    version="1.0.0"
)


# Open and close database sessions
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Welcome endpoint
@app.get("/")
def home():
    return {
        "message": "Welcome to the Student Opportunity Tracker API!",
        "status": "running"
    }


# CREATE: Add a new opportunity
@app.post(
    "/opportunities",
    response_model=OpportunityResponse,
    status_code=201
)
def create_opportunity(
    opportunity: OpportunityCreate,
    db: Session = Depends(get_db)
):
    new_opportunity = models.Opportunity(
        **opportunity.model_dump()
    )

    db.add(new_opportunity)
    db.commit()
    db.refresh(new_opportunity)

    return new_opportunity


# READ: Get all opportunities
@app.get(
    "/opportunities",
    response_model=list[OpportunityResponse]
)
def get_opportunities(db: Session = Depends(get_db)):
    return db.query(models.Opportunity).all()


# READ: Get one opportunity by ID
@app.get(
    "/opportunities/{opportunity_id}",
    response_model=OpportunityResponse
)
def get_opportunity(
    opportunity_id: int,
    db: Session = Depends(get_db)
):
    opportunity = db.query(models.Opportunity).filter(
        models.Opportunity.id == opportunity_id
    ).first()

    if opportunity is None:
        raise HTTPException(
            status_code=404,
            detail="Opportunity not found"
        )

    return opportunity


# UPDATE: Update an existing opportunity
@app.put(
    "/opportunities/{opportunity_id}",
    response_model=OpportunityResponse
)
def update_opportunity(
    opportunity_id: int,
    updated_opportunity: OpportunityCreate,
    db: Session = Depends(get_db)
):
    opportunity = db.query(models.Opportunity).filter(
        models.Opportunity.id == opportunity_id
    ).first()

    if opportunity is None:
        raise HTTPException(
            status_code=404,
            detail="Opportunity not found"
        )

    for key, value in updated_opportunity.model_dump().items():
        setattr(opportunity, key, value)

    db.commit()
    db.refresh(opportunity)

    return opportunity


# DELETE: Delete an opportunity
@app.delete("/opportunities/{opportunity_id}")
def delete_opportunity(
    opportunity_id: int,
    db: Session = Depends(get_db)
):
    opportunity = db.query(models.Opportunity).filter(
        models.Opportunity.id == opportunity_id
    ).first()

    if opportunity is None:
        raise HTTPException(
            status_code=404,
            detail="Opportunity not found"
        )

    db.delete(opportunity)
    db.commit()

    return {
        "message": "Opportunity deleted successfully"
    }
