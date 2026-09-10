def f_to_c():
    proceed = True
    while proceed:
        temp = input("Enter temperature in F: ")
        temp = int(temp)
        tempC = (temp - 32) * 5/9
        print(f"Temperature in C: {tempC:.1f}")
        print("Do you wish to continue? (y/n)")
        choice = input()
        if choice == "y":
            proceed = True
        else:
            proceed = False
    return

if __name__ == '__main__':
    f_to_c()
