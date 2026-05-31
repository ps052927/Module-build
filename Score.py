# Package Module

def show_result(score, total):
    print("\n===== RESULT =====")

    print(f"Score: {score}/{total}")

    if score == total:
        print("Excellent!")
    elif score >= total // 2:
        print("Good Job!")
    else:
        print("Keep Practicing!")
