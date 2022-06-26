#Function to take input values.
def function_input():
    correct = False
    while correct == False:
        try:
            num = int(input("Enter a number: "))
            #To check if the number is less than 0 or greater than 255.
            if(num < 0 or num > 255):
                print("ERROR!!!\nThe number should be greater than 0 but less than 255\n")
            else:
                correct = True
                return num
        except:
            #Error if string value is entered
            print("ERROR!!!\nPlease input a valid number\n")
