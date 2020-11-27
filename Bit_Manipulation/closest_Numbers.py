# Closest (or Next) smaller and greater numbers with same number of set bits

def next_greater(num):
    res = num
    if num != 0:

        # Find the rightmost 1 position
        right_one = num & -num

        #find the left pattern to merge
        left_pattern = num + right_one

        #get the right pattern to merge
        right_pattern = (num ^ left_pattern) >>right_one +1

        # Or both the patterns
        res = left_pattern | right_pattern

    return res

def next_smaller(num):
    return ~next_greater(~num)

num = int(input("enter the number for which you want to get next small and next large!!!"))

print("next greater",next_greater(num))
print("next smaller",next_smaller(num))
