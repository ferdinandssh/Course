class QuizBrain():
    def __init__(self,question_class):
        self.question_class = question_class
        self.q_number = 0
        self.score = 0

    def still_has_questions(self):
        while self.q_number < len(self.question_class):            
            return True
        return False        
    
    def print_question(self):
        current_question = self.question_class[self.q_number] 
        self.q_number +=1
        guess = input(f'Q{self.q_number}. {current_question.text} (True/False): ')
        self.check_answer(guess,current_question.answer)
    
    def check_answer(self,guess,answer):
        if guess.lower() == answer.lower():
            self.score += 1
            print("You are right")
        else:
            print("You are wrong")


    






