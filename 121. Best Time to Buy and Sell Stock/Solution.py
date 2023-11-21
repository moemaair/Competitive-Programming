from ast import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

    # Check length
        if len(prices) < 2:
            raise Exception('Need at least two stock prices!')
        
        # Start minimum price marker at first price
        min_stock_price = prices[0]
        
        # Start off with an initial max profit
        max_profit = prices[1] - prices[0]
        
        # Skip first index of 0
        for price in prices[1:]:
            
            
            # NOTE THE REORDERING HERE DUE TO THE NEGATIVE PROFIT TRACKING
            
            # Check the current price against our minimum for a profit 
            # comparison against the max_profit
            comparison_profit = price - min_stock_price
            
            # Compare against our max_profit so far
            max_profit = max(max_profit,comparison_profit)
            
            # Check to set the lowest stock price so far
            min_stock_price = min(min_stock_price,price)
        return max_profit    
            
            