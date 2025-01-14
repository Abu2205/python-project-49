from brain_games.cli import welcome_user
import prompt

ROUNDS_TO_WIN = 3

def run_game(game):
    
    name = welcome_user()
    
    
    print(game.RULE)

    for _ in range(ROUNDS_TO_WIN):
        question, correct_answer = game.generate_question_and_answer()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")

        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was "
                  f"'{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
        
        print("Correct!")

    print(f"Congratulations, {name}!")