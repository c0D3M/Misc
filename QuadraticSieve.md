We will discuss various ways to factorize a given number **N**.

## Difference of Square Method
If this method, we will try to find two numbers **b** and **b**  , whose difference of square is N i.e. <br />
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
301| 318 | NO
302| 921 | NO
303| 1526| NO
398| 68121| Perfect Square(261)

a= 398 b = 261 and a<sup>2</sup> -b<sup>2</sup> = N <br />
So GCD(a+b, N) = 659 and other factor would be 90283/ 659 = 137<br />
659 * 137 = 90283<br />
As you see we did found **b**  but we have to iterate very long.<br />

## Dixon Factorization method

The main idea is instead of looking for **b** which is a perfect square we tried to find multiple **bi**  which has factor to a choose base **B**.<br />
Next combine those **bi** whose **sum of exponent is even** and that will give us our **b**.<br />
Let's explain all this with example.<br />

N = 84923  and we choose factor base of B = {2, 3, 5, 7} , Factor base means while b such that it cna be expressed in this factor base.

lets choose a = 513     b<sup>2</sup> = a<sup>2</sup> mod N = (513) mod 84923 = 8400 = 2<sup>4</sup>  . 3 . 5<sup>2</sup> .7
537 <sup>2</sup> mod 84923 = 33600 =  2<sup>6</sup>  . 3 . 5<sup>2</sup> .7

if we select these two a , exponent of b is even i.e. 
(513 . 537 )<sup>2</sup> mod 84923 = (2<sup>5</sup>  . 3 . 5<sup>2</sup> .7)<sup>2</sup>



