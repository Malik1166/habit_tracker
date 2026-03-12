from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.habit import HabitCreate, HabitResponse
from app.core.auth import get_current_user
from app.services.habit_service import create_habit
from app.db.session import get_db
from app.models.user import User

router = APIRouter()


@router.post("/habits", response_model=HabitResponse)
async def post_habit(data: HabitCreate,
                    db: AsyncSession = Depends(get_db),
                    current_user: User = Depends(get_current_user)):
    habit = await create_habit(db, data, current_user.id)
    return habit
