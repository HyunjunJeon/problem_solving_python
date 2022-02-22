import sys


def solve(data: str):
    operator_stack = list()
    res = ""
    for i in data:
        if i.isdecimal():
            res += i
        else:
            if i == "(":
                operator_stack.append(i)
            elif i == "*" or i == "/":
                while operator_stack and (operator_stack[-1] == "*" or operator_stack[-1] == "/"):
                    res += operator_stack.pop()
                operator_stack.append(i)
            elif i == "+" or i == "-":
                while operator_stack and operator_stack[-1] != "(":
                    res += operator_stack.pop()
                operator_stack.append(i)
            elif i == ")":
                while operator_stack and operator_stack[-1] != "(":
                    res += operator_stack.pop()
                operator_stack.pop() # "(" 를 없애버려야 함

    while operator_stack:
        res += operator_stack.pop()

    return res


if __name__ == "__main__":
    sys.stdin = open("/pythonalgorithm_formac/섹션 5/3. 후위표기식 만들기/in1.txt", "rt")
    middle_equation = input()
    print(solve(middle_equation))