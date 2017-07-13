## Set
Collection of weel defined disctinct object.<br />
Example:<br />
_**N**_ set of **Natural numbers** = **{1, 2, 3, 4, ..}** , Some places 0 is also included, that set is Whole Number.<br />
_**Z**_ set of **Integers** = **{.....,-2, -1, 0, 1, 2, 3...}**<br />
_**Q**_ set of **Rational Nmbers** , which can be expressed in p/q form, while Irrational number are those which cannot like **√2**<br />
_**R**_ set of **Real Numbers** includes integers, rational and irational numbers.

## Group

### Binary opreation
Any operation when performed on member of set to get another member is binary operation.<br />
For example + is a binary operation for set of Integer , if we take 2 and 3 and apply + operation we get 5 , which is also a member of I.<br />

### Algebraic structure : 
A set which obey one or more axioms (Closure, Associative, etc). _Ring_, __Group_, _Field_ etc.<br />
### Group: 
Any set which satisfies axioms 1-4 on some binary operation is called group.<br />

1. Closure property: Take any two elements from set and perform binary operation, result should also be in same set , like + on Integer.<br />
2. Associative property: a+b = b+c , this is true for (I,+)
3. Identitiy Element: there exists an element in _**e**_ such that a + e = a , in case of I this will be 0 and 0 exists in I.
4. Inverse , there exists an element in set suhc that a + a<sup>-1</sup> = e (Identiy element) , in set I if we take 2 , its invers would be -2 since
2 + (-2) = 0

Similary we can show that set of real number R is group under binary opreation *. _**(R, \*)**_
### Abelian Group:
If beside above axioms , group satisfies commutative law also , it is called Abelion Group.<br />
a + (b+c) = (a+b) + c <br />
Set of Integer satisfies this propery under + , so **(I, +)** is an **Abelion Group**
### Cyclic Group
Using atleast one elemnt of group we can geerate all other element of group.<br />
For example Set of integer modulo 5 = **{0, 1, 2, 3, 4}** is a cyclic group  and its generator are any element relative prime to 5 i.e. 1,2,3,4.<br />

### Order of a group
Cardinality of a group i.e. number of elements.<br />
Order of element is i.e. number of time binary operation is performed to get identity element.<br />
For example Group of Intger under Addiona modulo 4 = {0, 1, 2 , 3}<br />
Order(1) = 1+1+1+1 mod 4 = 4<br />
Order (2) = 2+2 mod 4 = 2<br />
Order (3) = 3+3+3+3 = 4<br />
Order (4) = 4+4+4 = 3<br />

### sub group
If G is group , H is a subset of its element also obeying group property under binary operation.<br />
H is closed under operation on G (closure property) a,b belongs to H then ab also belongs to H<br />
H contains indetitiy element <br />
H is closed under inverse i.e. a belongs to H then a<sup>-1</sup> belongs to H<br />
ab<sup>-1</sup> also belongs to H.<br />

### Normal sub group
H is subrgoup of G<br />
and for all h , and for x belong to Group<br />
xhx<sup>-1</sup> belongs to H as<br />
H is normal subrgoup<br />
Example: Subgroup of abelian group is normal subgroup, like (I, +)<br />

### Coset
G is a group and H is a subgroup <br />
Then g belongs G <br />
gH is left coset and Hg is right coset <br />

if H is normal subgroup , left and right coset conincide.

### Homomorphism
(G, o)>  (G', o')  [o/o' are some opreations]<br />
F: G -> G'<br />
f(a o b) = f(a) o' f(b) [o and o' can be same) f(x * y) = f(x) * f(y)<br />

### Kernel of Homomorphism
k(f) contains all elelennts of G such that their f mapping results e' (indentity elements of G').<br />
Example:
 Let (I, +) and another G{1, -1, i, -i}  foruth root of unity <br/>
 f: I -> G  by f(n) = i<sup>n</sup> is homomorphic<br/>
 f(x+y) = i<sup> x+y</sup> = i<sup> x </sup> i<sup>y</sup> = f(x) . f(y) <br/>
 
 Kernel of f such that f(x) = 1 (which is identity elelment of G}<br/>
 all multiple of 4 will form this group because i<sup>4</sup> = 1<br/>
 
 hence k(f) = {0, +-4, +- 8, +- 12....} = **4Z** <br/>
 
### Isomorphism
(G, o) and (G, o') be group and f: G->G' mapping
1. f should be one to one mapping 
2. f is onto mapping i.e. no elelmenbt in G' is not left without mapping from G.
3. f is homomorphism i.e.<br />
   f(a o b) = f(a) o' f(b)<br />
Note that 1 & 2 together called bijective  

Example:<br />
G= (I, +)<br />
G= (2Z, +) group of even number<br />
f(x) =2x for x belongs to G<br />
Prove that f(x) is isomorphism<br />

1. All number in G will have a 2x maping in G'
2. Any even number will have corresponding element in G such that 2x is even.
3. take 2 elements x1, x2<br />

f(x1+x2) =2(x1+x2) = 2x1 + 2x2 = f(x1) + f(x2) hence f is homomorphism<br />

### Quotient Group

Take a group G under multiplication and a normal sub-group H.
for all a belongs to G , it can be shown shown that 

{a<sub>1</sub>H, a<sub>2</sub>H ....} is also a group , note that {a<sub>1</sub>H} is a set itself

## Ring
A Ring in an abelian group with second binary operation that is<br />
- Associativity 
- Distributive over alebian group operation
- Has Identity element
Example , Group of Integer , abelian group operation is addition and second operation is multiplication
**(I, +, .)**<br />
We knew that **(I, +)** is abelian group.<br />
- . is associative for Integers i.e. a.(b.c) = (a.b).c
- a.(b+c) = (ab) + (bc)
- has identity element 1 such that a.1 = a
This ring is also **commutative ring** since a.b = b .a<br />
Example of non-commutative ring can be ring of square matrices.<br />

### Ideal
an idela is a subset of ring such that following property are satisfied
a + b belongs to I , where a and b belongs to I
r . x = I , r belongs to R and x belongs to I
Example: subset of even integer is a ideal, because above property holds true.

### Quotient Ring
Let I be an ideal of ring R , then we cna definie
(a+I ) + (b+I) = (a+b)+ I  [ and b belongs to R)
(a+I) . (b+I) = (ab) +I (since a.I =I and b.I =I)
R/I is called quotient ring or reside class or equivalence class or set of coset. <br/>

## Field
A field is a ring which also contain additional property of **multiplicative inverse**.<br />
Set of Real number is a field (it is also an abelian group and ring).<br />
For example if we take **4/3** their exist and inverse which is **3/4**.<br />

Complex number **a+bi** also form a field.<br />
Addition and multiplication can be done in such a way that all group and ring axiom holds true.<br />
Multiplicative inverse of a+bi = a/(a<sup>2</sup> + b<sup>2</sup>) - bi / (a<sup>2</sup> + b<sup>2</sup>)<br />


## Reference
http://www.di-mgt.com.au/multiplicative-group-mod-p.html
