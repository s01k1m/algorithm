q = int(input()) # 찾아야하는 q번째
num = 1
start = 666

while q != num: # 찾는 q랑 num이 같을때까지 
    start += 1 # bruteforce이므로 1씩 더하면서 다 확인한다
    if '666' in str(start): # 666이 들어가면
        num += 1 # num에 1을 더한다

print(start)