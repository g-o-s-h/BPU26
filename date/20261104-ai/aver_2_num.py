num1 = input("The first number is: ")
num2 = input("The second number is: ")
avg_num = (float(num1) + float(num2)) / 2

print(f"The average of {num1} and {num2} is {avg_num}")

print("The average of {} and {} is {}".format(num1, num2, avg_num))

print("The average of %s and %s is %.1f" % (num1, num2, avg_num))
