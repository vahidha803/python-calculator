a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
operation=input("Enter operation(ADD,SUb,MUL,DIV):").upper()
if operation=="ADD":
    print("Result:",a+b)
elif operation=="SUB":
    print("Result:",a-b)
elif operation=="MUL":
    print("Result:",a*b)
elif operation=="DIV":
    print("Result:",a/b)
else:
    print("Invalid operation")
