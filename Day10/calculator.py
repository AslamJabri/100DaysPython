from art import logo
def add (n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide (n1,n2):
    return n1/n2


operations = {
    "+": add,
    "-":sub,
    "*":multiply,
    "/" : divide
}

def calculator():
    print(logo)
    num1 = float(input("what's your number? "))
    for symbol in operations:
        print(symbol)
            
    is_again = True

    while is_again:
    
        symbol_operation = input("Pick an Operation? ")
        num2 = float(input("What's your number? "))

        calculation_function = operations[symbol_operation]
        answer = calculation_function(num1,num2)
        
        print(f"{num1}{symbol_operation}{num2} = {answer}")
        
        if input(f"Type 'y' to continue calculating with {answer} , or type 'n' for start again and x for exit ").lower()=="y":
            num1 = answer
        elif input(f"Type 'y' to continue calculating with {answer} , or type 'n' for start again and x for exit ").lower()=="n":
            is_again=False
            calculator()
        else:
            break

calculator()
