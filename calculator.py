def calculator():
    try:
        num1 = float(input("请输入第一个数字："))
        op = input("请输入运算符(+ - * /)：")
        num2 = float(input("请输入第二个数字："))
        if op == "+":
            res = num1 + num2
        elif op == "-":
            res = num1 - num2
        elif op == "*":
            res = num1 * num2
        elif op == "/":
            if num2 == 0:
                print("错误：不能除以0")
                return
            res = num1 / num2
        else:
            print("运算符非法")
            return
        print(f"结果：{res}")
    except ValueError:
        print("输入不是有效数字！")

if __name__ == "__main__":
    calculator()
