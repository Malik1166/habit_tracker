from authx import AuthX, AuthXConfig

from app.core.config import settings



config = AuthXConfig(
    JWT_SECRET_KEY=settings.SECRET_KEY,
    JWT_ALGORITHM=settings.ALGORITHM,
    JWT_ACCESS_TOKEN_EXPIRES=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60
)


auth = AuthX(config=config)


def create_access_token(user_id: int):
    payload={
        "sub": user_id
    }
    token = auth.create_access_token(payload)
    return token