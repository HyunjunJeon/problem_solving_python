import sys


def solve(data: str):
    # 연산자를 먼저 찾아서 그 앞에 2개 숫자와 그 연산자를 사용함
    stack = list()
    for x in data:
        if x.isdecimal():
            stack.append(x)
        else:
            a = int(stack.pop())
            b = int(stack.pop())
            if x == "*":
                stack.append(a * b)
            elif x == "/":
                stack.append(b / a)
            elif x == "+":
                stack.append(a + b)
            elif x == "-":
                stack.append(b - a)

    return stack[0]

if __name__ == "__main__":
    sys.stdin = open("/pythonalgorithm_formac/섹션 5/4. 후위식 연산/in1.txt", "rt")
    postfix_equation = input()
    print(solve(postfix_equation))