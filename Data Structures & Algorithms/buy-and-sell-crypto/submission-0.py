class Solution:
    def maxProfit(self, prices):
        left = 0
        profit = 0
        for right in range(len(prices)):
            if prices[left] > prices[right]:
                left = right
            else:
                profit = max(profit,prices[right] - prices[left])
        return profit
        
sol = Solution()
prices = [10,8,7,5,2]
print(sol.maxProfit(prices))
