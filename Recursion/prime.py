import math
def prime(num):
    if num ==0 or num ==1:
        return False
    elif(num ==2):
        return True
    else:
        for i in range(2,int(math.sqrt(num))+1):
            if num % i == 0:
                return False
        return True

num = int (input("Enter the number"))
Isit = prime(num)
switch = {
True :"The Number is prime",
False :"The Number is not Prime"
}
print(switch[Isit])
