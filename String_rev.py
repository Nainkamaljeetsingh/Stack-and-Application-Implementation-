from Stack import *
string=input('Enter the string\n')
st=Stack()
i=0
st.cap=len(string)
rev=[]
while(i<len(string)):
    st.push(string[i])
    i+=1
j=len(string)
while(j>0):
    rev.append(st.pop())
    j-=1
print('The reversed String is ',''.join(rev))
print(st.pop())