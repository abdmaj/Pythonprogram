base=int(input())
exp=int(input())
def power(base,exp):
    if(exp==1):
        return(base)
    if(exp!=1):
        return(base*power(base,exp-1))

print(power(base,exp))
