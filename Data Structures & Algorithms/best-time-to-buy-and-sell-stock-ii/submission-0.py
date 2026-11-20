class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # int array prices
        # contains pricines on ith day
        # each day we can either buy and or sell
        # must have at most 1 share of stock at all times
        # buy low sell high
        # we add increase in stock prices to total profit
        # O(n) loop through array
        # 1-5 profit 4
        # 3-6 profit 3
        # when we see an increase we can look ahead

        profit = 0
        
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i-1]

        return profit

