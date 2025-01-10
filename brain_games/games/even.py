import random

RULE = "Answer \"yes\" if the number is even, otherwise answer \"no\"."


def is_even(number):
    """Check if the number is even."""
    return number % 2 == 0


def generate_question_and_answer():
    number = random.randint(1, 100)
    correct_answer = "yes" if is_even(number) else "no"
    return str(number), correct_answer