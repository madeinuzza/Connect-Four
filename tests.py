while True:
    user_input = input("Enter an integer between 1 and 8: ")

    try:
        num = int(user_input)

        if 1 <= num <= 8:
            print(f"Valid input: {num}")
            break
        else:
            print("Number not in range 1–8. Try again.")

    except ValueError:
        print("Input is not an integer. Try again.")
