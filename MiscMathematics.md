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

x = 99 + 77*4 + 10*63 = 1037  

Again check if this is smallest?  
Find LCM of 7, 9 11 = 693  
1037 - 693 = 344  
Ans 344  

