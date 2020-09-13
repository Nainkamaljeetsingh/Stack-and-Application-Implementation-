# The precedence of operator is based on the python precedence
from Stack import Stack
def gt_priority(p1,p2):
    if p2 !='*':
        if p2 not in '{([':
            if(p1>p2):
                return False
            else:
                return True
    else:
         True

def inf_postfix(infix_exp):
    s=Stack()
    post_exp=[]
    i=0
    while i<len(infix_exp):
        #print(post_exp)
        #print(s.items)
        read=infix_exp[i]
        if read in '[{(':
            s.push(read)
        elif read in '+*-/^':
            if s.isempty():
                s.push(read)
            else:
                top=s.peek()
                if gt_priority(read,top):
                    s.push(read)

                else:
                    if top not in'[{(':
                        k=s.pop()
                        if k not in'({[)}]':
                            post_exp.append(k)
                    s.push(read)
        elif read in ')}]':
            while str(s.peek()) not in '{[(':
                post_exp.append(s.pop())
                s.cap+=1
        else:
            post_exp.append(read)
        i+=1
    while not s.isempty():
        k=s.pop()
        if k not in '[{(':
            post_exp.append(k)
    post_exp.reverse()
    return post_exp
inp=input('Enter the infix expression')
k=reversed(inp)
k=''.join(k)
post=inf_postfix(k)
print(''.join(post))