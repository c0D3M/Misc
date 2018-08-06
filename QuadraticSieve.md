We will discuss various ways to factorize a given number **N**.

## Congurence
*a* & *b* are said congurenet modulo *n* , when a and b have same remainder when divided by n.    
![](https://wikimedia.org/api/rest_v1/media/math/render/svg/fbb66ad4d03232b185b3dd6a6ee293943f21f786)  
Example a= 37 , b = 57 n =10  
![](https://wikimedia.org/api/rest_v1/media/math/render/svg/2597d68becb3448bb118defd783d20f82d182aee)  
Alternatively, *a*-*b* is dibisible by *n*

## Congurence of Square Method
If this method, we will try to find two numbers **a** and **b**  , whose difference of square is N i.e. <br />
**a<sup>2</sup>** - **b<sup>2</sup>** = **N**

This idea works because<br />
a<sup>2</sup> - b<sup>2</sup> = N<br />
(a+b)(a-b) = N<br />

Thus a+b and a-b divides N and if we take GCD(a+b, N) and the other factor can be found by dividing by N.<br />
Lets see this by an example **N = 8051** <br />
start with a whose square is closest to 8051 , we can easily se it is 90 as,  90<sup>2</sup> = 8100 , which is close to N <br />
by tial and error , b = 7 as 8100 - 49 = 8051<br />
Hence **a= 90 b = 7** as 90<sup>2</sup> - 7<sup>2</sup> = 8051<br />
GCD(a+b, N) = GCD (97, 8051) = 97 , other factor would be 8051 / 97 = 83<br />

So the factors of 8051 are 97 and 83.<br />

Although this is a great method to find factor, it can be very slow in certain case,<br />
For example  N = 90283<br />
Starting a= 301 , we keep looking whether a<sup>2</sup> - N is a perfect square or not and our search ends at a = 398 !<br />

a | a<sup>2</sup> - N| b
------|-------|--------
301| 318 | no
302| 921 | no
303| 1526| no
398| 68121| Perfect Square(261)

a= 398 b = 261 and a<sup>2</sup> -b<sup>2</sup> = N <br />
So GCD(a+b, N) = 659 and other factor would be 90283/ 659 = 137<br />
659 * 137 = 90283<br />
As you see we did found **b**  but we have to iterate very long.<br />

## Observation
Is 6 a perfect square ? No    
Is 54 a perfect square? No  
As per fundamental theorem of artithemic  
6 = 2<sup>1</sup> * 3<sup>1</sup>  
54 = 2<sup>1</sup> * 3<sup>3</sup>  
6 * 54 is perfect square? Yes i.e. 18<sup>2</sup> = 6 * 54  
A key observation is exponents of 6 and 54 when multipled together become perfect sqaure i.e. multiple of 2  
6 * 54 = 2<sup>2</sup> * 3 <sup>4</sup>  
We will use this aspect in next section  

## Dixon Factorization method

Let's try to factorize 
N = 84923 
As per difference of square method, we have to start with √N i.e. 292 and keep counting up until a<sup>2</sup> -N is perfect square  
Our search ends at a = 505 !  b = 16 i.e. 505<sup>2</sup> - 85923 = 16<sup>2</sup>  
GCD(505-16, 85923) = 163, other factor would be 521  

The main idea is instead of looking for **b** which is a perfect square we tried to find multiple **bi**  which has factor to a choose base **B**.  
Next combine those **bi** whose **sum of exponent is even** and that will give us our **b**.<br />
Let's explain all this with example.  

N = 84923  and we choose factor base of B = {2, 3, 5, 7} , Factor base means while b such that it can be expressed in this factor base.

lets choose a = 513     b<sup>2</sup> = a<sup>2</sup> mod N = (513) mod 84923 = 8400 = 2<sup>4</sup>  . 3 . 5<sup>2</sup> .7
537 <sup>2</sup> mod 84923 = 33600 =  2<sup>6</sup>  . 3 . 5<sup>2</sup> .7

if we select these **two** a , exponent of **b is even** i.e. 
(513 . 537 )<sup>2</sup> mod 84923 = (2<sup>5</sup>  . 3 . 5<sup>2</sup> .7)<sup>2</sup>

One simplication can we done i.e. 513.537 can we written as 84923 * 3 + 20712, so instead of using 513.537 , which is a very big number, we can use 20712 since 84923 is anyway dividing 513.537.  
And then we can use gcd way of calculating factors  

## Quadratic Sieve  

In Dixon method, we have to keep looking for a's for which b's exponent can be perfect square  
Next we try to  create  these  **a**  number, but before that  

### Quadratic residue
q is said to be quadratic residue , if it congurent to perfect square modulo n  
*x<sup>2</sup>* ≡  *q*  mod *p*  

For p =2, every integer is quadratic residue, because either it will divisible or will have remainder 1  
For exampple 7<sup>2</sup> ≡ 1 mod 2  

For p =5 , quadratic residues are **1**, 2, 3, **4** (residue in **bold**)  

If p is prime , there will be **(p-1)/2** quadratic residues  
p = 5  

1<sup>2</sup> ≡ 1 mod 5  
2<sup>2</sup> ≡ 4 mod 5  
3<sup>2</sup> ≡ 4 mod 5  
4<sup>2</sup> ≡ 1 mod 5  

### Euler Criteria
For a given *a* and odd prime *p*, then  
![](https://wikimedia.org/api/rest_v1/media/math/render/svg/f91057ce9d4d7a48280406d44f52d6417950b43f)  

Example p =5  
For a = 1 ; 1 <sup> 5-1/2</sup> ≡ 1 mod  5=> ≡  1 mod 5, then a=1 is quadratic **residue**.  
For a = 2 ; 2 <sup> 5-1/2</sup> ≡ 4 mod  5=> ≡ -1 mod 5, then a=2 is quadratic **non-residue**.  
For a = 3 ; 3 <sup> 5-1/2</sup> ≡ 4 mod  5=> ≡ -1 mod 5, then a=3 is quadratic **non-residue**.  
For a = 4 ; 4 <sup> 5-1/2</sup> ≡ 16 mod 5=> ≡  1 mod 5, then a=4 is quadratic **residue**.  

We can answer following question on quadratic residue
#### 1. Find the quadratic resdue for a given number *p* , this is easy just interate 1 to p and calculate  
Example, p = 17  
1<sup>2</sup> mod 17 = 1  
2<sup>2</sup> mod 17 = 4  
3<sup>2</sup> mod 17 = 9  
4<sup>2</sup> mod 17 = 16  
5<sup>2</sup> mod 17 = 8  
6<sup>2</sup> mod 17 = 2  
7<sup>2</sup> mod 17 = 15  
8<sup>2</sup> mod 17 = 13  
9<sup>2</sup> mod 17 = 13  
10<sup>2</sup> mod 17 = 15   

No need to calculate from 9 onward, why because 9<sup>2</sup> ≡ (-8)<sup>2</sup> mod 17 , so whatever value 8 takes return same is true for 9 also.  
So quadratic residue of 17 are **{1,2,4,8,9,13,15,16}**  

TODO: Law of Quadratic Reciprocity.  
#### 2. For a given *a* if this is quadratic residue of prime *p*  

a = 3, p = 17  
Apply Euler criteria
3 <sup> (17-1)/2 </sup>  = 16 mod 17 = -1 mod 17 , and hence 3 is **not a quadratic residue**  

#### 3. Finding primes for a given quadratic residue

 q = 15 p=? 
 Apply Euler criteria
 
 Lets put p =17 and see if q=15 is quadratic residue ?  
 15<sup> (17-1)/2</sup>  = 15<sup>8</sup> mod 17 = 1 , hence 15 is quadratic residue  
 
Back to our original problem, as we have seen in Dixon method, we keep **searching** for multiple a's and select some of them for which b's exponent vector is mod 2. This is still a problem, next we will see how to **create** these a's effectuvely and then solve their exponent vector to get the b.  


## Reference
1. https://blogs.msdn.microsoft.com/devdev/2006/06/19/factoring-large-numbers-with-quadratic-sieve/
2. https://www.youtube.com/watch?v=Y3N0vZoPCWE
3. http://thales.doa.fmph.uniba.sk/macaj/skola/teoriapoli/primes.pdf
4. https://www.ams.org/notices/199612/pomerance.pdf

