"""
To be honest I don't really know what recursion is or how it works
But this is my attempt to figure that out without like actually doing research 


My first attempt:

def countToOneHundred(a):
    if a == 10:
        return("You counted to 10!")
    
    a += 1
    print(a)
    countToOneHundred(a)

The idea was that instead of using a loop the function would just call itself until 'a' reached 10

The issue with this code (I think) is that the original function never returned anything.
The instance of the function that DID return the "You counted to 10!" string was 10 iterations down
"""



def countToOneHundred(a):
    if a == 10:
        return("You counted to 100!")
    
    a += 1
    print(a)
    countToOneHundred(a)
    
print(countToOneHundred(0))