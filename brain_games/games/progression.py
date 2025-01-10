import random

RULE = "What number is missing in the progression?"


def generate_question_and_answer():
    length = random.randint(5, 10)
    start = random.randint(1, 50)
    step = random.randint(1, 10)

    progression = [start + step * i for i in range(length)]

    missing_index = random.randint(0, length - 1)
    correct_answer = str(progression[missing_index])

    progression[missing_index] = ".."
    question = " ".join(map(str, progression))

    return question, correct_answer