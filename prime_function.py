#function to check if the number is prime
def is_prime(x):
    for a in range(2, x):
        if x%a==0:
            return False
        
    return True

#loop through number range
for x in range(3,100):
    if is_prime(x):
        print(x)
        
