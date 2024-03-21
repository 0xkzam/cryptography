### 1. Modular Arithmetic
- $a, b$ and $n$ are positive integers. If the remainders of $a$ and $b$ when divided by $n$ are equal, then the integers $a$ and $b$ are congruent. It’s denoted as $a ≡ b \pmod{n}$
- Properties
  - Addition
    - If $a ≡ b \pmod{n}$ and $c ≡ d \pmod{n}$, then $a + c ≡ b + d \pmod{n}$	
    - If $a ≡ b \pmod{n}$, then $a + k ≡ b + k \pmod{n}$ for any integer $k$
    - If $a + b = c$, then $a \pmod{n} + b \pmod{n} ≡ c \pmod{n}$
  - Multiplication 
    - If $a.b = c$, then $(a \mod{n}) . (b \mod{n}) ≡ c \pmod{n}$
    - If $a ≡ b \pmod{n}$, then $ka  ≡ kb \pmod{n}$ any integer $k$
    - If $a ≡ b \pmod{n}$ and $c ≡ d \pmod{n}$, then $a * c ≡ b * d \pmod{n}$
  - Exponentiation
    - If $a ≡ b \pmod{n}$, then $a^k ≡ b^k \pmod{n}$ for any positive integer $k$


### 2. Groups
- Definition: 
  - A group consists of a set of elements and an operation. The operation is usually denoted by a dot "**.**"
  - A group should fulfill the following 4 properties.
    - Closure: For all elements $a,b$ in the group, the operation $a.b$ is also in the group.
    - Associativity: For all elements $a,b,c$ in the group, $(a.b).c = a.(b.c)$
    - Identity: There exists one unique identity element $I$ such that $a.I =I.a= a$ for every element $a$ in the group.
    - Invertibility: Every element $a$ in the group, has an inverse $b$ such that $a.b =b.a= I$
  - Abelian groups
    - This is a special type of group that fulfills an additional property called commutativity.
    - Commutativity: For every pair of elements a,b in a group, $a.b=b.a$ 
    - ie. the order of $a$ and $b$ doesn't matter.
  
### 3. Fields
- A field is an Abelian group that fulfills both Addition $(+)$ and Multiplication $(*)$ operations and has the Distributive property.
- I.e., for all elements $a,b,c$ in the field,
  
    ||Additive|Multiplicative|
    |--|--|--|
    |Closure|$a+b∈F$|$a*b ∈F$|
    |Associativity| $(a+b)+c = a+(b+c)$ | $(a * b) * c = a * (b * c)$ |
    |Identity|$I = 0$ |$I=1$|
    |Invertibility|$a+ (-a)=I=0$|$a*a^{-1}=I=1$|
    |Commutativity|$a+b = b+a$| $a * b=b * a$ |
- Distributive property: For all elements $a,b,c$ in the field, $a*(b+c)=(a * b)+(a * c)$ holds.
