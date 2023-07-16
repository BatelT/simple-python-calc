# Perform operation and print result

def main():
   # Define ANSI color codes
   BLUE = "\033[94m"
   GREEN = "\033[92m"
   RED = "\033[91m"
   RESET = "\033[0m"


   # Prompt user for input
   num1 = float(input(BLUE + "Enter first number: " + RESET))
   num2 = float(input(BLUE + "Enter second number: " + RESET))
   operation = input(BLUE + "Enter operation (+, -, *, /): " + RESET)

   if operation == "+":
      result = num1 + num2
      print(GREEN + "Result: ", result, RESET)
   elif operation == "-":
      result = num1 - num2
      print(GREEN + "Result: ", result, RESET)
   elif operation == "*":
      result = num1 * num2
      print(GREEN + "Result: ", result, RESET)
   elif operation == "/":
      if num2 == 0:
         print(RED + "Error: division by zero!" + RESET)
      else:
         result = num1 / num2
         print(GREEN + "Result: ", result, RESET)    
   else:
      print(RED + "Error: invalid operation!" + RESET)
if __name__ == '__main__':
   main()