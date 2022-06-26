#Function to convert decimal to binary
def DToB(n):
        bit = []
        counter=0
        while counter !=8:
                remainder=n%2
                bit.append(remainder)
                n=n//2
                counter+=1
        return bit
#Function to reverse the list numbers
def reverse(revNum):
        rev=[]
        for i in range(len(revNum)-1,-1,-1):
                rev.append(revNum[i])
        return rev
#Function to change the list into digits
def listToDigits(bitList):
        temp=""
        for i in range (0,len(bitList),1):
                temp = temp + str(bitList[i])
                digit = int(temp)
        return digit
