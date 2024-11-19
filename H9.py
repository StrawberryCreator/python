#do any calculation the user wants
while True:
    print ("-"*50)
    cal = input("What do you want to (+, -, *, /, //, **, % or stop)? ")
    if cal == "stop":
        break
    print ("-  "*17)
    num1 = int(input("What's the first number? "))
    print ("-   "*13)
    num2 = int(input("What's the second number? "))
    print ("- "*25)
    if cal == "+":
        ans = (num1 + num2)
        print (num1, "+", num2, "=", ans)
    elif cal == "-":
        ans = (num1 - num2)
        print (num1, "-", num2, "=", ans)
    elif cal == "*":
        ans = (num1 * num2)
        print (num1, "*", num2, "=", ans)
    elif cal == "/":
        ans = (num1 / num2)
        print (num1, "/", num2, "=", ans)
    elif cal == "//":
        ans = (num1 // num2)
        print (num1, "//", num2, "=", ans)
    elif cal == "**":
        ans = (num1 ** num2)
        print (num1, "**", num2, "=", ans)
    elif cal == "%":
        ans = (num1 % num2)
        print (num1, "%", num2, "=", ans)