# Write a program which accepts one number and prints that many numbers starting from 1
# Input: 5
# Output: 1 2 3 4 5

def Display(value):
    for i in range(1, value + 1):
        print(i, end=" ")


def main():
    print("Enter the number:")
    No1 = int(input())

    Display(No1)


if __name__ == "__main__":
    main()