from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


#CONVERTING QUESTION LIST TO QUESTION OBJECT
q_bank = []
for question in question_data:
    text = question["text"]
    answer = question ["answer"]
    new_question = Question(text,answer)
    q_bank.append(new_question)
quiz = QuizBrain(q_bank)

while quiz.still_has_questions():
    quiz.print_question()

print("You are completed the quiz")
score = round(quiz.score/quiz.q_number,2)*100
print(f'your score is {score} ({quiz.score}/{quiz.q_number})')