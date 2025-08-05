option = -1

while option != 0:
    option = int(input("[1] Withdraw \n [2] Statement \n [3] Exit"))

    if option == 1:
        print("Withdrawing money...")
    elif option == 2:
        print("Displaying statement...")
    else:
        print("Thank you for using our banking system, see you soon!")
        break