## Fundamental Theorem of Arithmetic
Any number can be represented in form of prime exponents and this combination is unique  
*n = p<sub>1</sub><sup>k<sub>1</sub></sup>....p<sub>r</sub><sup>k<sub>r</sub></sup>*
## Euler Totient
Count number of positive integer relative prime to it.  
For example  
<a href="https://www.codecogs.com/eqnedit.php?latex=\phi&space;(12)&space;=&space;4" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\phi&space;(12)&space;=&space;4" title="\phi (12) = 4" /></a>
because {1, 5 , 7, 11} are all relative prime to 12 and cardinality of that set is 4.  
Their is a formula to calculate it directly  
<a href="https://www.codecogs.com/eqnedit.php?latex=\phi&space;(n)&space;=&space;n&space;.&space;\prod_{p}^{n}&space;(1-1&space;/p)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\phi&space;(n)&space;=&space;n&space;.&space;\prod_{p}^{n}&space;(1-1&space;/p)" title="\phi (n) = n . \prod_{p}^{n} (1-1 /p)" /></a>
p is prime divisior of n

Example n =12 , its prime divisor are 2 and 3 only   
Eulter totient (12) = 12 . (1-1/2) .(1-1/3) = 4 i.e. {1, 5, 7, 11}   

For __prime number__ its Euler totient will always be p-1, since prime number between 1 to p-1 are all relative prime to p.  

## Fermat's Little Theorem
If __p__ is prime number then for any interger __a__  a<sup>p</sup> - a is an integral multiple of p.  
It cna be re-arragnged an written as  
<a href="https://www.codecogs.com/eqnedit.php?latex=a^{p-1}&space;\equiv&space;1&space;(mod&space;n)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?a^{p-1}&space;\equiv&space;1&space;(mod&space;n)" title="a^{p-1} \equiv 1 (mod n)" /></a>

## Euclid Lemma
If a prime p divided products of two numbers ab, then p must divide atleast one of those integer  

## Euclidean Algorithm
Suppose you have to find GCD of two number 1701, 3768  
- Start with larger of two number  
3768 = 1701 * q + r  
After each step move q -> LHS and r in place of q, do this until we get remainder a 0  
3768 = 1701 * 2+ 366  (1)  
1701 = 366 * 4 + 237  (2)  
366  = 237 * 1 + 129  (3)  
237  = 129 * 1 + 108  (4)  
129  = 108 * 1 + 21   (5)  
108  = 21  * 5 + 3    (6)  
21   = 3 * 7   + 0    <---- So our __GCD(3768, 1701) is 3__

## Extended Euclidean Algorithm
Idea is to represent the GCD in the linear form of the number  
For example  
__3 = 376 * x + 1701 * y__ [where x and y are Integers]  
We can traverse backward  
from 6 we get 3 = 108 - (21 * 5)  
from 5 we know 21 =  129 - (108 * 1)   3 = 108 - [5 * (129 - 108)]           =>  3 = 6 * 108 - 5 * 129  
from 4 we know 108 = 237 - (129 * 1)   3 = 6 * 237 - 6 * 129 - 5 * 129       => 3 =6 * 237 - 11 * 129  
from 3 we know 129 = 366 - (237 * 1)   3 = 6 * 237 - 11 * 366 + 11 * 237     => 3= 17 * 237 - 11 * 366  
from 2 we know 237 = 1701 - (366 * 4)  3 = 17 * 1701 - 68 * 366 - 11 * 366   => 3 = 17 * 1701 - 79 * 366  
from 1 we know 366 = 3768 - (1701 * 2) 3=  17 * 1701 - 79 * 3768 +158 * 1701 => 3 = 175 * 1701 - 79 * 3768  

Hence __3 = 175 * 1701 - 79 * 3768__ GCD is represented in some linear form of inputs.  

## Modular Multiplicative Inverse
Sometime we are given a problem  
a .x  = 1 mod n...(1)  
and we have to find x which is multiplicative inverse of a mod n.  

if __n is prime__ we can use __Fermat's Little Theorem__ to find it quickly

Fermat's Little theorem states  
<a href="https://www.codecogs.com/eqnedit.php?latex=a^{p-1}&space;\equiv&space;1&space;(mod&space;n)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?a^{p-1}&space;\equiv&space;1&space;(mod&space;n)" title="a^{p-1} \equiv 1 (mod n)" /></a>
   Replace 1 mod n from equiuation 1  
<a href="https://www.codecogs.com/eqnedit.php?latex=a^{p-1}&space;\equiv&space;a&space;.&space;x" target="_blank"><img src="https://latex.codecogs.com/gif.latex?a^{p-1}&space;\equiv&space;a&space;.&space;x" title="a^{p-1} \equiv a . x" /></a>  

<a href="https://www.codecogs.com/eqnedit.php?latex=x&space;=&space;a^{p-2}&space;\rightarrow&space;x&space;=a&space;^{(\phi&space;(p)-1)}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x&space;=&space;a^{p-2}&space;\rightarrow&space;x&space;=a&space;^{(\phi&space;(p)-1)}" title="x = a^{p-2} \rightarrow x =a ^{(\phi (p)-1)}" /></a>

If __n is not prime__ we can use __Extended Euclidean Algorithm__ to find it out.  
Example  
11 .x = 1 mod 26  
Since 26 is not prime we will use Extended Eucleadean Algorithm to represent their GCD(11, 26) in some linear form  

26 = 11 * 2 + 4  
11 = 4 *  2 + 3  
4  = 3 * 1  + 1  
3  = 1 * 3  + 0  
Regargging these equation  

1 = 26 * 3 - 7 * 11 this is linear arangement in terms of inputs  
Now do mod 26 , which will divide 26 * 3 completely and no remainder left and we get  
1 mod 26 = -7 * 11 , hence -7 is one such inverse  
In mod -7 mod 26 is same as 19 mod 26 , so **19** is another inverse.

**11 * 19 = 1 mod 26**

## Chinese Remainder Theorem
Smallest number which when divided by x, y, z leaves remainder a, b, c

Example:
Find smallest number when divided by 2, 3, 5 leaves remainder 1, 2, 3  
x = 15x<sub>1</sub> + 10x<sub>2</sub> + 6x<sub>3</sub> [15x<sub>1</sub> comes from the fact that it is not divisible by 2 but by 3,5 that means its a multiple of 3 and 5 i.e. 15]  

lowest 15x<sub>1</sub> when divided by 2 leaves remainder 1 = 1  
lowest 10x<sub>2</sub> when divided by 3 leaves remainder 2 = 2  
lowest 6x<sub>3</sub>  when divided by 5 leaves remainder 3 = 3  

15 + 20 + 18 = 53  
But is this the smallest ? we can find by lcm(2,3,5) = 30  
Since divided by 30 doesnt change the result  
53-30 = 23 , so thats the smalles number satisfying the above condition  

Example  
Find smallest number when divided by 7, 9, 11 leaves remainder 1, 2, 3  

x = 99x<sub>1</sub> + 77x2 + 63x<sub>3</sub>  

lowest 99x<sub>1</sub> when divided by 7 leaves remainder 1 = 1 [ write as multiple of 7 i.e. 98 + 1 / 7]  
lowest 77x<sub>2</sub> when divided by 9 leaves remainder 2 = 4  [ 72 + 5 / 9..that means we have to find multiple of 5 when divided by 9 leaves remainder 2]  
lowest 63x<sub>3</sub> when divided by 11 leaves remainder 3= 10   [55 + 8/11 that means we have to find multiple of 8 when divided by 11 leaves remainder 3 ]  

x = 99 + 77 * 4 + 10 * 63 = 1037  

Again check if this is smallest?  
Find LCM of 7, 9 11 = 693  
1037 - 693 = 344  
__Ans 344__  

## Primality Testing

Often we are given task to find all the prime number ina  given range.  
### Sieve of Erathosthenes
Idea is to start with a given prime and cross all its multiple.  
For example if we have to find all prime between 1 to 100  
start with 2 and cross all its multiple i.e. 4, 6, 8, 10, 12  ......98  
start with 3 and cross all its multiple i.e. 6, 9, 12, 15...........99  
and so on what is left are the prime numbers.

### Segmented Sieve
Main problem of above approach is lot of memory requirement  
- Start with sqrt(n) and use above way to get all prime, for example prime between 1 to 10 are [2, 3, 5, 7]
- Now between each range of sqrt(n) i.e. 11 to 20 all prime found above , find first multple i.e. 12, 14, 16, 18, 20 cross them 
out as they aren't prime, similar for 3 [12, 15, 18] for 5 [15,20], and for 7 is [14], what is left is [11, 13, 17, 19] they are prime.
- Repeat the same step for each of the block [21, 30] , [31, 40]...[91, 100]  

### Miller Rabin Test
