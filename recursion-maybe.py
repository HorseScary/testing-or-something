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


#Im pretty sure this is a correct use of recursion?

def countToOneHundred(a):
    a += 1
#adds 1 to a before doing anything else!
    if a != 10:
        return(countToOneHundred(a))
#if a is not at the max value (10) the function returns itself

    else:
        return(f"You counted to 10!\na = {a}")
#if a is not not equal to 10 than that means it is equal to 10, and the program is done. 
#this returns the final 

print(countToOneHundred(0))