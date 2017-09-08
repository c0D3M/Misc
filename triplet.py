import math
def permute(a , b):
	if(b==0 or a==b):
		return 1
	r = a
	val = 1
	while r >= (a-b+1):
		val = val *r;
		r = r-1;
	return val;
	
#print permute(365, 10)

M = 3 # input..basically how many people can share birthday
P = 0 # probability
N = 20 # Number of people, starts a loop, keep adding people 1-by-1 and calculate probability 
k = 2 # Group size ..starts from 2 upto M-1

while True:
	k =2
	P =0
	while k <= (M-1):
		i =0
		P =0
		while i <= math.floor(N/k):
			a = permute(N, k*i)
			b = permute(365, N-i)
			c = math.pow(math.factorial(k), i)
			d = math.pow(365, N)
			e = math.factorial(i)
			x =  b /d /e / c 
			x = x * a	
			P =P + x
			i = i+1
		k = k+1
		if(k>=N):
			break;
		
	if(P<=0.5):
		break;
	N = N+1;
print N	
