import random

RULE = "What is the result of the expression?"


def generate_question_and_answer():
    operators = ['+', '-', '*']
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    operator = random.choice(operators)
    
    question = f"{num1} {operator} {num2}"
    if operator == '+':
        correct_answer = str(num1 + num2)
    elif operator == '-':
        correct_answer = str(num1 - num2)
    elif operator == '*':
        correct_answer = str(num1 * num2)
    
    return question, correct_answer