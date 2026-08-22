n=int(input("Enter a number:"))

if n<=1:
  print("NOT a prime number")
else:
  for i in range(2,n):
    if n%i==0:
      print("NOT a prime number")
    else:
      print("Prime number")
