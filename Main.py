import random
from quiz_module import run_quiz
from score import show_result

print("=" * 30)
print(" FUN QUIZ APP ")
print("=" * 30)
messages = [
    "Ready to test your brain?",
    "Let's see how smart you are!",
    "Challenge Accepted!"
]

print(random.choice(messages))
print()

score = run_quiz()

show_result(score, 3)
