# Write a program which accepts one number and prints numbers in reverse order
# Input: 5
# Output: 5 4 3 2 1

def Display(value):
    for i in range(value, 0, -1):
        print(i, end=" ")


def main():
    print("Enter the number:")
    No1 = int(input())

    Display(No1)


if __name__ == "__main__":
    main()