grade = int(input())
# grade = input()
# grade = int(grade)


if grade < 0 or grade > 100:
    print("error")
 
elif grade < 60:
    print("F")

elif grade < 70:
    print("D")

elif grade < 80:
    print("C")

elif grade < 90:
    print("B")

else:
    print("A")
    