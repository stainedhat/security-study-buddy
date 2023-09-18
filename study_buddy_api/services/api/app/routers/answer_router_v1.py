from typing import List
from fastapi import APIRouter, HTTPException

from models.answer_model_v1 import Answer
from data.db import database, answers, questions


router = APIRouter(
    prefix="/answers",
    tags=["answers"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[Answer])
async def get_answers():
    query = answers.select()
    return await database.fetch_all(query)


@router.get("/{question_id}", response_model=Answer)
async def get_answer(question_id):
    query = answers.select().where(answers.c.question_id == question_id)
    result = await database.fetch_one(query)
    if not result:
        raise HTTPException(status_code=404, detail="Answer to question not found!")
    return result

