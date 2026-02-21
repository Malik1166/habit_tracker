from fastapi import FastAPI
from app.db.session import engine
from sqlalchemy import text


app = FastAPI()


@app.get('/test-db')
async def test_db():
    async with engine.begin() as conn:
        result = await conn.execute(
            text('SELECT 1')
        )
        value = result.scalar_one()
        return {"result": value}