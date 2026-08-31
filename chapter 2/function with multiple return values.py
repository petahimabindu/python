def calculate(a,b):
  sum=a+b
  difference=a-b
  product=a*b
  return sum,differnce,product
a=int(input("enter first number:"))
b=int(input("enter second number:"))

s,d,p=calculate(a,b)

print("Sum=",s)
print("difference=",d)
print("product=",p)
