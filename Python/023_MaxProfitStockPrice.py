class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = 9999999
        max = 0
        
        for i in range(len(prices)):
            
            if prices[i] <= min:
                min = prices[i]
            
            profit_val = prices[i] - min
            if profit_val > max:
                max = profit_val

        return max

            


