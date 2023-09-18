from pydantic import BaseModel


class Answer(BaseModel):
    answer_id: int
    question_id: int
    answer: str
