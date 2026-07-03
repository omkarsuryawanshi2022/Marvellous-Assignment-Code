# Write a program which accept one character and check whether it is vowel or consonant
#  input  a
# output  Vovel

def CheckVovel(Character):
    if Character in ('a','e','i','o','u'):
        return True
    else:
        return
    return False
    
def main():
    print("Enter the character:")
    ch = input()

    Check  = CheckVovel(ch)

    if Check == True:
        print("Vovel")
    else:
        print("consonant")
    
    
if __name__ == "__main__":
    main()