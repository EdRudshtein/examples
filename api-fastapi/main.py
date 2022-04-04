from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn


class Person(BaseModel):
	name: str
	description: Optional[str] = None
	price: float
	tax: Optional[float] = None


app = FastAPI()


@app.get("/")
async def index():
	return "Hello World"


@app.get("/calc1")
async def calc1(a: int) -> Person:
	result = Person(name='edward', price=a)
	return result


@app.get("/calc2")
async def calc2(a: int) -> int:
	return a+2


if __name__ == "__main__":
	uvicorn.run("main:app", port=8080, log_level="debug", reload=True)  #host="0.0.0.0",
