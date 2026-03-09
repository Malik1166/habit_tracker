from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from uuid import UUID

from app.models.user import User
from app.core.security import hash_password
from app.schemas.auth import UserRegister
from app.core.security import verify_password

async def create_user(db: AsyncSession, user_data: UserRegister):
    hashed_password = hash_password(user_data.password)
    user = User(
        email=user_data.email,
        hashed_password=hashed_password
    )
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user


async def get_user_by_email(db: AsyncSession, email: str):
    query = select(User).where(User.email == email)
    result = await db.execute(query)
    user = result.scalar_one_or_none()
    return user 

    
async def authenticate_user(db: AsyncSession, email: str, password: str):
    user = await get_user_by_email(db=db, email=email)
    if not user: 
        return None
    
    valid_password = verify_password(password, user.hashed_password)
    
    if not valid_password:
        return None
    
    return user


async def get_user_by_id(db: AsyncSession, user_id: UUID):
    query = select(User).where(User.id == user_id)
    result = await db.execute(query)
    user = result.scalar_one_or_none()
    return user