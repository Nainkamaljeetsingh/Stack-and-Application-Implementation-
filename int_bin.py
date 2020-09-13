'''num=int(input('Enter the number '))
bin_num=[]
is_true=True
while is_true:
    bin_num.append(num%2)
    num=num//2
    if num==0:
        is_true=False
for i in range(len(bin_num)):
    s=str(bin_num[i])
    print(s)
print(bin_num.reverse())'''
from Stack import Stack
def to_binary(num):
    s=Stack()
    while(num>0):
        s.push(num%2)
        num=num//2
        s.cap+=1
    res=''
    while not s.isempty():
        res+=str(s.pop())
    return  res
num=int(input('Enter the number'))
res=to_binary(num)
k=int(res,2)
print(f'The binary form of {k} is {res}')
