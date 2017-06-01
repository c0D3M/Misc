## Discrete Logarithm Problem
Fix a group G and a generator element *g* from that group.<br />
Any element *h* from **subgroup of G**<br />
Fin *m* such that *h = g<sup>m</sup>* <br />
 *m= log <sub>g</sub> h*<br /> [This is continiuos log]
 Complexity of the solution depends on chosen **group**.<br />
 For some group its easy, example **Z/mZ group under binary operation addition** (Z/mZ is the set of integers mod m )<br />
 **Z<sub>p</sub><sup>*</sup> group under multiplication** problem is tough to solve for some large prime and used in DH .<br />
 Some places **Z<sub>p</sub><sup>*</sup>** is also written as **F<sub>p</sub><sup>*</sup>** <br/>

## Primitive root modulo n
3 is a primitive root of 7 , meaning when raised to any power between [1,6] mod 7 , result is some order of [1,6].<br />
The powers of 3, reduced modulo 7, are 3, 2, 6, 4, 5, 1, so we does get everything between [1,6] <br />

Note that after g<sup>p-1</sup> the power starts all over <br />
Fermat's little theorem  g<sup>p-1</sup> ≡ 1 mod p , g<sup>p</sup> = g<sup>p-1</sup> . g<sup>1</sup> <br />

a is called __discrete logarithm__ of of A with respect to __primitive root__ g and computing for __a__ is comoutationally harder.<br />
However given g,a,p one can find __A__. See [link](https://en.wikipedia.org/wiki/Modular_exponentiation) <br />

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


## RSA
- Take two prime number p and q
- multiply it to get n = pq
- choose any number 1 < e < lcm(p-1, q-1)
- d is modular multiplixative inverse of e mod lcm(p-1, q-1)
- (d,n) is private key and (e, n) is public key
Here the trapdoor function (easy in one way , difficult in other) is factoring of n, multiplication of p and q are easy.

## Perfect Forward Secrecy
Its a feature where if private key is comprmised, sesson keys (symemtric keys for encryption and HMAC) will not be compromised.  
A unique session key is generated every time user initated a session.  
As we know in TLS session Pre-Master Secret is encrypted with server public key and which is later on used to generate Master Secret  
If private key is compromised, this session key wil be exposed.  
So we will use such cipher suite during key-exchange which is ephemeral, like DH.
Remember that in DH , our session key was **g<sup>a</sup><sup>b</sup>**
In DH, everytime client chose a different random secret a.
Choosing g and a is a fast operation as opposed to RSA , where if every time we have to generate new pair of keys we have to start with p and q prime number and generating prime number is not an easy operation.  

### Digital Signature
- created by known sender.
- cannot deny having sent/sign that message ( non-repudiation)
- message was not altered.

Every digital signature requires a public-private key pair and a hash function.   
First we generate hash of input message, Then using private key and hashed message , we generate the signature.
At receving end , we have message, public key and signature. Using public key on signature , we retrieved the hashed value by decrypting, and compare the same value with hashed-message(incoming message hashed).If its a match signature is valid.  

**Sign-then-encrypt** seems to be general approach which is diameterically opposite for MAC  
In PKI, a certificate authority , hash the certificate and then encrypt using its **private key**  
Certificate contains all details in plain text (X.509) and also it contained encrypted digital signature  
On client side, plain text is first hashed using SHA-1/2  
ecnrypted digital signature is decrypted using **certificate authroty public key**  and the result is match against hash  

In MAC our aim was to check for authenicty and integrity for **data**  
While in Signature our aim is to verify authenicty, integrity as well as non-repudiation for **entity**  
https://crypto.stackexchange.com/questions/5458/should-we-sign-then-encrypt-or-encrypt-then-sign
http://commandlinefanatic.com/cgi-bin/showarticle.cgi?article=art012

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

## MAC (Message Authentication Code)
Mac preserves both **authenticity** and **integrity** of message.
Example: HMAC, CBC-MAC
MAC uses same key for generating hash as well as verifying MAC while digital signature doesnt.
HMAC uses cryptographic hash function i.e. MD5/SHA256 etc
CBC-MAC are based on block cipher.
New fasters onces like UMAC & VMAC uses universal hashing.created by know sender

MAC vs SHA256 : Key difference is cryptographic hash function doesnt use any shared key to derive authentication code hence SHA cannot guarantee authenticty of a message.
Both can however guarantee integrity of message.  

### Encrypt-then-MAC
First we encrypt the plaintext using session keys and then compute the MAC of cipher text.  
So we are sending (CipherText, MAC_Cipher)  
On receiver side, we compute MAC of Cipher text and if both matches, message is authentic and we proceed to decrypt the message.  

### MAC-then-Encrypt
We compute MAC of plain text and encrypt plain_text + MAC using session key.  
ON receciver side  
- Use session key we decypt the message first
- Then we compute MAC of plain text and verifies with incoming MAC.
https://eprint.iacr.org/2014/206.pdf

### Encrypt-and MAC
Here we first compute MAC of plain text and then ecrypt plain text. So we are sending (Cipher Text, MAC_Plain)
On receiver side
- First decypt the cipher text   
- Compute MAC using decrypted text and MAC key and match.  
https://crypto.stackexchange.com/questions/202/should-we-mac-then-encrypt-or-encrypt-then-mac  
https://crypto.stackexchange.com/questions/15485/why-do-we-encrypt-then-mac-but-sign-then-encrypt  
Encrypt-then-MAC is best of all three approach since we ahave already exchange sessions & MAC keys and we will first compute  
MAC using exchanged MAC keys and if they mismatch we wont decrypt at all  

## Block Ciphers
### ECB Mode
PT is divided in block and XOR with key 

### CBC mode
PT is divided in block 
PT<sub>i</sub> = PT<sub>i</sub> XOR CT<sub>i-1</sub>

### Counter Mode 
Counter || IV is encrypted and then XORed with PT block

### GCM Mode
Provides AEAD , after encryption the CT is multiplied with Galios Filed Polynomial number 

## AEAD -. Authentcated, Encrypted, Additional Data. 
They do encryption and authentication (HMAC) all in one go using a single key, rather than relying on HMAC key.  
Part of it is plain text ,part of it is encrypted but everything is authenticated.  
AES-GCM is one such AEAD cipher.  
TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256 is  cipher suite   
Since in GCM mode no separate HMAC construction is required , SHA256 is used for other functions like digital signature.  
https://crypto.stackexchange.com/questions/26410/whats-the-gcm-sha-256-of-a-tls-protocol  
ChaCha is a stream cipher and faster than AES (software only) , a variant of Salsa  
Poly1305 is MAC algorithm.  

### Crytographic hash function
Example: MD4, MD5, SHA1, SHA256, SHA512
SHA256(key || message) 
suspectible to length extension attack, i.e. given a H(x) and length of key , Hash of some other message can be calculated.  
https://blog.cloudflare.com/why-its-harder-to-forge-a-sha-1-certificate-than-it-is-to-find-a-sha-1-collision/  
http://www.win.tue.nl/hashclash/rogue-ca/  

## Elliptic Curve Cryptography
high security with short, fast keys and their isn't trapdoor yet.

An ellipctic curve satisfies the equation
y2 = x3 + ax + b
and look something like
![EC](https://blog.cloudflare.com/content/images/image00.png) <br/>
https://blog.cloudflare.com/a-relatively-easy-to-understand-primer-on-elliptic-curve-cryptography/
This also form a group and group laws (closure, inverse, identity, associativity and commutative) are defined **geometrically**  

Explanation:
Curve has intesresting property, take two points A, B on curve and draw a line, it will intersect  at a third place.
Draw a vertical line and the place it hit is new point, this new point is A+B.  

Adding a point to itself is tangent from that point and using similar process above will give A+A = 2A  
-A will be on symetrically opposite to A over x-axis  
Note that A+ (-A) should be dfined by this line intersecting at a third point but their is no such intersection !  
Lets calls this O.  
 Abelian group axiom can be proved using this  

And keep doing that.
So here the trapdoor function is if you are given a point on curve , you dont know how many times the process is repeated unless we redraw the whole process again.

 ### Elliptic Curve Discrete Logarithm Problem
 is the discrete logarithm problem for the group of points on an elliptic curve over a finite field.  
 Best known algroithm to solve it is exponential as compared to sub-exponential algorithm for DLP above.  
 http://www.math.brown.edu/~jhs/Presentations/WyomingEllipticCurve.pdf  
 https://blog.cloudflare.com/ecdsa-the-digital-signature-algorithm-of-a-better-internet/

## ECDHE
Smaller, faster keys and same level of secrecy as achived by 2048+ keys for DH/RSA.  
_G_ is an initial point on Curve, server chose an random number _a_ and compute a .G , a.G will be apoint lies on curve but finding a from G and a.G is Elliptic curve Disceret Logarithm problem  

Client also chose a random b and compute b.G and send to server.
Server now has a.b.G and client has b.a.G
https://crypto.stackexchange.com/questions/5896/does-the-elliptic-curve-ec-cryptosystem-outperform-rsa-and-dl-cryptosystems/5897#5897
https://security.stackexchange.com/questions/14731/what-is-ecdhe-rsa

### Miscellaneous Topics

### nonce
https://security.stackexchange.com/questions/3001/what-is-the-use-of-a-client-nonce

### salt
Additional data to hash passsword and used to protect against dictionary attack, for an attacker to determine password he has to 
compute hash for all dictionary with salt and it slows down.
On the system Hash(salt||password) is saved and salt is saved in plain text, when a user logged we again calculate Hash using
input string and salt and if both hash matches , password is correct.

### entropy

### maleability
A ciphertext is changed such that when decrypted it produced a different plaintext.  
See example of malleable on wiki https://en.wikipedia.org/wiki/Malleability_(cryptography)  


## ElGamal

### Cryptographic Usage

## How TOR Works
TOR is a network to provide anonymity.  
TOR connected to directory servers, these are trusted node and used to build a circuit.  
Suppose source node wants to communicate to destination node over a TOR network
First it select an entry node and create a TLS tunnel and create session keys.  
Next it create a tls tunnel between a middle node and our node by using entry node.  
Next it select and exit node and again create a tls tunnel between source node and exit node.  

Now when a message have to sent to desitination node, first we encrypt with exit node session key.

Here msg is IP packet we wanted to send to destination node  
TOR Msg = SK1(SK2(SK3(msg))) here entry node will unwrap using SK1 and forward, middle node will unwrap using SK2 and then 
exit node unwrap using SK3 and finally send the msg to destination node.  
Generally all TOR nodes are listed and an ISP cna found if you are using TOR or not but 
TOR bridge are unlisted node and can be used for entry node.

## How SSL works
https://stribika.github.io/2015/01/04/secure-secure-shell.html

## Bit coin:
https://chrispacia.wordpress.com/2013/09/02/bitcoin-mining-explained-like-youre-five-part-2-mechanics/
http://www.coindesk.com/information/what-is-bitcoin/

## Whatsapp Security
https://www.whatsapp.com/security/WhatsApp-Security-Whitepaper.pdf  
