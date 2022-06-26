from conversion_module import *
#To add the given input numbers after converting them into binary.
def function_addition(list1,list2):
    Cin=0
    add=[] 
    for i in range(7,-1,-1):
        A=list1[i]
        B=list2[i]
        Var1 = A ^ B #XOR Gate         
        Var2 = A & B #AND Gate  
        Var3 = Var1 & Cin       
        Sum = Var1 ^ Cin       
        Cout = Var2 | Var3 #OR Gate 
        Cin = Cout
        add.append(Sum)
    add.append(Cin)
    #If the addition is 9 bits.
    if Cin==1:
        add = "ERROR!!! The addition exceeds 8 bits"
    else:
        add = listToDigits(reverse(add)) #Changing the added number to digit and reversing it if it is 8 bits.
    return add

