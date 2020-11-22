# Input a number
number = int (input("Enter a number"))
fib_series = [0,1]
for i in range(2,number+1):
    fib_series.append( fib_series[i-1]+fib_series[i-2])
print(len(fib_series))
