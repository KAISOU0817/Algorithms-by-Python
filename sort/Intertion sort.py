number=[5,2,4,6,1,3,7,2,8,4]


for j in range(1, len(number)):
    key=number[j]
    i=j-1
    
    while number[i]>key and i>=0:
        number[i+1]=number[i]
        number[i]=key
        i=i-1

print(number)