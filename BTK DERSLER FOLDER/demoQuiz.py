#QUESTIONS

class Question:
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer
    
    def checkAnswer(self,answer):
        return self.answer== answer   
    


#QUIZ
class Quiz:
    def __init__(self,cabbar):
       self.cabbar = cabbar
       self.score = 0
       self.questionindex = 0

    def getQuestion(self):
        return self.cabbar[self.questionindex]   

q1 = Question("en iyi programlama dili hangisidir ?",['C#','Python','Java', 'C++'],'Python')
q2 = Question("en popüler programlama dili hangisidir ?",['C#','Python','Java', 'C++'],'Python')
q3 = Question("en çok kazandiran programlama dili hangisidir ?",['C#','Python','Java', 'C++'],'Python')
cabbar = [q1,q2,q3]

# print(q1.checkAnswer('Python'))
# print(q2.checkAnswer('C++'))

quiz = Quiz(cabbar)
question = quiz.getQuestion
print(question.text)   