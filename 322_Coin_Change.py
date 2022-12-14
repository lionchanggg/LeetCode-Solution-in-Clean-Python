class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        MAX = float('inf')
        
        dp = [MAX] * (amount + 1)
        dp[0] = 0
        
        for a in range(1, amount+1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], dp[a-c] + 1)
                    
        if dp[amount] != MAX:
            return dp[amount]
        
        else:
            return -1
