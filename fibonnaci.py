a=10 
def fibonnaci(a):
    a,b=0,1
    for i in range(n):
        a,b=b,a+b
    return a

def rec_fibo(a):
    if a==0 or a==1:
        return a
    return fibonnaci(a-1)+fibonnaci(a-2) 


import sys 
sys.setrecursionlimit(10000)
cache={}
def memo_fibo(a):
    if a in cache:
        return cache[a]

    if a ==1 or a==2:
        value=1
    elif a>2:
        value=memo_fibo(a-1)+memo_fibo(a-2)
    cache[a]=value
    return value                

# print(memo_fibo(100))

# using Memoization
from functools import lru_cache

@lru_cache(maxsize=10000)
def memo_fibo_lru(a):
    if a ==1 or a==2:
       return 1
    elif a>2:
        return memo_fibo(a-1)+memo_fibo(a-2)
print(memo_fibo_lru(1000))    




#Memonization
def fibo(n,memo={}):
    if n in memo:
        return memo[n]
    if n <=2:
        return 1
    memo[n]=fibo(n-1,memo) + fibo(n-2,memo)
    return memo[n]
