# primeGapper
Explores gaps between primes
The gaps between primes seems to follow a continuously changing pattern and this repo is to explore that pattern. The exact details of that pattern are in a different document and the reader is asked to accept the examples below so that we can quickly get to the program:  

## Preamble
Candidate Primes are number that are not divisible by any prime <= P
Ex: p=2 => candidate primes are 3,5,7,9..; p=3 => 5,7,11,13,17,19,23..

## Hypothesis
The hypothesis is Candidate Primes follow a 'gap' pattern:  
cp(p) = p+a+(c,d,e,f..)\* (*=the pattern enclosed in brackets repeats).  
g(p) = cp - p = a+(c,d,e,f..)\* where g(p) is the gap between primes
Ex: g(2) = 1+(2)* = 1,2,2,..=> cp(2) = 3,5,7,9..


1.  cp(p1) is a subset of cp(p) for p1 > p (i.e. cp(p) = numbers not divisible by primes upto p, and cp(p1) = number not divisible by primes upto P AND number not divisible by primes upto P1)  


## Examples:
Taking the first prime as 2: The prime gap function is g(2) = {1,(2)\*} . The (2)\* is a continuing sequence of 2's and is the repeating part. The repeating part adds up to 2 = pf(2)  

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
It is in Python using normal python integers and works upto about 31.  The failure after that is probably due to number overflow or the size of the pattern being too large for the memory etc.

The algorithm in the program is based on the gap pattern. It starts with the gap pattern for 1 =>{1,(1)\*}.  Note that 1 is not considered a prime, and so this pattern simply states that all numbers are candidate primes for 1.  
From this it divines pattern for the next prime (i.e. next prime = 1+the first term in the pattern which is 1+1=2). The pattern is determined by expanding the pattern using the prime factorial (i.e. 2*1 =2 and the modVattam theorem) and it is {1,(2)\*}.  
It continues to find the next prime and its pattern...

To Validate the program, a routine to find the prime numbers below N has been coded which utilizes this prime gapper method.  This result is then compared to the published results for primes under N


# Usage
Download the repo and:  
python primeGapper.py <N> #give the patterns and the primes below N.  
ex: python primeGapper.py 100  
<b>Output<b>:  
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





