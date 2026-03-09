from fastapi import FastAPI
from sqlalchemy import text

from app.db.session import engine
from app.routers.auth_router import router as auth_router



app = FastAPI()

app.include_router(auth_router)


@app.get('/test-db')
async def test_db():
    async with engine.begin() as conn:
        result = await conn.execute(
            text('SELECT 1')
        )
        value = result.scalar_one()
        return {"result": value}