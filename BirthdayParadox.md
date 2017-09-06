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

**P_N(0) = P(365, n) / 365^n**  

2. 1 pair of people share a birthday and then n-2 people have different birthday.  

Number of ways 1 pair of people can be chosen out of **__n people__** = nC<sub>2</sub> and this pair can take any of 365 days, Probability = 365/ 365^2   
Now ways of n-2 people have different birthday   = 364 * 363 * ......[364 - (n-2)] / 365^ n-2 = P(365-1, n-2) / 365^n-2  

**P_N(1) = 365 * nC<sub>2</sub> * P(365-1, n-2) / 365^n**  

3. 2 pair of people share a birthday and then n-4 people have different birhday.  

- Number of ways 1st pair can be chosen  = nC<sub>2</sub>
- Number of ways 2nd pair can be chosen  
    We have now n-2 people, hence n-2C<sub>2</sub>  
- Number of ways 2 birthday can be chosen for above 2 pairs would be 365C<sub>2</sub>  
- Now we have n-4 people left = 363, 362, .....365-(n-4) = P(365-2, N-4)  
**P_N(2) = nC<sub>2</sub> * n-2C<sub>2</sub> * 365C<sub>2</sub> * P(365-2, n-4)**  


Generalizing for all the maximum 2 pair possible which is n/2  
This is for all the 'k' pairs nC<sub>2</sub> * n-2C<sub>2</sub> * (n-2k+1)C<sub>2</sub>  
Now for choosing 'k' birthdays for above k pairs = 365C<sub>k</sub>  
Next the left overs can choose 365-k birthdays = P(365-k, N-2k) ways  

Multiplying all of the above and cancelling denominator to numerator  

**P_N(K) = C(365,K) * P(N,2K) * P(365-K,N-2K)/((2!)^K * 365^N)**    

So essentially we have to sum up P_N(K) from K=0 to n/2(Case #2 to Case #1+n/2)  
Case # 1 i.e. P_N(0) can also be obtained by putting k=0 in this equation.  

<a href="https://www.codecogs.com/eqnedit.php?latex=\sum_{i=0}^{n/2}&space;C(365,i)&space;*&space;P(N,2i)&space;*&space;P(365-i,N-2i)/((2!)^i&space;*&space;365^N)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\sum_{i=0}^{n/2}&space;C(365,i)&space;*&space;P(N,2i)&space;*&space;P(365-i,N-2i)/((2!)^i&space;*&space;365^N)" title="\sum_{i=0}^{n/2} C(365,i) * P(N,2i) * P(365-i,N-2i)/((2!)^i * 365^N)" /></a>  

This can be further simplified as, advantage is we get rid of Combinatorial and we get rid of denominator.  

<a href="https://www.codecogs.com/eqnedit.php?latex=\sum_{i=0}^{n/2}&space;P(N,2i)&space;*&space;P(365,N-i)/((2!)^i&space;*&space;365^N&space;*&space;i!)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\sum_{i=0}^{n/2}&space;P(N,2i)&space;*&space;P(365,N-i)/((2!)^i&space;*&space;365^N&space;*&space;i!)" title="\sum_{i=0}^{n/2} P(N,2i) * P(365,N-i)/((2!)^i * 365^N * i!)" /></a>  

## Birthday Problem Generalization

Here we will try to generalize the problem i.e.  __*M*__  can share same birthday.  
So we start with first gorup of 2 people, 3 people ... and upto M-1 people.  
Why 2, because we are calculating  *P(no_collission)* and then subrract from 1 which give *P(collission)*
and to have *no collssion*, grouping of people has to start with 2 or more is necessary.    
Why __M-1__: because we are calcuating no collision, if we take all M people there will be collision, hence M-1.  
So for each group size we have to evaluate all possible grouping.  

P(no_collission) = <a href="https://www.codecogs.com/eqnedit.php?latex=\sum_{k=2}^{M-1}&space;\sum_{i=0}^{n/k}&space;P(N,ki)&space;*&space;P(365,N-i)/((k!)^i&space;*&space;365^N&space;*&space;i!)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\sum_{k=2}^{M-1}&space;\sum_{i=0}^{n/k}&space;P(N,ki)&space;*&space;P(365,N-i)/((k!)^i&space;*&space;365^N&space;*&space;i!)" title="\sum_{k=2}^{M-1} \sum_{i=0}^{n/k} P(N,ki) * P(365,N-i)/((k!)^i * 365^N * i!)" /></a>    

