from pydantic import BaseModel


class Question(BaseModel):
    question_id: int
    question: str
    category: str


class NewQuestion(BaseModel):
    question: str
    answer: str
    answer_id: str = None
    category: str
