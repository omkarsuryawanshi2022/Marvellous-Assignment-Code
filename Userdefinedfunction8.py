def BigBazar():
    print("Inside Big Bazar")

    def Amul():
        print("Inside Amul Icecreame Parlor")

def main():
    BigBazar()   # Alloow
    Amul()   # error
    BigBazar.Amul()  # ERRor
     
if __name__  == "__main__":
    main()

    