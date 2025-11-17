def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
operation_dict={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
def calculator():
    number1=float(input("Enter first number:"))
    for symbol in operation_dict:
        print(symbol)
    should_continue=True
    while should_continue:
        operation_symbol=input("Pick an operation:")
        number2=float(input("Enter next number:"))
        calculation_function=operation_dict[operation_symbol]
        output=calculation_function(number1,number2)
        print(f"{number1} {operation_symbol} {number2} = {output}")
        should_continue=input(f"Type 'y' to continue calculating with {output}, or type 'n' to start a new calculation, or type 'e' to exit:")
        if should_continue=="y":
            number1=output
        elif should_continue=="n":
            should_continue=False
            calculator()
        else:
            should_continue=False
            print("Thank you")
calculator()
        
