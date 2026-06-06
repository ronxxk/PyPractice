from question_model import Question
from data import question_data, question_data_2nd
from quiz_brain import QuizBrain

question_bank = []
question__data = ""

input("Choose your theme:\n")
if input == "fun facts":
    question__data = question_data
else:
    question__data = question_data_2nd

for i in question__data:
    ques = i["text"]
    ans = i["answer"]
    question_bank.append(Question(ques, ans))

# for q_obj in question_bank:
#     q_obj_txt = q_obj.text
#     q_obj_ans = q_obj.answer
#     print(f"Q: {q_obj_txt}\nA: {q_obj_ans}")

quiz = QuizBrain(question_bank)

while quiz.still_has_ques():
    quiz.next_ques()

print(f"Your final score is {quiz.score}/{quiz.ques_no}!")