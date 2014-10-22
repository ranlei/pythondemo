def cacl(a, b, op):
    if op not in '+-*/':
        return "Please only type one of these characters '+-*/'"

    if op == '+':
        return str(str(a)+op+str(b)+'='+str(a+b))
    if op == '-':
        return str(str(a)+op+str(b)+'='+str(a-b))
    if op == '*':
        return str(str(a)+op+str(b)+'='+str(a*b))
    if op == '/':
        return str(str(a)+op+str(b)+'='+str(a//b))

if __name__ == "__main__":
    flag = True
    while flag:
        pass
        try:
            a = input("please this first number:")
        except:
            print("maybe you should input number.")
        b = input("please this second number:")
        op = raw_input("give me you want excution(+-*/):")
        if a and b and op:
            flag = False
            print(cacl(a, b, op))
