add = lambda x, y: x + y
subtract = lambda x, y: x - y
multiply = lambda x, y: x * y
divide = lambda x, y: x / y if y != 0 else "Division by zero!"

if __name__ == "__main__":
  num1 = float(input("Enter first number: "))
  num2 = float(input("Enter second number: "))

  print("Sum:", add(num1, num2))
  print("Difference:", subtract(num1, num2))
  print("Product:", multiply(num1, num2))
  print("Quotient:", divide(num1, num2))