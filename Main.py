from conversion_module import *
from addition_module import function_addition
from input_module import function_input 
from output_module import function_output
print("PROGRAM TO ADD BINARY NUMBERS\n")
run="yes"
#Creating a loop to run the program untill said so.
while (run.lower())=="yes" or (run.lower()) =="y":
        num1 = function_input()
        num2 = function_input()
        bin1 = DToB(num1)
        bin2 = DToB(num2)
        rev1 = reverse(bin1)
        rev2 = reverse(bin2)
        dig1 = listToDigits(rev1)
        dig2 = listToDigits(rev2)
        bin_sum = function_addition(rev1,rev2)
        function_output(bin_sum,dig1,dig2)
        run = input("\nEnter yes or y to continue. Press any other key to exit.\n")
print("\n--------------------------------")
print("Thank you for using this program.")

