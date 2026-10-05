from crewai import Crew, Process

from src.llm import get_llm

from src.agents import (
    create_coordinator,
    create_explainer,
    create_quiz_master,
)

from src.tasks import (
    create_coordinator_task,
    create_explanation_task,
    create_quiz_task,
)


# -------------------------
# Student input
# -------------------------

topic = "Photosynthesis"
level = "Beginner"


# -------------------------
# Load LLM
# -------------------------

llm = get_llm()


# -------------------------
# Create agents
# -------------------------

coordinator = create_coordinator(llm)

explainer = create_explainer(llm)

quiz_master = create_quiz_master(llm)


# -------------------------
# Create tasks
# -------------------------

coordinator_task = create_coordinator_task(
    coordinator,
    topic,
    level,
)


explanation_task = create_explanation_task(
    explainer,
    coordinator_task,
    topic,
    level,
)


quiz_task = create_quiz_task(
    quiz_master,
    explanation_task,
    topic,
)


# -------------------------
# Create Crew
# -------------------------

crew = Crew(
    agents=[
        coordinator,
        explainer,
        quiz_master,
    ],

    tasks=[
        coordinator_task,
        explanation_task,
        quiz_task,
    ],

    process=Process.sequential,

    verbose=True,
)


# -------------------------
# Run
# -------------------------

result = crew.kickoff()


import json

from src.models import QuizOutput


quiz_raw = result.tasks_output[-1].raw

quiz_data = json.loads(quiz_raw)

quiz = QuizOutput.model_validate(quiz_data)

print("\nTOPIC:")
print(quiz.topic)

print("\nQUESTIONS:")

for question in quiz.questions:
    print(f"{question.question_number}. {question.question}")
    print(f"Expected answer: {question.expected_answer}")
    print()