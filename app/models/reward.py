import uuid

from sqlalchemy import Integer, String, Column, ForeignKey, DateTime, UniqueConstraint, func
from sqlalchemy.dialects.postgresql import UUID

from app.db.session import Base



class Reward(Base):
    __tablename__ = 'rewards'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False, index=True)
    streak_value = Column(Integer, nullable=False)
    reward_type = Column(String, nullable=False)
    unlocked_at = Column(DateTime(timezone=True), server_default=func.now())
    
    __table_args__ = (
        UniqueConstraint('user_id', 'streak_value', name='uq_user_streak_reward'),
    )