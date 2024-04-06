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
#myself
def solve():
    tmul,mul,ans= 1,1,[]
    
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
#from github :)
def solve2():
    ans=[]
    l_mul= [1 for i in range(len(li))]
    r_mul= [1 for i in range(len(li))]
    ans= [1 for i in range(len(li))]
    l_mul[0]= li[0]
    r_mul[len(li)-1]= li[len(li)-1]
    for i in range(len(li)-1):
        l_mul[i+1]= l_mul[i]*li[i+1]
        r_mul[len(li)-2-i]= r_mul[len(li)-1-i] * li[len(li)-2-i]
    ans[0], ans[len(li)-1]= r_mul[1], l_mul[len(li)-2]
    for i in range(1,len(li)-1):
        ans[i]= l_mul[i-1]* r_mul[i+1]
    return ans
            
li= [int(i) for i in ((input()).split())]         
ans1= solve()
ans2= solve2()
print(ans1,ans2)
