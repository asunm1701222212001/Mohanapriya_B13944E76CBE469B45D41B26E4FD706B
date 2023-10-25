def Fact_rec(n):
  if n==0 or n==1:
   return 1
  else:
    return n* Fact_rec(n-1)
number =2
res= Fact_rec(number)
print("the Factorial of{} is{}.".
format (number,res))      