# Write a program which accepts marks and displays grade

def CheckGrade(marks):
    if marks >= 75:
        return "Distinction"
    elif marks >= 60:
        return "First Class"
    elif marks >= 50:
        return "Second Class"
    else:
        return "Fail"


def main():
    print("Enter marks:")
    marks = float(input())

    result = CheckGrade(marks)

    print("Grade is:", result)


if __name__ == "__main__":
    main()