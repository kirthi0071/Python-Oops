
num = int(input("Enter the Number:"))

if num <= 0:
    print("The number is not a positive integer.")
else:
    for i in range(2,num):
        if (num % i == 0):
            print(num, "is not a prime number")
            break
        else:
            print(num,"is a  prime number")

