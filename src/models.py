from pydantic import BaseModel
from typing import List


class QuizQuestion(BaseModel):
    question_number: int
    question: str
    expected_answer: str


class QuizOutput(BaseModel):
    topic: str
    questions: List[QuizQuestion]