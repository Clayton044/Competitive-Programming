# Problem: C - Vacation - https://atcoder.jp/contests/dp/tasks/dp_c


data = input().split()

n = int(data[0])

activities = []
index = 1
for i in range(n):
    a = int(data[index])
    b = int(data[index+1])
    c = int(data[index+2])
    activities.append((a, b, c))
    index += 3

prev_a, prev_b, prev_c = 0, 0, 0

for i in range(n):
    a, b, c = activities[i]
    
    
    curr_a = a + max(prev_b, prev_c)  
    curr_b = b + max(prev_a, prev_c)  
    curr_c = c + max(prev_a, prev_b)  
    
    
    prev_a, prev_b, prev_c = curr_a, curr_b, curr_c

print(max(prev_a, prev_b, prev_c))

