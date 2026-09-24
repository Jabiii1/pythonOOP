import random
import time
import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


# -------------------------
# QUIZ QUESTIONS
# -------------------------

# MULTIPLE CHOICEEEEEEEEE

def multiple_choice():
    print("\n=== MULTIPLE CHOICE ===")
    print("What does CPU stand for?")
    print("A. Central Processing Unit")
    print("B. Computer Personal Unit")
    print("C. Central Program Utility")
    print("D. Computer Processing Utility")

    answer = input("\nAnswer: ").strip().upper()

    if answer == "A":
        print("\n✓ YOU ARE CORRECT!")
        return True

    elif answer in ["B", "C", "D"]:
        print("\n✗ YOU ARE WRONG!")
        print("Correct answer: A")
        return False

    else:
        print("\nPlease enter A, B, C, or D.")
        return multiple_choice()

# TRUE OR FALSEEEEEEEEE

def true_false():
    print("\n=== TRUE OR FALSE ===")
    print("Python is a programming language.")

    answer = input("\nAnswer (T/F): ").strip().upper()

    if answer == "T":
        print("\n✓ YOU ARE CORRECT!")
        return True

    elif answer == "F":
        print("\n✗ YOU ARE WRONG!")
        print("Correct answer: T")
        return False

    else:
        print("\nPlease enter T or F.")
        return true_false()

# IDENTIFICATIONNNNNNN

def identification():
    print("\n=== IDENTIFICATION ===")
    print("What keyword is used to define a function in Python?")

    answer = input("\nAnswer: ").strip().lower()

    if answer == "def":
        print("\n✓ YOU ARE CORRECT!")
        return True

    else:
        print("\n✗ YOU ARE WRONG!")
        print("Correct answer: def")
        return False


# -------------------------
# ROULETTE / SPINNER
# -------------------------

def spin():
    print("\nSpinning...")

    for _ in range(15):
        number = random.randint(1, 3)

        print(
            f"\r        [ {number} ]",
            end="",
            flush=True
        )

        time.sleep(0.08)

    final_number = random.randint(1, 3)

    print(f"\r        [ {final_number} ]")

    time.sleep(0.5)

    return final_number
    
# hmm uhh just to show that it is randomizing???!?!?!?!???????   not that needed
    
    

# -------------------------
# MAIN GAME
# -------------------------

def main():

    # Question typesss
    choices = {
        1: multiple_choice,
        2: true_false,
        3: identification
    }

    # Game dat assssssssssss
    score = 0
    total_questions = 5


    # -------------------------
    # START SCREEN
    # -------------------------

    clear_screen()


# Start of using IA (only in the layout or output)
    print("╔═══════════════════════════╗")
    print("          🎰 QUIZ ROULETTE          🏆 0 / 0")
    print("╚═══════════════════════════╝")

    print(f"\nYou will answer {total_questions} questions.")
    print("The roulette will randomly choose the question type.")

    input("\nPress ENTER to start...")


    # -------------------------
    # QUESTION LOOP
    # -------------------------

    for question_number in range(1, total_questions + 1):

        clear_screen()

        # Header with current score
        print("╔═══════════════════════════╗")
        print(
            f"          🎰 QUIZ ROULETTE          "
            f"🏆 {score} / {question_number - 1}            "
        )
        print("╚═══════════════════════════╝")

        print(f"\nQuestion {question_number} / {total_questions}")


        # -------------------------
        # SPIN THE ROULETTE
        # -------------------------

        number = spin()

        print(f"\n🎯 RESULT: {number}")


        # -------------------------
        # SELECT QUESTION TYPE
        # -------------------------

        question = choices[number]


        # -------------------------
        # ASK QUESTION
        # -------------------------

        correct = question()


        # -------------------------
        # UPDATE SCORE
        # -------------------------

        if correct:
            score += 1


        # -------------------------
        # SHOW CURRENT SCORE
        # -------------------------

        print(f"\n🏆 SCORE: {score} / {question_number}")


        # -------------------------
        # NEXT QUESTION
        # -------------------------

        if question_number < total_questions:
            input("\nPress ENTER for the next question...")


    # -------------------------
    # FINAL RESULT
    # -------------------------

    clear_screen()

    print("╔═══════════════════════════╗")
    print(
        f"          🎉 QUIZ COMPLETE!         "
        f"🏆 {score} / {total_questions}          "
    )
    print("╚═══════════════════════════╝")

    print(f"\n🏆 FINAL SCORE: {score} / {total_questions}")


    # -------------------------
    # FINAL MESSAGE (dunno if the emoji is right thing or nah)
    # -------------------------

    if score == total_questions:
        print("🌟 PERFECT SCORE!")

    elif score >= 3:
        print("👏 GOOD JOB!")

    else:
        print("📚 KEEP PRACTICING!")


    input("\nPress ENTER to exit...")


# -------------------------
# PROGRAM START
# -------------------------

# may dinagdag si ai idk what is the use ofnit

if __name__ == "__main__":

    try:
        main()

    except (KeyboardInterrupt, EOFError):
        print("\n\nInterrupted. Goodbye!")