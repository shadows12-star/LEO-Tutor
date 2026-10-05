from crewai import Agent


def create_coordinator(llm):
    return Agent(
        role="Leo Coordinator",
        goal=(
            "Understand the student's request and coordinate the tutoring workflow."
        ),
        backstory=(
            "You manage a tutoring team. You decide which specialist should "
            "handle each part of the student's learning process."
        ),
        llm=llm,
        verbose=True,
        allow_delegation=False,
    )


def create_explainer(llm):
    return Agent(
        role="Concept Explainer",
        goal=(
            "Teach the requested topic clearly at the student's current level."
        ),
        backstory=(
            "You are a patient teacher who explains difficult ideas using "
            "simple language, examples, and step-by-step reasoning."
        ),
        llm=llm,
        verbose=True,
        allow_delegation=False,
    )


def create_quiz_master(llm):
    return Agent(
        role="Quiz Master",
        goal=(
            "Create structured practice questions based on the explanation."
        ),
        backstory=(
            "You are an assessment specialist who creates questions that test "
            "real understanding rather than memorization."
        ),
        llm=llm,
        verbose=True,
        allow_delegation=False,
    )


def create_evaluator(llm):
    return Agent(
        role="Student Answer Evaluator",
        goal=(
            "Evaluate the student's answers and provide a score and useful feedback."
        ),
        backstory=(
            "You carefully compare the student's answers with the expected concepts "
            "and explain both strengths and mistakes."
        ),
        llm=llm,
        verbose=True,
        allow_delegation=False,
    )