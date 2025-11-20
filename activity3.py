num = int(input("Enter a number: "))
t = num
numlen = 0
while t > 0:
    numlen = numlen + 1
    t = int(t / 10)
if numlen >= 4:
    numlen = int(numlen / 2)
    check = 0
    while num > 0:
        rem = num % 10
        if check == numlen:
            midone = rem
        elif check == (numlen - 1):
            midtwo = rem
        num = int(num / 10)
        check = check + 1
    product = midone * midtwo
    print("\nproduct of mid digits (" +str(midone) + "*" + str(midtwo)+") = ",product)
else:
    print("Please enter more than 4 digit number")
