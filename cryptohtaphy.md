## Diffie-Hellman 
A method to securely exchange cyptographic keys over a public network.

_g_ and _p_ are public values. g is **primitive root modulo** of p.

Alice Choose secret _a_ and send _g<sup>a</sup> mod p_**(A)**  to Bob.<br />
Bob choose secrte _b_ and send _g<sup>b</sup> mod p_**(B)** and send to Alice.<br />

On receiving result, both side calculate<br />
_**(g<sup>b</sup> mod p)<sup>a</sup> = g<sup> ba </sup> mod p**_<br />
_**(g<sup>a</sup> mod p)<sup>b</sup> = g<sup> ab </sup> mod p**_<br />
Notice that in arithmetic (g<sup>a</sup>)<sup>b</sup> is same as  (g<sup>b</sup>)<sup>a</sup>.
__Ordering__ doesnt change result.

An eavesdropper to find **a** has to solve <br />
__g<sup>a</sup> = A (mod p)__
This problem is known as  [discrete lograthimic problem](https://en.wikipedia.org/wiki/Discrete_logarithm)

## Primitive root modulo n
3 is a primitive root of 7 , meaning when raised to any power between [1,7] mod 7 , result is rearrangemnet of remainder modulo 7

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

