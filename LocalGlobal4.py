no = 11  # Global variable

def Display():
    global no
    no = 21
    print("From Display :",no)

print("BEfore:",no)

    
Display()

print("After :",no)