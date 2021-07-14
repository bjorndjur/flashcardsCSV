# Load from questions from file
import pandas as pd
import random

class Question:
    def __init__(self, subject, question, answer):
        self.subject = subject
        self.question = question
        self.answer = answer


class Answers:
    def __init__(self, question, correct, selected, isCorrect):
        self.question = question
        self.correct = correct
        self.selected = selected
        self.isCorrect = isCorrect



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
    randomSample = []
    responsOptions.append(questions[questionCounter])
    #questions.pop(questionCounter)
    randomSample = random.sample(range(0, len(questions)), 3)

    for i in range(len(randomSample)):
        responsOptions.append(questions[randomSample[i]])

    return(responsOptions)


def trySelectedAnswer(currentQuestion,responsOptions):


    if (currentQuestion.answer == responsOptions.answer):
        return Answers(currentQuestion.question, currentQuestion.answer, responsOptions.answer, True)
    else:
        return Answers(currentQuestion.question, currentQuestion.answer, responsOptions.answer, False)



def result(answers):
    counterCorrect = 0
    for i in range(len(answers)):
        print(answers[i].question)
        if (answers[i].isCorrect == True):
            counterCorrect += 1
            print('Your answer: {correct}\n'.format(correct=answers[i].correct))
        else:
            print('Your answer: {selected}'.format(selected = answers[i].selected))
            print('Correct anser: [{correct}]\n'.format(correct=answers[i].correct))

    print('{numberOfCorrect}/{numberOfQuestions}'.format(numberOfCorrect=counterCorrect, numberOfQuestions=len(answers)))




questionCounter = 0
answers = []


# Read questions and answers 
questions = loadQuestions('subjects/first.csv')


while (questionCounter < len(questions)):
    # Get current question
    currentQuestion = getNextQuestion(questions, questionCounter)
    print(questionCounter + 1, currentQuestion.question)
    # print(currentQuestion.answer)

    # Get respons options
    responsOptions = getResponsOptions(questions,questionCounter)
    random.shuffle(responsOptions)
    for i in range(len(responsOptions)):
        print('{i}: {responsOption}'.format(i=i+1, responsOption=responsOptions[i].answer))

    # Selected answer
    selectedAnswer = input('>')

    answer = trySelectedAnswer(currentQuestion,responsOptions[int(selectedAnswer) - 1])
    answers.append(answer)
    #print(answer.isCorrect)
    questionCounter += 1


result(answers)