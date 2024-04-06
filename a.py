##Daily Coding Problem: Problem #2 [Hard]
##This problem was asked by Uber.
##
##Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
##
##For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
##
##Follow-up: what if you can't use division?

prob_num= 2
print(f'Daily Problem Solving, Problem number: {prob_num}')
def solve():
    tmul,mul,ans= 1,1,[]
    li= [int(i) for i in ((input()).split())]
    for i in li:
        tmul*= i

    for i in range(len(li)):
        for j in range(len(li)):
            if j==i:
                continue
            mul*= li[j]
        ans.append(mul)
        mul= 1
    return ans
            
            
ans= solve()
print(ans)
