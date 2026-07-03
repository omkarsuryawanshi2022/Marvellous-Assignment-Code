# ------------------------ List       Tuple
#                          Yes         Yes #
#                          yes          yes
#                          yes         No


# ordered
# Indexed
# mutable
# Heterohenious             Yes         Yes
def main():
    data1 = [10,3.14,True,"Pune"]  # list
    data2 = (10,3.14,True,"Pune")  # tuple

    print(data1)
    print(data2)

    print(data1[0])
    print(data2[0])
    

if __name__ == "__main__":
    main()
