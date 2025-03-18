from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data: # creates a list of Question objects
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions(): # loops through the questions
    quiz.next_question()
else:
    quiz.quiz_end()