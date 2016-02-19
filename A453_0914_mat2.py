##a453 programming project 2, released sept 14 for jun 16
##A primary school teacher wants a computer program to test the basic arithmetic skills of her students.
##The program should generate a quiz consisting of a series of random questions, using in each case
##any two numbers and addition, subtraction and multiplication. The system should ask the student’s
##name, then ask 10 questions, output if the answer to each question is correct or not and produce a final
##score out of 10.
##Analyse the requirements in detail and design, code, test and evaluate a program to meet these
##requirements.

from random import randint
import operator

def studentName():
    userName = 0
    userClass = 0
    userConfirm = 0
    while userConfirm != "Y":
        userName = input("What is your Name?")
        userClass = input("Which Class are you in (A,B or C?)")
        userConfirm = input("your name and class is "+ userName + userClass +", correct, Y/N?")
    questions()


def questions():
    score = 0
    opList = ["*", "-", "+"]
    opDict = { "+": operator.add, "-": operator.sub, "*": operator.mul }
    
    #print (c)
    for x in range (0,9):
        a = (randint(0,9))
        b = (randint(0,9))
        c = opList[(randint(0,2))]
        qAnswer = int(input("Here is a question - what is?:" + str(a) + str(c) + str(b)))
        if qAnswer == opDict[c](a,b):
            print ("the answer is: " + str(opDict[c](a,b)) +", Well Done")
            score = score+1
            print ("your score is: " + str(score))
        else:
            print ("Sorry, that's wrong, the answer is ")
            print (opDict[c](a,b))
            print ("your score is: " + str(score))

