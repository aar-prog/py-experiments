#print only even numbers
#loop from 0-9

    
def is_even(x):
    if x % 2==0:
        return True
    else:
        return False
    
for x in range(10):
    if is_even(x):
        print(x)    
    
