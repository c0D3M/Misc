## Discrete Logarithm Problem
Fix a group G and an element *g* from that group.<br />
Any element *h* from **subgroup of G**<br />
Fin *m* such that *h = g<sup>m</sup>* <br />
 *m= log <sub>g</sub> h*<br />
 Complexity of the solution depends on chosen **group**.<br />
 For some group its easy, example **Z/mZ group under binaryoperation addition** (Z/mZ is the set of integers mod m )<br />
 **Z<sub>p</sub><sup>*</sup> group under multiplication** problem is tough to solve for some large prime and used in DH .<br />
 Some places **Z<sub>p</sub><sup>*</sup>** is also written as **F<sub>p</sub><sup>*</sup>** <br/>
 ### Elliptic Curve Discrete Logarithm Problem
 is the discrete logarithm problem for the group of points on an elliptic curve over a finite field.
 Best known algroithm to solve it is exponential as compared to sub-exponential algorithm for DLP above.
 

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
## RSA
- Take two prime number p and q
- multiply it to get n = pq
- choose any number 1 < e < lcm(p-1, q-1)
- d is modular multiplixative inverse of e mod lcm(p-1, q-1)
- (d,n) is private key and (e, n) is public key
Here the trapdoor function (easy in one way , difficult in other) is factoring of n, multiplication of p and q are easy.


## MAC (Message Authentication Code)
Mac preserves both **authenticity** and **integrity** of message.
Example: HMAC, CBC-MAC
MAC uses same key for generating hash as well as verifying MAC while digital signature doesnt.
HMAC uses cryptographic hash function i.e. MD5/SHA256 etc
CBC-MAC are based on block cipher.
New fasters onces like UMAC & VMAC uses universal hashing.created by know sender

MAC vs SHA256 : Key difference is cryptographic hash function doesnt use any shared key to derive authentication code hence SHA cannot guarantee authenticty of a message.
Both can however guarantee integrity of message.

### Crytographic hash function
Example: MD4, MD5, SHA1, SHA256, SHA512
SHA256(key || message) 
suspectible to length extension attack, i.e. given a H(x) and length of key , Hash of some other message can be calculated.

### Digital Signature
- created by known sender.
- cannot deny having sent/sign that message ( non-repudiation)
- message was not altered.

First we generate hash of input message and using private key and hashed message , we generate the signature.
At receving end , we have hashed-message, public key and signature. Using public key on signature , we receive the value 
and compare the same value with received hashed-message.If they are equal message is OK.

**Encrypt-then-sign**, here the message is first encrypted , hashed and then signed using Digital Signature.
At receiving end , first we verify the signature using Public key and verify the output with encypted message , if its matched we proceed to decrypt the message.


1st and 3rd point are also supported by HMAC.
Example: DSA, ECDSA, RSA <br />


Cryptographic primitive | Hash |    MAC    | Digital
------------------------|------|-----------|-------------
Integrity               |  Yes |    Yes    |   Yes
Authentication          |  No  |    Yes    |   Yes
Non-repudiation         |  No  |    No     |   Yes
Kind of keys            | none | symmetric | asymmetric

DSA vs RSA vs ECDSA

DSA & ECDSA both reply on a random number generator , so if random number generator is poor, private key can be leaked.

## Elliptic Curve Cryptography
high security with short, fast keys and their isn't trapdoor yet.

An ellipctic curve satisfies the equation
y2 = x3 + ax + b
and look something like
![EC](https://blog.cloudflare.com/content/images/image00.png) <br/>
https://blog.cloudflare.com/a-relatively-easy-to-understand-primer-on-elliptic-curve-cryptography/

Explanation:
Curve has intesresting property, take two points on curve and draw a line, it will intersect  at a third place.
Draw a vertical line and the place it hit is new point , again draw a line with this new point and A , where ever it hits draw a line up.
And keep doing that.
So here the trapdoor function is if you are given a point on curve , you dont know how many times the process is repeated unless we redraw the whole process again.
