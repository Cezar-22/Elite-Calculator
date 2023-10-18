#Elite Calculator 2.0
print("Welcome to Elite Calculator 2.0") 
userAnswer = None
while userAnswer != "X":
    print("Press 1 for addition")
    print("Press 2 for subtraction")
    print("Press 3 for multiplication")
    print("Press 4 for division")
    print("Press 5 for parallelepiped volume calculation")
    print("Press 6 for rounding")
    print("Press 7 for binary")
    print("Press 8 for parallelogram calculation")
    print("Press 9 for Gauss sum formula")
    print("Press X to cancel")
    userAnswer = input("Type your answer here: ")
    if userAnswer == "1":
        term1 = int(input("What is number one?"))
        term2 = int(input("What is number two?"))
        ammount = term1 + term255
        print("The ammount is", ammount)
    elif userAnswer == "2":
        num1 = int(input("What is number one?"))
        num2 = int(input("What is number two?"))
        difference = num1 - num2
        print("The difference is", difference)
    elif userAnswer == "3":
        factor1 = int(input("What is number one?"))
        factor2 = int(input("What is number two?"))
        result = factor1 * factor2
        print("The result of the multiplication is", result)
    elif userAnswer == "4":
        num1 = int(input("What is number one?"))
        num2 = int(input("What is number two?"))
        result = num1 / num2
        print("The result of the division is", result)
    elif userAnswer == "5":
        num1 = int(input("What is number one?"))
        num2 = int(input("What is number two?"))
        num3 = int(input("What is number three?"))
        volume = num1*num2*num3
        print("The volume is", volume)
    elif userAnswer == "6":
        number = float(input("What is the number?"))
        roundedNumber = round(number)
        print("The number is now", roundedNumber)
    elif userAnswer == "7":
        number = int(input("What number do you want to convert to binary?"))
        answer = bin(number)
        print("Your answer is", answer)
    elif userAnswer == "8":
        lat1 = int(input("what number is the first angle proportional to?"))
        lat2 = int(input("what number is the second angle proportional to?"))
        lat3 = int(input("what number is the third angle proportional to?"))
        lat4 = int(input("what number is the fourth angle proportional to?"))
        proportionality = lat1+lat2+lat3+lat4
        k = 360/proportionality
        print("The first angle is", lat1*k ,"degrees")
        print("The second angle is", lat2*k ,"degrees")
        print("The third side is", lat3*k, "degrees")
        print("The fourth side is", lat4*k, "degrees")
    elif userAnswer == "9":
        num1 = int(input("What is the last number of the Gauss sum?"))
        num2 = num1 + 1
        answer = num1*num2/2
        print("Your answer is", answer)
    elif userAnswer == "X":
        print("We are grateful to know elite calculator has heped you today!")
