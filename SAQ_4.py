def division():
    try:
        numerator = float(input("\nEnter the first number: "))
        denominator = float(input("\nEnter the second number: "))
        result = numerator / denominator
    except ValueError:
        print("\nError: Invalid input! Please enter numeric values.")
    except ZeroDivisionError:
        print("\nError: Any numbers cannot be divide by zero!")
    else:
        print(f"\nThe result is: {result}")
    finally:
        print("\nThe division has been done without any error.")

division()
