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
# 🎓 **Grading System in Python** 📊

Welcome to the **Grading System**! This simple Python program helps you input student scores and returns their corresponding grades based on predefined criteria. 📝

## 📜 **Features**:
- **Input Validation** ✅: Ensures scores are between 0 and 100.
- **Grade Calculation** 🎯: Automatically calculates and displays the grade based on the score.
- **User-Friendly** 🖥️: Easy to use with clear instructions.

## 💡 **How to Use**:
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/grading-system.git
    cd grading-system
    ```

2. Run the script:
    ```bash
    python grading_system.py
    ```

3. **Enter a score** when prompted (between 0 and 100). The system will return the corresponding grade.

## 📈 **Grading Scale**:
- **A**: 90 - 100 🎉
- **B**: 80 - 89 📚
- **C**: 70 - 79 📝
- **D**: 60 - 69 🔨
- **F**: 0 - 59 🚫

## 🔧 **Technologies Used**:
- Python 🐍
- Terminal/Command Line

## 🚀 **Contribute**:
Feel free to fork this repository and submit pull requests to improve or add new features. Your contributions are welcome! 🌱

## 📄 **License**:
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Thanks for checking out the Grading System! 🌟
