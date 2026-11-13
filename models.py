
from sqlalchemy import Column, Integer, String, Date, Text
from database import Base


class Opportunity(Base):
    __tablename__ = "opportunities"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    category = Column(String, nullable=False)
    organization = Column(String, nullable=False)
    deadline = Column(Date, nullable=False)
    status = Column(String, default="Interested")
    description = Column(Text, nullable=True)
