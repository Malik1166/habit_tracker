from typing import Optional

from pydantic import BaseModel
from datetime import date, time, datetime
from uuid import UUID

from app.models.habit import FrequencyEnum, HabitTypeEnum



class HabitCreate(BaseModel):
    title: str
    description: Optional[str]
    start_date: date
    end_date: Optional[date]
    frequency: FrequencyEnum
    habit_type: HabitTypeEnum
    target_value: Optional[int]
    reminder_time: Optional[time]
    
    
class HabitUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    start_date: Optional[date]
    end_date: Optional[date]
    frequency: Optional[FrequencyEnum]
    habit_type: Optional[HabitTypeEnum]
    target_value: Optional[int]
    reminder_time: Optional[time]
    
    
class HabitResponse(BaseModel):
    id: UUID
    title: str
    description: Optional[str]
    start_date: date
    end_date: Optional[date]
    frequency: FrequencyEnum
    habit_type: HabitTypeEnum
    target_value: Optional[int]
    reminder_time: Optional[time]
    created_at: datetime
    model_config = {"from_attributes": True}