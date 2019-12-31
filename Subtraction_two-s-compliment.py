# this function converts decimal numbers to binary
def decimal_to_binary(n):
    a=[]
    while n>0 :
        a.append(n%2)
        n=n//2
    b=[]
    for i in range(0,len(a)):

        b.append(a[len(a)-i-1])
    
    return b    

# this function converts binary numbers to decimals   
def binaryTodecimal(n): 
      
    s, i= 0, 0
    while(n != 0): 
        dec = n % 10
        s = s + dec * pow(2, i) 
        n= n//10
        i += 1
    return s   

# this function calculates two's compliment
def compliment(n):
    for i in range(0,len(n)):
        if n[len(n)-i-1]==1:
            index=len(n)-1-i
            break
        else:
            continue
    for i in range(0,index):
        if n[i]==1:
            n[i]=0
        else:
            n[i]=1
    
    return n 


# this function adds two binary no.s of same length
def add_bin(m,n):
    n.reverse()
    m.reverse()
    p=[]
    for i in range(0,len(m)+1):
        p.append(0)
    
        

    o=[]
    for i in range(0,max(len(n),len(m))):

        if n[i]==0 and m[i]==0 and p[i]==0:

            o.append(0)
            p[i+1]=0
            
        elif n[i]==0 and m[i]==0 and p[i]==1:
            o.append(1)
            p[i+1]=0
            
        elif n[i]==0 and m[i]==1 and p[i]==0:
            o.append(1)
            p[i+1]=0
            
        elif n[i]==0 and m[i]==1 and p[i]==1:
            o.append(0)
            p[i+1]=1
            
        elif n[i]==1 and m[i]==0 and p[i]==0:
            o.append(1)
            p[i+1]=0
            
        elif n[i]==1 and m[i]==0 and p[i]==1:
            o.append(0)
            p[i+1]=1
            
        elif n[i]==1 and m[i]==1 and p[i]==0:
            o.append(0)
            p[i+1]=1
            
        elif n[i]==1 and m[i]==1 and p[i]==1:
            o.append(1)
            p[i+1]=1
            
        

    o.reverse()
    return o


# this is main functiion 

x=input('Enter the first number:')
y=input('Enter the second number:')

x=int(x)
y=int(y)

x=decimal_to_binary(x)
y=decimal_to_binary(y)

x=[0]+x
y=[0]+y
q=[]
if len(x)>len(y):
    for i in range(0,len(x)-len(y)):
        q.append(0)
    y=q+y
if len(y)>len(x):
    for i in range(0,len(y)-len(x)):
        q.append(0)
    x=q+x



z=compliment(y)


v=add_bin(x,z)



if v[0]==1:
    f=compliment(v)
    u=int("".join(map(str,f)))
    print('The answer for this operation is:-',binaryTodecimal(u))

else :
    u=int("".join(map(str,v)))
    print('The answer for this operation is:',binaryTodecimal(u))


    









    







   

        
    

  
