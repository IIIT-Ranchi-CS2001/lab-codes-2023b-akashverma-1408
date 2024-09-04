def check_palindrome():
    S = input("Enter the string: ")
    S = S.replace(" ", "").lower()
    if S == S[::-1]:
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")

check_palindrome()  