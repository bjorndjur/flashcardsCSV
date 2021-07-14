# Load from questions from file
import pandas as pd
import random

class Question:
    def __init__(self, subject, question, answer):
        self.subject = subject
        self.question = question
        self.answer = answer



def loadQuestions(file):
    questions = []
    data = pd.read_csv(file)

    for i in range(len(data)):
        subject = data['subject'][i]
        question = data['question'][i]
        answer = data['answer'][i]

        questions.append(Question(subject, question, answer))

    return questions

# Get next question 
def getNextQuestion(questions, questionCounter):
    currentQuestion = questions[questionCounter]
    questionCounter += 1
    return currentQuestion

# Get four respons options
def getResponsOptions(questions, questionCounter):
    responsOptions = []
    responsOptions.append(questions[questionCounter])
    questions.pop(questionCounter)
    randomSample = random.sample(range(0, len(questions)), 3)

    for i in range(len(randomSample)):
        responsOptions.append(questions[randomSample[i]])

    return(responsOptions)


def trySelectedAnswer(currentQuestion,responsOptions):
    if (currentQuestion.answer == responsOptions.answer):
        return True
    else:
        return False



questionCounter = 0

# Read questions and answers 
questions = loadQuestions('subjects/first.csv')

# Get current question
currentQuestion = getNextQuestion(questions, questionCounter)
print(currentQuestion.question)
print(currentQuestion.answer)

# Get respons options
responsOptions = getResponsOptions(questions,questionCounter)
random.shuffle(responsOptions)
for i in range(len(responsOptions)):
    print('{i}: {responsOption}'.format(i=i+1, responsOption=responsOptions[i].answer))


# Selected answer
selectedAnswer = input('>')

isCorrect = trySelectedAnswer(currentQuestion,responsOptions[int(selectedAnswer) - 1])

print(isCorrect)