
from Question import Question

question_prompts = [
    "How is your day?\n(a) Good\n(b)Apple\n(c)Ten\n\n",
    "How is your ankle?\n(a) Terrible\n(b) Fuck\n(c) Nahhh\n\n",
    "How is your code?\n(a) IDK\n(b) Pie\n(c) One\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "a")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(questions)
        if answer == Question.answer:
            score += 1
    print("You got" + str(score) + "/" + str(len(questions) + "correct"))
run_test(questions)

