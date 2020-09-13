from Stack import Stack
def operate(k,j,ch):
    if ch == '+':
        return k+j
    elif ch =='-':
        if k>j:
            return k-j
        else:
            return j-k
    elif ch == '*':
        return k*j
    elif ch =='/':
        if j!=0:
            return k/j
        else:
            return 0
    elif ch == '^':
        return k^j
    else:
        pass
def post_eval(post_exp):
    s=Stack()
    i=0
    while i < len(post_exp):
        ch=post_exp[i]
        if ch in '+-*/^' and not  s.isempty():
            k=int(s.pop())
            j=int(s.pop())
            s.push(operate(k,j,ch))
        else:
            s.push(ch)
        i+=1
    return int(s.peek())
post_exp=input('Enter the postfix expression(only numbers allowed')
res=post_eval(post_exp)
print('The result is :',res)