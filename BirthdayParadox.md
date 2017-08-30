## Birthday Paradox
As per [Wikipedia](https://en.wikipedia.org/wiki/Birthday_problem) in a set of randomly chosen __n people__, some pair of them have same birthday.  

__P(collision) + P(no collision) = 1__  
So we will calculate the probability of no collission   
1st person can choose birthday in 365 ways .. __365 / 365__  
2nd person, in order to have no collission at all, can choose birthday in 364 ways ..hence probability = __364 /365__  
3rd person, in order to have no collission at all, can choose birthday in 363 ways ..hence probability = __363 /365__  

P(no colission) = 365/365 * (364 / 365) * (363 /365) ..........  
P( no collission) = 1 * (1 - 1/365) * (1- 2/365) ..... (1* n-1/365)  
P (collssion) = 1 - P(no collission)  

Sometime you are asked find number of people such that P(collsion) >= 0.5  
This can be found easily using a computer program  

```c
double p = 1;
int i= 1;
do{
   p *= (1- i/365);
}while(p<0.5);
```
## Birthday Problem for triplet
In this problem, 3 people in a random group of n people share same birthday.  
This is slightly trickier than above problem.  
P(3 share a birthday) + P(3 didnt share) = 1  
Lets see how many possible way 3 people out of n didn't share a birthday  
1. All 'n' people have different birthday
2. 1 pair of people share a birthday and then n-2 people have different birhday.  
3. 2 pair of people share a birthday and then n-4 people have different birhday.  
.......
n+1. n/2 pair of people share a birthday.

So essentially we have to sum all the above possible ways  
1. All 'n' people have different birthday  
This would be 365 * 364 * 363 .... (365 - (n-1)) / 365^n  
365 * 364 * 363 .... (365 - (n-1)) can be termed as P(365, n)  which is actually 365C<sub>n</sub>  * n!

2. 1 pair of people share a birthday and then n-2 people have different birthday.  

Number of ways 1 pair of people can be chosen out of **__n people__** = nC<sub>2</sub> and this pair can take any of 365 days.  
Now ways of n-2 people have different birthday   = 364 * 363 * ......[364 - (n-2)] / 365^ n-2 = P(364, n-1) / 365^n-2




