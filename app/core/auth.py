from authx import AuthX, AuthXConfig
from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession 
from fastapi import Depends, Security, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError

from app.core.config import settings
from app.db.session import get_db
from app.services.auth_service import get_user_by_id


config = AuthXConfig(
    JWT_SECRET_KEY=settings.SECRET_KEY,
    JWT_ALGORITHM=settings.ALGORITHM,
    JWT_ACCESS_TOKEN_EXPIRES=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60
)


auth = AuthX(config=config)
security = HTTPBearer()


def create_access_token(user_id: UUID):
    token = auth.create_access_token(str(user_id))
    return token


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Security(security),
    db: AsyncSession = Depends(get_db)):
    try:
        token = credentials.credentials
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
            )
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )
    subject: str = payload.get("sub")
    user_id = UUID(subject)
    user = await get_user_by_id(db, user_id)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='User not found')
    
    return user
    