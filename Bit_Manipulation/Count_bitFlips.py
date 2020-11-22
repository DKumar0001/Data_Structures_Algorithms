# Counting Number of flips needed to convert A to B

def bit_manipulation(a, b):
    count = 0
    c = a ^ b
    while c != 0:
        c &= c-1
        count +=1
    return count

A = int(input("input first number"))
B = int(input("Enter second number"))
cout = bit_manipulation(A,B)
print("Number of bits required are ",cout)
