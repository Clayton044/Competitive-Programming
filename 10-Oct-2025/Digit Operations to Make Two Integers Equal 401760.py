# Problem: Digit Operations to Make Two Integers Equal - https://leetcode.com/problems/digit-operations-to-make-two-integers-equal/description/?envType=problem-list-v2&envId=shortest-path

prime = [True for _ in range(10001)] 
p=2

while p*p <= 10001:
    if prime[p]:
        for i in range(p*p, 10001, p):
            prime[i]=False
    p+=1
class Solution:
    def minOperations(self, n: int, m: int) -> int:        
        if n==1 and m==1:
            return 1
        if prime[n]:
            return -1
        heap=[(0,n)]
        seen = set()

        while len(heap) > 0:
            cost, num = heapq.heappop(heap)

            if num == m:
                return cost + num
            if num in seen:
                continue
            seen.add(num)
            list_num = list(str(num))

            for i, digit in enumerate(list_num):
                copy = deepcopy(list_num) 

                if digit == '9':
                    copy[i] = '8'
                    new_num = "".join(copy)

                    if not prime[int(new_num)] and new_num[0] != 0:
                        heapq.heappush(heap, (cost+num, int(new_num)))
                elif digit == '0':
                    copy[i] = '1'
                    new_num = ''.join(copy)

                    if not prime[int(new_num)] and new_num[0] != 0:
                        heapq.heappush(heap, (cost+num, int(new_num)))
                else:
                    digit = int(digit)
                    copy[i] = str(digit - 1)
                    new_num = ''.join(copy)

                    if not prime[int(new_num)] and new_num[0] != 0:
                        heapq.heappush(heap, (cost+num, int(new_num)))
                    
                    copy[i] = str(digit + 1)
                    new_num =''.join(copy)

                    if not prime[int(new_num)] and new_num[0] != 0:
                        heapq.heappush(heap, (cost+num, int(new_num)))

        return -1            

        
