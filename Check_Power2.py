# Check wheather a given number is a power of 2 or 0

def Check_pow_2(num):
    if num ==0:
        return 0
    if(num & num-1) == 0:
        return 1

    return 2

switch ={
    0 : "Number is 0",
    1 : "Number is power of two",
    2 : "Number is neither power of 2 nor 0"
}

number = int(input("Enter a Number"))
case =Check_pow_2(number)
print(switch[case])
