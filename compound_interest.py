def  compoundInterest(p,r,t):
	a= p * (pow((1 + r / 100), t))
	ci=a-p 
	return ci
   
p = float(input("Enter the principal amount : "))
t = float(input("Enter the number of years : ")) 
r = float(input("Enter the rate of interest : "))
i=1
while i<=t:
	compi =  compoundInterest(p, r, i) 
	print("Compound interest for",i,"years",compi)
	i=i+1
