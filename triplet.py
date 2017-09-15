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

def combi(n, r):
	return permute(n, r) / math.factorial(r)
	
#print permute(365, 10)

M = 3 # input..basically how many people can share birthday
P = 0 # probability
N = 20 # Number of people, starts a loop, keep adding people 1-by-1 and calculate probability 
k = 2 # Group size ..starts from 2 upto M-1
'''
n = number of people
d = number of days
s = how many people can share birthday
'''
def computeProb(n, d, k):
	'''
	Example n=10, d=365  s=3 i.e. we are calculating probability that 3 can have same birthday
	i = 1  , j =1 to 10  this is same as all 100 people have independent birthday
	i = 2  , j = 1 to 5 
				j=1  ->1 group 2 people(2) and rest  8 people
				j=2  ->2 group 2 people(4) and rest  6 people
				j=3  ->3 group 2 people(6) and rest  4 people
				j=4  ->4 group 2 people(8) and rest  2 people
				j=5  ->5 group 2 people(10) and rest 0 people
				Rest people will again can be choosen in similar way , recurrence 
	'''
	if(k==1):
		return permute(d, n) / math.pow(d, n)
	
	X = 0
	for i in range(1, 1+int(math.floor(n/k))):
		p = combi(d, i) *  permute(n, i*k) / math.pow(math.factorial(k), i) / math.pow(d, i*k)
		#Now we are left with n -ik people, d-i days which can again we recursively calcualated
		q = 0
		for j in range(1, k):
			#print "calling recursive"
			q = q + computeProb(n -i*k, d-i, j)
			#print ("return recursive %0.2f" %q)
		if(q==0):
			q = 1;
		r = math.pow (d-i, n-i*k) / math.pow(d, n-i*k)
		X = X + (p*q*r)
		#print ("i=%0.2f p=%0.2f q=%0.2f r=%0.2f X=%0.2f ff=%0.2f" %(i, p, q, r, X, (p*q*r)))
	return X
while True:
	print ("M = %d N=%d" %(M, N))
	P =0
	for i in range(1, M):
		P = P + computeProb(N, 365, i);
		print ("N=%d P=%0.2f" %(N, P))
	if(P<=0.5):
		break
	N = N+1	