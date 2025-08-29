a= input("Enter number: ")
b=""
for i in range (len(a)):
    b=b+a[len(a)-1-i]
if b==a:
    print("Number is palindrome.")
else:
    print("Number is not palindrome. ")