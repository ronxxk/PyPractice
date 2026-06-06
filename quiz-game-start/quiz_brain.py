class QuizBrain:

    def __init__(self, q_list):
        self.ques_no = 0
        self.ques_list = q_list
        self.score = 0
    
    def still_has_ques(self):
        # return self.ques_no < len(self.ques_list)
        if self.ques_no < len(self.ques_list):
            return True
        else:
            return False

    def next_ques(self):
        item = self.ques_list[self.ques_no]
        self.ques_no +=1
        user_ans = input(f"Q{self.ques_no}: {item.text} (True/False)?: ")
        self.check_ans(user_ans, item.answer)

    def check_ans(self, user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            print("Correct!\n")
            self.score += 1
        else:
            print(f"Wrong! The answer is {correct_ans}\n")
        print(f"Your score is:{self.score}/{self.ques_no}\n")
        print("\n"*3)