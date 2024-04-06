##Daily Coding Problem: Problem #1 [Easy]
##This problem was recently asked by Google.
##
##Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
##
##For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
##
##Bonus: Can you do this in one pass?

prob_num= 1
print(f'Daily Problem Solving, Problem number: {prob_num}')

def solve(li:list, k:int):
    
    le= len(li)
    for i in range(le-1):
        for j in range(i, le):
            if li[i]+li[j] == k:
                return (i,j,True)
    return False   
            
            

li= [10, 15, 3, 7]
k= 17

ans= solve(li,k)
print(ans)
