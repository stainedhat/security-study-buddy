from typing import List
from fastapi import APIRouter, HTTPException

from data.db import database, questions
from models.question_models_v1 import Question, QuestionWithoutAnswer, NewQuestion, Answer, QuestionUpdate


router = APIRouter(
    prefix="/questions",
    tags=["questions"],
    responses={
        404: {"error": "Not found"},
        422: {"error": "Invalid object schema!"},
        500: {"error": "Oops, something went wrong!"}
    },
)


@router.get("/", response_model=List[QuestionWithoutAnswer])
async def get_questions():
    query = questions.select().with_only_columns(
        [questions.c.question_id, questions.c.question, questions.c.category]
    )
    return await database.fetch_all(query)


@router.get("/{question_id}", response_model=QuestionWithoutAnswer)
async def get_question(question_id):
    query = questions.select().with_only_columns(
        [questions.c.question_id, questions.c.question, questions.c.category]
    ).where(
        questions.c.question_id == question_id
    )
    result = await database.fetch_one(query)

    if not result:
        raise HTTPException(status_code=404, detail="Question not found!")

    return result


@router.get("/{question_id}/answer", response_model=Answer)
async def get_answer(question_id):
    query = questions.select().with_only_columns(
        [questions.c.question, questions.c.answer]
    ).where(
        questions.c.question_id == question_id
    )
    result = await database.fetch_one(query)

    if not result:
        raise HTTPException(status_code=404, detail="Question not found!")

    return result


@router.delete("/{question_id}")
async def delete_question(question_id):
    query = questions.select().where(
        questions.c.question_id == question_id
    )
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
    q_query = questions.insert().values(
        question=question.question,
        answer=question.answer,
        category=question.category
    )
    q_id = await database.execute(q_query)
    return {**question.model_dump(), "question_id": q_id}


@router.put("/{question_id}", response_model=Question)
async def update_question(question_id, question: QuestionUpdate):
    u_query = questions.update().where(
        questions.c.question_id == question_id
    ).values(
        **question.model_dump(exclude_unset=True)
    )
    q_id = await database.execute(u_query)

    # Return the entire new object as it exists in the database
    result_query = questions.select().where(
        questions.c.question_id == question_id
    )
    result = await database.fetch_one(result_query)

    return result
