class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # integer array prices
        # i = day
        # that i index indicates price at that day
        # choose one day to buy and one day to sell
        # max profit is when buy - sell is max
        # essentially smallest buy, biggest sell
        # can also not make buys which profit = 0
        # day to buy has to be before day to sell

        buy_price = prices[0]
        max = 0
        for i in range(len(prices)):
            profit = prices[i] - buy_price
            if profit > max:
                max = profit

            if prices[i] < buy_price:
                buy_price = prices[i]
        return max

        

        