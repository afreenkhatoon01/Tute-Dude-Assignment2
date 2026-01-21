#Task 1 check whether the number is even or odd
num=int(input("Enter a number:"))
if num%2==0:
    print(num,"is an even number.")
else:
    print(num,"is an odd number.")

#Task 2 : Find the sum of numbers from 1 to 50
sum=0
for i in range(1,51):
    sum+=i
    print("the sum of numbers from 1 to 50 is:",sum)
    
