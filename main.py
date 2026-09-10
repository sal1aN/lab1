def convert_f_to_C(tempF):
    try:
        tempF = int(tempF)
        tempC = (tempF - 32) * 5 / 9
    except ValueError:
        print("Please enter a valid temperature")
        return False
    return tempC

def run():
    proceed = True
    while proceed:
        temp = input("Enter temperature in F: ")
        tempC = convert_f_to_C(temp)
        if tempC:
            print(f"Temperature in C: {tempC:.1f}")
            print("Do you wish to continue? (y/n)")
            choice = input()
            if choice == "y":
                proceed = True
            else:
                proceed = False
    return

if __name__ == '__main__':
    run()
