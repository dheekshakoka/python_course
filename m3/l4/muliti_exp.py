try:
    n1 = int(input("Enter a number: "))
    n2 = int(input("Enter another number: "))
    res = n1/n2
except ValueError:
    print("You entered an invalid number.")
except ZeroDivisionError:
    print("You can't divide by zero.")
except Exception as e:
    print("Error", e)
finally:
    print("Thanks!")