n = int(input())

def GCD(a,b):
    if(b==0):
        return a
    else:
        return GCD(b,a%b)

arr=[]
for _ in range(n):
    arr.append(int(input()))

distances =[]
for i in range(len(arr)-1):
    distances.append(abs(arr[i+1]-arr[i]))

temp =distances[0]

for i in distances:
    temp = GCD(temp,i)

len_arr = (max(arr)-min(arr))//temp +1
print(len_arr-len(arr))