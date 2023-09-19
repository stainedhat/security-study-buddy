from typing import Optional
from pydantic import BaseModel


class Question(BaseModel):
    question_id: int
    question: str
    answer: str
    category: str


class QuestionWithoutAnswer(BaseModel):
    question_id: int
    question: str
    category: str


class NewQuestion(BaseModel):
    question: str
    answer: str
    category: str


class Answer(BaseModel):
    question: str
    answer: str


# This model can be used to update any editable field in a question
class QuestionUpdate(BaseModel):
    question: Optional[str] = None
    answer: Optional[str] = None
    category: Optional[str] = None
