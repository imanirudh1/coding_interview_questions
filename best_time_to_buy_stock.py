def maxProfit(prices):
    max_profit=0
    min_val=float('inf')
    for i in range(len(prices)):
        if prices[i]<min_val:
            min_val=prices[i]
        elif prices[i]-min_val>max_profit:
            max_profit=prices[i]-min_val
    return max_profit        
prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))