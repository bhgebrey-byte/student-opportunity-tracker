
from datetime import date
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


# Information required when creating an opportunity
class OpportunityCreate(BaseModel):
    title: str = Field(min_length=3)
    category: Literal["Scholarship", "Internship", "Job", "Training"]
    organization: str
    deadline: date
    status: Literal["Interested", "Applied", "Accepted", "Rejected"] = "Interested"
    description: str | None = None


# Information returned by our API
class OpportunityResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    category: str
    organization: str
    deadline: date
    status: str
    description: str | None
