from operations.add import add_func
from operations.sub import sub_func
from operations.mul import mul_func
from operations.div import div_func



while True:
    inp1 = int(input("Enter the first no: "))
    inp2 = input("Enter the operation: ")
    inp3 = int(input("Enter the second no: "))

    if inp2 == "+":
        result=add_func(inp1,inp3)
        print(f"The result is : {result}")
    elif inp2 == "-":
        result=sub_func(inp1,inp3)
        print(f"The result is : {result}")
    elif inp2 == "*":
        result=mul_func(inp1,inp3)
        print(f"The result is : {result}")
    elif inp2 == "/":
        result=div_func(inp1,inp3)
        print(f"The result is : {result}")
    elif inp1 == "exit":
        break