from crewai import Task

from src.models import QuizOutput


def create_coordinator_task(coordinator, topic, level):
    return Task(
        description=f"""
        A student wants to learn the following topic:

        Topic: {topic}
        Student level: {level}

        Analyze the student's request.

        Create a short learning plan for the Explainer.

        Your plan should mention:
        - what concepts should be taught
        - how difficult the explanation should be
        - what examples may help
        - what the student should understand by the end
        """,
        expected_output=(
            "A short learning plan that another tutor can follow."
        ),
        agent=coordinator,
    )


def create_explanation_task(explainer, coordinator_task, topic, level):
    return Task(
        description=f"""
        Teach the student about:

        Topic: {topic}
        Level: {level}

        Use the Coordinator's learning plan as guidance.

        Explain the topic clearly using:
        - simple language
        - step-by-step explanation
        - at least one useful example

        Avoid unnecessary technical jargon.
        """,
        expected_output=(
            "A clear lesson that teaches the student the requested topic."
        ),
        agent=explainer,

        # REAL HANDOFF
        context=[coordinator_task],
    )


def create_quiz_task(quiz_master, explanation_task, topic):
    return Task(
        description=f"""
        Create a quiz about:

        {topic}

        Use the Explainer's lesson as your source.

        Create exactly 5 questions.

        Return ONLY valid JSON using this exact structure:

        {{
            "topic": "{topic}",
            "questions": [
                {{
                    "question_number": 1,
                    "question": "question here",
                    "expected_answer": "expected answer here"
                }}
            ]
        }}

        Requirements:
        - exactly 5 questions
        - question_number must be an integer
        - every question must have an expected_answer
        - do not include markdown
        - do not include ```json
        - do not write anything before or after the JSON
        """,
        expected_output="Valid JSON containing the topic and exactly 5 quiz questions.",
        agent=quiz_master,
        context=[explanation_task],
    )
 