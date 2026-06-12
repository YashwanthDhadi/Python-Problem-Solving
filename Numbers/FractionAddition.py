def FractionAdd(n1,n2,d1,d2):
     if d1 ==0 or d2==0:
         return "Undefined input"
     tn1 =d1
     tn2 =d2
     while tn2:
         tn1,tn2 = tn2,tn1%tn2
     gcd = tn1
     lcm = (d1*d2)//gcd
     numerator = (n1*lcm)//d1 + (n2*lcm)//d2

     return numerator,lcm
n1,d1 = 3,4
n2,d2 = 1,7
numerator, denominator = FractionAdd(n1,n2,d1,d2)
print(f"Numerator is {numerator} and Denominator is {denominator}")
