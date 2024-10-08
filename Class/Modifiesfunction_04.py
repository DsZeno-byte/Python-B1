# write a function that take one input parameter (n) and evaluates an expression  a=n*10,for all values between 0 to n
import time
ns=[12313212,232211532,12545332,5448446451]
n=10000
def eva(n):
    for i in range (0,n):
        a=i*10
    print (a)
# def wrapper(fun,n):        
def wrapper(fun,*args,**kwargs):
    
    def wrapped(*args,**kwargs):
        start_time=time.time()*100000

        fun(*args,**kwargs)

        end_time=time.time()* 1000000
        print(f" For n={n} \n Execution time is {end_time-start_time} micro second")
    # wrapped(*args,**kwargs) 
    return wrapped
# Main Function
@wrapper #decorator
def eva(n):
    for i in range (0,n):
        a=i*10
# n=100000
# for n in ns:
# wrapped_fn=wrapper(eva,n)

# wrapped_fn(n)
# wrapper(eva,n)

@wrapper
def random1(n):
    n**n
eva(n)
