# Problem: B - Frog 2 - https://atcoder.jp/contests/dp/tasks/dp_b

    data = input().split()
    
    n = int(data[0])
    k = int(data[1])
    h = list(map(int, data[2:2+n]))
    
    # dp[i] = minimum cost to reach stone i (0-indexed)
    dp = [float('inf')] * n
    dp[0] = 0  # Start at stone 1 (index 0)
    
    for i in range(1, n):
        # Look back at most k steps
        for j in range(max(0, i - k), i):
            cost = abs(h[i] - h[j])
            dp[i] = min(dp[i], dp[j] + cost)
    
    print(dp[n-1])