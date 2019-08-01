    UserName = input("Hey Uesr!! Input your Name")
    Len = len(UserName)
    print("User's Name length is", Len)

    if Len < 4:
        print("User#s Name is less than 4 Characters")

    elif 4 <= Len < 10:
        print("name is greater than or equal to 4 characters in the length but less than 10 characters long")

    else:
        print("Your name is very long")

