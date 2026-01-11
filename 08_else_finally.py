try:
    num = int(input("Enter a number: "))
    print(10 / num)
except Exception as e:
    print("Error:", e)
else:
    print("Calculation successful")
finally:
    print("Program finished")
