def fibonacci(a):
    if(a==1):
        return 0
    if(a==2):
        return 1
    return fibonacci(a-1)+fibonacci(a-2)

def is_prime(a):
    if(a<0 or a==1):
        return False
    i=2
    while(i<a):
        if(a%i==0):
            return False
        i=i+1
    return True

def print_prime_factors(a):
    print(f"{a} = ",end="")
    ppm(a,0)

def ppm(a,i):
    if(i!=0):
        print("*",end=" ")
    i=i+1
    if(is_prime(a)):
        print(int(a),end=" ")
    else:
        j=2
        while(j<a-1):
           if(a%j==0):
               print(j,end=" ")
               ppm(a/j,i)
               break
           else:
                j=j+1