from Stack import Stack
def ismatch(p1,p2):
    if p1 == '(' and p2 == ')':
        return  True
    elif p1 == '[' and p2 == ']':
        return  True
    elif p1 == '{' and p2 == '}':
        return  True
    else:
        return False
def is_para_bal(par_str):
    s=Stack()
    s.cap=len(par_str)
    is_bal=True
    i=0
    while i<len(par_str) and is_bal:
        par=par_str[i]
        if par in '({[':
            s.push(par)
        else:
            if s.isempty():
                is_bal=False
            else:
                top=s.pop()
                if not ismatch(top,par):
                    is_bal=False
        i+=1
    if s.isempty() and is_bal:
        return True
    else:
        return False
str_par=input('Enter the paranthesis String')
bal=is_para_bal(str_par)
if bal == True:
    print('The String is balanced')
else:
    print('The String is unbalanced')