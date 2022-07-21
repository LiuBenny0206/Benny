from Question import Question
question_prompts = [
    "How old is Benny?\n(a) 20 \n(b) 25 \n(c) 12 \n\n",
    "How dumb you are?\n (a) Very \n (b) Not \n (c) 5\n\n",
    "What is your favorite team?\n(a) FCB \n(b) BAR \n(c) RAM\n\n"
]
questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "b"),
]
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question_prompts)
        if answer == question.answer:
            score += 1
    print("You got" + str(score)+ "/" + str(len(questions)) + "correct")

run_test(questions)