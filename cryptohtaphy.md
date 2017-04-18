## Diffie-Hellman 
A method to securely exchange cyptographic keys over a public network.

_g_ and _p_ are public values. g is **primitive root modulo** of p.

Alice Choose secret _a_ and send _g<sup>a</sup> mod p_**(A)**  to Bob.<br />
Bob choose secrte _b_ and send _g<sup>b</sup> mod p_**(B)** and send to Alice.<br />

On receiving result, both side calculate<br />
_**(g<sup>b</sup> mod p)<sup>a</sup> ≡ g<sup> ba </sup> mod p**_<br />
_**(g<sup>a</sup> mod p)<sup>b</sup> ≡ g<sup> ab </sup> mod p**_<br />
Notice that in arithmetic (g<sup>a</sup>)<sup>b</sup> is same as  (g<sup>b</sup>)<sup>a</sup>.
__Ordering__ doesnt change result.

An eavesdropper to find **a** has to solve <br />
__g<sup>a</sup> ≡ A (mod p)__
This problem is known as  [discrete lograthimic problem](https://en.wikipedia.org/wiki/Discrete_logarithm)<br />

## Primitive root modulo n
3 is a primitive root of 7 , meaning when raised to any power between [1,6] mod 7 , result is some order of [1,6].<br />
The powers of 3, reduced modulo 7, are 3, 2, 6, 4, 5, 1, so we does get everything between [1,6] <br />

Note that after g<sup>p-1</sup> the power starts all over <br />
Fermat's little theorem  g<sup>p-1</sup> ≡ 1 mod p , g<sup>p</sup> = g<sup>p-1</sup> . g<sup>1</sup> <br />

a is called __discrete logarithm__ of of A with respect to __primitive root__ g and computing for __a__ is comoutationally harder.<br />
However given g,a,p one can find __A__. See [link](https://en.wikipedia.org/wiki/Modular_exponentiation) <br />


TODO:
- Pohlig Hellman
- index calculus
- DHE
- EC-DH
- Chinese Remainder Theorem<br />
X divide by 3 yield 2 as remainder.
X divide by 5 yield 3 as remainder.
X divide by 7 yield 2 as remainder.
What is X ? 

