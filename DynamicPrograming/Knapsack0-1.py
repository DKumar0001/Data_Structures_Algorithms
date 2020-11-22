#Knapsack bag weight capacity = w
# Number of items each having wights and Profit = n
# Weight of item = w1,w2.........wn
# Profit (Margin) of each item = P1,P2.......Pn
# We have to collect the obects with maximizing marign


def knapsack_calculator(bag_size, weights, profits, num_items):
    k = [[0 for i in range(bag_size+1)] for i in range(num_items+1)]
    for i in range(num_items+1):
        for w in range(bag_size+1):
            if i == 0 or w == 0:
                k[i][w] = 0
            elif weights[i-1] <= w:
                k[i][w] = max(profits[i-1] + k[i-1][w-weights[i-1]], k[i-1][w])
            else:
                k[i][w] = k[i-1][w]

    for w in k:
        print(w)
    return k





#Enter Knapsack bag weight, number of items to choose from, their weights and Profits

bag_size = int(input("Enter the weight of knapsck"))
num_items = int(input("Enter number of items you have in your shopping list"))

weights = []
profits = []

for i in range(0, num_items):
    weight = int(input("Enter the weight of item"))
    profit = float (input ("Enter the profit of item"))
    weights.append(weight)
    profits.append(profit)

num_items = len(profits)
k = knapsack_calculator(bag_size, weights, profits, num_items)
print("Maximum Knapsack Profit is",k[num_items][bag_size])

