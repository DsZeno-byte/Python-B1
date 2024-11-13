# write a program to create dic where keys are number and the values are square of number
# write a function that takes a dict and returns a dic where keys are value and valus are keys
n=50
res= [x**2 for x in range (0,n) if x  % 2==0]   
print(res)

res2={x:x**2 for x in range (0,n )if x%2==0}
print(res2)
def flip_dict(d1):
    assert isinstance(d1,dict),"Input is not a dictionary"
    flipped ={val:key for key,val in d1.items()}
    
    return flipped

print(f"flipped dictionary if \n{flip_dict(res2)}")

flip_dict(1)    
    
    
    
    
    # print type of dog
    # print type of cat