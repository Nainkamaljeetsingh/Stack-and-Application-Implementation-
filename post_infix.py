from Stack import Stack
def operate(k,j,ch):
    return j+ch+k

def post_eval(post_exp):
    s=Stack()
    i=0
    while i < len(post_exp):
        ch=post_exp[i]
        if ch in '+-*/^' and not  s.isempty():
            k=s.pop()
            j=s.pop()
            s.push(operate(k,j,ch))
        else:
            s.push(ch)
        i+=1
    return s.peek()
post_exp=input('Enter the postfix expression(only numbers allowed')
res=post_eval(post_exp)
print('The result is :',res)