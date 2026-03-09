from authx import AuthX, AuthXConfig
from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession 
from fastapi import Depends, HTTPException, status

from app.core.config import settings
from app.db.session import get_db
from app.services.auth_service import get_user_by_id


config = AuthXConfig(
    JWT_SECRET_KEY=settings.SECRET_KEY,
    JWT_ALGORITHM=settings.ALGORITHM,
    JWT_ACCESS_TOKEN_EXPIRES=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60
)


auth = AuthX(config=config)


def create_access_token(user_id: UUID):
    payload={
        "sub": str(user_id)
    }
    token = auth.create_access_token(payload)
    return token


async def get_current_user(
    db: AsyncSession = Depends(get_db),
    _=Depends(auth.access_token_required)):
    
    subject = auth.get_access_token_subject()
    user_id = UUID(subject)
    user = await get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='User not found')
    
    return user
    