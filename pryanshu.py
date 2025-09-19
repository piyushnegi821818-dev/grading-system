def get_grade(score):
    # Check the score and return the corresponding grade
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def main():
    # Input score from the user
    score = float(input("Enter the score (0-100): "))

    # Validate score
    if score < 0 or score > 100:
        print("Invalid score! Please enter a score between 0 and 100.")
    else:
        # Get grade for the score
        grade = get_grade(score)
        print(f"The grade for a score of {score} is: {grade}")

if __name__ == "__main__":
    main()
