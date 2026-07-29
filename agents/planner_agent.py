def planner_agent(user_input):

    user_input = user_input.lower()

    if "quiz" in user_input or "question" in user_input:
        return "quiz"

    elif "summary" in user_input or "summarize" in user_input:
        return "summary"

    else:
        return "explanation"