# Problem: A - Frog 1 - https://atcoder.jp/contests/dp/tasks/dp_a

    n = int(input())
    h = list(map(int, input().split()))
    
    if n == 1:
        print(0)
        return
    if n == 2:
        print(abs(h[0] - h[1]))
        return
    
    # Only keep track of last two dp values
    prev2 = 0                 # dp[0]
    prev1 = abs(h[0] - h[1])  # dp[1]
  
    for i in range(2, n):
        # dp[i] = min( dp[i-1] + |h[i-1]-h[i]|, dp[i-2] + |h[i-2]-h[i]| )
        cost1 = prev1 + abs(h[i-1] - h[i])      # jump from i-1
        cost2 = prev2 + abs(h[i-2] - h[i])      # jump from i-2
        current = min(cost1, cost2)
        
        prev2 = prev1
        prev1 = current
    
    print(prev1)