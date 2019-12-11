def is_prime(x):
    for a in range(2, x):
        if x%a==0:
            return False
        
    return True
    
    
    

for x in range(3,10000):
    if is_prime(x):
        print(x)
        
