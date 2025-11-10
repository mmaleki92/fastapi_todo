from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TodoCreate(BaseModel):
    """Schema for creating a todo"""
    title: str
    description: Optional[str] = None

class TodoUpdate(BaseModel):
    """Schema for updating a todo"""
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

class TodoResponse(BaseModel):
    """Schema for todo response"""
    id: int
    title: str
    description: Optional[str] = None
    completed: bool
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True