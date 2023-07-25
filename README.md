# primeGapper
Explores gaps between primes
The gaps between primes seems to follow a continuously changing pattern and this repo is to explore that pattern. The exact details of that pattern are not that complex and is demonstrated with examples.    

## Preamble
Candidate Primes after a prime p are numbers that are not divisible by any prime <= p
Ex: p=2 => candidate primes are 3,5,7,9..; p=3 => 5,7,11,13,17,19,23..

## Hypothesis
The hypothesis is that the gap between Candidate Primes follow a pattern:  
cp(p) = p+a+(c,d,e,f..)\* (*=the pattern enclosed in brackets repeats).  
g(p) = cp - p = a+(c,d,e,f..)\* where g(p) is the gap between primes
Ex: g(2) = 1+(2)* = 1,2,2,..=> cp(2) = 3,5,7,9..

<b>Observations</b>  
1.  cp(p1) is a subset of cp(p) for p1 > p (i.e. cp(p) = numbers not divisible by primes upto p, and cp(p1) = number not divisible by primes upto P AND number not divisible by primes upto P1)  


## Examples:
Taking the first prime as 2: The prime gap function is g(2) = {1,(2)\*} . The (2)\* is a continuing sequence of 2's and is the repeating part. The repeating part adds up to 2.  

Using this pattern the next primes are: 2+1 = 3, 3+2 = 5, 5+2 = 7, ..9, 11, 13 ...  
Here '9' is not a prime, and so we have to create a new pattern by including the number 3 as a prime..
Taking 2 and 3 as primes: g(3) = {2,(2,4)\*} => 5,7,11,13,17,19,23...  

### Important discovery:  
The repeating portion of the pattern adds up to 'prime factorial'.  For example:  
pf(2) = all primes 2 and below multiplied = 2 => pattern is {1,(2)\*} and the repeating portion adds to 2  
pf(3) = all primes 3 and below multiplied = 2x3 = 6 => pattern is {2,(2,4)\*} and the repeating portion adds to 2+4=6  
pf(5) = all primes 5 and below multiplied = 2x3x5 = 30 => pattern is {2,(4,2,4,2,4,6,2,6)\*} and the repeating portion adds to  
4+2+4+2+4+6+2+6 = 30.

## ModVattam Theorem (or ModCircle theorem):
 (x+n*pf) mod p1 traverses all the numbers 0..p1-1 as n goes from 0..p1-1
 Example: g(3) = {2,(2,4)\*}.  Here take :  
 p1 as the next prime = 5,  
 pf= sum of repeating part = 6
 x = p1  
 Then (5+n*6) mod 5 = {0,1,2,3,4} for n=0,1,2,3,4. In this case the result is orderly.  
 Another case:
 p1=7, x=5, pf=6
 Then (7+n*6) mod 5 = {2,3,4,0,1}  for n=0,1,2,3,4. In this case the result is not orderly but traverses 0..4


## On To The Program
The primeGapper process described about is related to the 'Eratothesnes Sieve'.  
The program finds the patterns starting from 1 (special prime, that does not divide anything) and continues with the next prime and so on.  
It is in Python using normal python integers and works upto about 800.  The failure after that is probably due to number overflow or the size of the pattern being too large for the memory etc.

The algorithm in the program is based on the gap pattern. It starts with the gap pattern for 1 =>{1,(1)\*}.  Note that 1 is not considered a prime, and so this pattern simply states that all numbers are candidate primes for 1.  
From this it divines pattern for the next prime (i.e. next prime = 1+the first term in the pattern which is 1+1=2). The pattern is determined by expanding the pattern using the prime factorial (i.e. 2*1 =2 and the modVattam theorem) and it is {1,(2)\*}.  
It continues to find the next prime and its pattern...

To Validate the program, a routine to find the prime numbers below N has been coded which utilizes this prime gapper method.  This result is then compared to the published results for primes under N


# Usage
Download the repo and:  
python primeGapper.py <N> #give the patterns and the primes below N.  
ex: python primeGapper.py 100  
<b>Output</b>:  
INFO - There are 25 primes below 100:  
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

# Some details:  
In the pattern form: {a,(b,c,d,e,..)*} for prime p, we can derive the next pattern as:  
The next prime = p+a  
In b,c,d,e,.. remove the element that is a multiple of p+a. The first element is b (or p+a+b). 
(p+a+b) mod (p+a) = b (assume that b < p+a).  Now the element b repeats after pf(p).  Since p+a is not a factor  
of pf(p) we can apply the modVattam theorem (mod circle) and find the occurence of b where the mod is zero (i.e. it is  
divisible by p+a). There will be only one occurence in the periodic pattern for p+a. That occurence can be eliminated.  
The same is done for all b,c,d,e.. and the new pattern can be derived.

# Onward to conjectures...

The modVattam theorem and a circular shift of the repeating pattern gives us a way of deriving the next pattern for cp's (i.e. candidate primes):
2 => {1,(2)\*} (to reiterate, the cp's for 2 are 3,5,7,9..)
3 => {2,(2,4)*}.. To derive this the method is to look at the two parts: The first number and the repeating part.  
a. The first number is simpley 'shift left' which is bump off the 1 and the next number 2 moves into its place.  
so now we have 3 => {2,(2)\*}
b. We know that the sum of the repeating part should be 2*3 = 6 for the prime 3. So expand the (2)\* to (2,2,2)\*
c. These (2,2,2) represent the cp's 3+2+2, 3+2+2+2, 3+2+2+2+2 = 7,9,11 and the number 9 is divisible by 3. So that can be eliminated, which makes the gap 2+2=4.  
so 3 => {2,(2,4)*}

The primeGapper program does these steps and produces the interesting printouts.  
To get the next pattern for prime p+1 we just shift left and repeat the previous pattern as indicated above.  This can be written like a inductive relation:
patt(p+1) = f(patt(p))  and patt(2) = [1,(1)\*]   
In the printout below '-01' under pattern means that the element has been removed. Corresponding to that the prime is shown as '000'.  

The formula for the number of terms in the pattern is:  
nt(p) = nt(p-1)*p - nt(p-1)
Ex: nt(3) = nt(2)*3 - nt(2) = 1\*3 -1 =2
Ex: nt(5) = nt(3)*5 - nt(3) = 10-2 = 8



Here are the interesting printouts from the primeGapper:

INFO - Pattern for prime: 2, length of pattern= 2  
INFO - [1, (1)\*]  
INFO - p = 2, sp: len = 1, ngp = 1, idxToDelete: [1]  
INFO - pattern line => corresponding primes:  
INFO - ['002'] => ['005']  
INFO - ['-01'] => ['000']  
INFO - Pattern for prime: 3, length of pattern= 2  
INFO - [1, (2)\*]  
INFO - p = 3, sp: len = 1, ngp = 2, idxToDelete: [2]  
INFO - pattern line => corresponding primes:  
INFO - ['002'] => ['007']  
INFO - ['004'] => ['011']  
INFO - ['-01'] => ['000']  
INFO - Pattern for prime: 5, length of pattern= 3  
INFO - [2, (2, 4)*]  
INFO - p = 5, sp: len = 2, ngp = 2, idxToDelete: [9, 6]  
INFO - pattern line => corresponding primes:  
INFO - ['004', '002'] => ['011', '013']  
INFO - ['004', '002'] => ['017', '019']  
INFO - ['004', '006'] => ['023', '029']  
INFO - ['-01', '002'] => ['000', '031']  
INFO - ['006', '-01'] => ['037', '000']  



