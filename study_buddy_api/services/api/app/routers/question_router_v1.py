from typing import List
from fastapi import APIRouter, HTTPException

from models.question_model_v1 import Question, NewQuestion
from data.db import database, questions, answers


router = APIRouter(
    prefix="/questions",
    tags=["questions"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[Question])
async def get_questions():
    query = questions.select()
    return await database.fetch_all(query)


@router.get("/{question_id}", response_model=Question)
async def get_question(question_id):
    query = questions.select().where(questions.c.question_id == question_id)
    result = await database.fetch_one(query)
    if not result:
        raise HTTPException(status_code=404, detail="Question not found!")
    return result


@router.delete("/{question_id}")
async def delete_question(question_id):
    query = questions.select().where(questions.c.question_id == question_id)
    result = await database.fetch_one(query)
    if not result:
        raise HTTPException(status_code=404, detail="Question not found!")
    del_query = questions.delete().where(questions.c.question_id == question_id)
    del_result = await database.execute(del_query)
    if not del_result:
        raise HTTPException(status_code=404, detail="Unable to delete question!")
    return {"Success": "Question deleted!"}


@router.post("/", response_model=Question)
async def create_question(question: NewQuestion):
    q_query = questions.insert().values(question=question.question, category=question.category)
    q_id = await database.execute(q_query)
    a_query = answers.insert().values(question_id=q_id, answer=question.answer)
    a_id = await database.execute(a_query)
    return {**question.model_dump(), "question_id": q_id, "answer_id": a_id}
