
questions = {
    "What is the capital of France? ": "paris",
    "Which language is used for AI most often? ": "python",
    "How many continents are there? ": "7"
}

def run_quiz():
    score = 0

    for question, answer in questions.items():
        user_answer = input(question).lower()

        if user_answer == answer:
            print("Correct!\n")
            score += 1
        else:
            print("Wrong!\n")

    return score
