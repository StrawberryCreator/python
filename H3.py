while True:
    calc = input("What do you want to (+, -, *, /, //, **, % or stop)? ")
    if calc == "stop":
        break
    num1 = int(input("What's the first number? "))
    num2 = int(input("What's the second number? "))
    if calc == "+":
        ans = (num1 + num2)
        print (num1, "+", num2, "=", ans)
    elif calc == "-":
        ans = (num1 - num2)
        print (num1, "-", num2, "=", ans)
    elif calc == "*":
        ans = (num1 * num2)
        print (num1, "*", num2, "=", ans)
    elif calc == "/":
        ans = (num1 / num2)
        print (num1, "/", num2, "=", ans)
    elif calc == "//":
        ans = (num1 // num2)
        print (num1, "//", num2, "=", ans)
    elif calc == "**":
        ans = (num1 ** num2)
        print (num1, "**", num2, "=", ans)
    elif calc == "%":
        ans = (num1 % num2)
        print (num1, "%", num2, "=", ans)