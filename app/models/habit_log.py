import uuid

from sqlalchemy import (Integer, Boolean,Column, ForeignKey,
                        Date, DateTime,UniqueConstraint,
                        Index, func)

from sqlalchemy.dialects.postgresql import UUID

from app.db.session import Base



class HabitLog(Base):
    __tablename__ = 'habit_logs'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    habit_id = Column(UUID(as_uuid=True), ForeignKey('habits.id'), nullable=False, index=True)
    date = Column(Date, nullable=False)
    completed = Column(Boolean, nullable=True)
    value = Column(Integer, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    __table_args__ = (
        UniqueConstraint('habit_id', 'date', name='uq_habit_date'),
        Index('ix_habit_date', 'habit_id', 'date'),
    )
    