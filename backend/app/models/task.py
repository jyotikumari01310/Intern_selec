from sqlalchemy import Column, Integer, String, Text
from app.config.database import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    description = Column(Text)