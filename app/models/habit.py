import uuid
import enum

from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, Date, Time, Enum, func
from sqlalchemy.dialects.postgresql import UUID

from app.db.session import Base



class FrequencyEnum(str, enum.Enum):
    DAILY = 'daily'
    WEEKLY = 'weekly'
    MONTHLY = 'monthly'
    
    
class HabitTypeEnum(str, enum.Enum):
    BOOLEAN = 'boolean'
    NUMERIC = 'numeric'


class Habit(Base):
    __tablename__ = 'habits'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=True)
    frequency = Column(Enum(FrequencyEnum, name='frequency_enum'), nullable=False)
    habit_type = Column(Enum(HabitTypeEnum, name='habit_type_enum'), nullable=False)
    target_value = Column(Integer, nullable=True)
    reminder_time = Column(Time, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    