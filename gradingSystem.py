#the system should ask the user to enter their marks
#calculate the average mark and assign grade

userinput = 0
sum = 0
average = 0
inputs = 0
grade = "F"

print("Enter the marks or q to exit")

while userinput != "q":
    userinput = input("Enter the marks: ")

    newValue = 0

    if userinput=="q":
        break


    else:
        try:

            newValue=float(userinput)
            sum += newValue
            inputs += 1
        except ValueError as e:
            print("Use numbers only!!")


    if inputs == 3:
        average = sum/inputs
        new_average = round(average,2)

        if new_average>100:
            print("Invalid")

        elif new_average>=75:
            grade="A"
            print(f"The average mark is: {new_average}")
            print(f"Your grade is: {grade}")

        elif new_average>=60:
            grade="B"
            print(f"The average mark is: {new_average}")
            print(f"Your grade is: {grade}")

        elif new_average>=50:
            grade="C"
            print(f"The average mark is: {new_average}")
            print(f"Your grade is: {grade}")

        elif new_average>=40:
            grade="D"
            print(f"The average mark is: {new_average}")
            print(f"Your grade is: {grade}")

        else:
            grade="F"
            print(f"The average mark is: {new_average}")
            print(f"Your grade is: {grade}")

        inputs = 0
        sum = 0



















