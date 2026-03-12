from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.schemas.auth import UserRegister, UserResponse, UserLogin
from app.services.auth_service import create_user, authenticate_user
from app.core.auth import create_access_token



router = APIRouter()


@router.post('/register', response_model=UserResponse)
async def register(user_data: UserRegister, db: AsyncSession = Depends(get_db)):
    user = await create_user(db=db, user_data=user_data)
    return user
    
    
@router.post('/login')
async def login(user_data: UserLogin, db: AsyncSession = Depends(get_db)):
    user = await authenticate_user(db, user_data.email, user_data.password)
    
    if not user:
       raise HTTPException(
           detail='Invalid email or password',
           status_code=status.HTTP_401_UNAUTHORIZED)
       
    token = create_access_token(user.id)
    
    return {
        "access_token": token,
        "token_type": "bearer"
    }
