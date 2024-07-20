#taking the input
a= int(input("Enter the first number:"))
b= int(input("Enter the second number:"))
try:
    c=a/b
    print("Result:",c)

except:
    print("Can't divide it to Zero...")

#the block will execute regardless of and exception
finally:
    print("Division operation attempted.")    