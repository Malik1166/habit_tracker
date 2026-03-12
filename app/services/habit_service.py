from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID

from app.schemas.habit import HabitCreate
from app.models.habit import Habit



async def create_habit(db: AsyncSession, data: HabitCreate, user_id: UUID):
    habit_data = data.model_dump()
    habit = Habit(**habit_data, user_id=user_id)
    db.add(habit)
    await db.commit()
    await db.refresh(habit)
    return habit