from six.moves import input

print("Convert temperature from C to F")
print("Press c to exit program")
ctemp = input("Please input number of C convert to F temperature: ")
while str(ctemp) != "c":
    if (ctemp.isdigit()):
        number_convert = (1.8 * int(ctemp)) + 32
        print(str(ctemp) + ":F" + " -> " + str(number_convert) + ":C")
    else:
        print("Your input has wrong value. Please try again with value is number")
    ctemp = input("Please input number of C convert to F temperature: ")
    if (str(ctemp) == "c"):
        print("Thank you for using our application")
        exit
