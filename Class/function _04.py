# write a function that take one input parameter (n) and evaluates an expression  a=n*10,for all values between 0 to n
import time
n=100
def eva(n):
    for i in range (0,n):
        a=i*10
    print (a)
        
start_time=time.time()*100000

eva(n)


end_time=time.time()* 1000000


print(f" For n={n} \n Execution time is {end_time-start_time} micro second")