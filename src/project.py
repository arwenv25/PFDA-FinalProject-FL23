
def two_option_menu():
    print("Welcome to the Image Insights Menue")
    print("Select 1 to analyze Color Profile")
    print("Select 2 to analyze Image Information")

    choice = input("Enter your choice here: ")

    if choice == "1":
        print("You chose analyze Color Profile!")
        # call respective code here from class above
    elif choice == "2":
        print("You chose analyze Image Information")
        # call respective code here from class above
    else:
        print("Invalid choice. Please choose either '1' or '2.'")



two_option_menu()

if __name__ == "__main__":
    main()

#Menu