from agents.planner_agent import planner_agent
from agents.study_agent import study_agent
from agents.quiz_agent import quiz_agent


question = input("Enter your request: ")

task = planner_agent(question)

print("Planner decided:", task)


if task == "quiz":
    response = quiz_agent(question)

else:
    response = study_agent(question)


print("\nAgent Response:")
print(response)