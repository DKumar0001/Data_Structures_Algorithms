def find_non_repeat():
    sums = 0
    num1 = 0
    num2 = 0
    
    #  xor elements with each other elements duplicate elements will each other
    for i in range(len(arr)):
        sums = sums ^ arr[i]
        
    # Bitwise & the sum with it's 2's Complement
    # Bitwise & will give us the sum containing
    # only the rightmost set bit
    sums = sums & -sums

    for i in range(len(arr)):
        if(arr[i]  & sums ) > 0:
            num1 = num1 ^ arr[i]
        else:
            num2 = num2 ^ arr[i]
    print(num1, num2)



def main():
    # Enter number of iterataions and number of elements
    num = int (input("Number of arry you want to check"))
    for i in range(num):
        arr = list(map(int, input("Enter elements seprated by spacae").split()))
    # print (arr)
if __name__ = "__main__":
    
