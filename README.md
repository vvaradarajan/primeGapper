# primeGapper
Explores gaps between primes
The gaps between primes seems to follow a continuously changing pattern and this repo is to explore that pattern. The exact details of that pattern are in a different document and the reader is asked to accept the examples below so that we can quickly get to the program:  

## Examples:
Taking the first prime as 2: Pattern = {1,(2)\*} . The (2)\* is a continuing sequence of 2's.  
Using this pattern the next primes are: 2+1 = 3, 3+2 = 5, 5+2 = 7, ..9, 11, 13 ...  
Here '9' is not a prime, and so we have to create a new pattern by including the number 3 as a prime..
Taking 2 and 3 as primes: Pattern = {2,(2,4)\*} => 5,7,11,13,17,19,23...  
### Important discovery:  
The repeating portion of the pattern adds up to 'prime factorial'.  For example:  
pf(2) = all primes 2 and below multiplied = 2 => pattern is {1,(2)\*} and the repeating portion adds to 2  
pf(3) = all primes 3 and below multiplied = 2x3 = 6 => pattern is {2,(2,4)\*} and the repeating portion adds to 2+4=6  
pf(5) = all primes 5 and below multiplied = 2x3x5 = 30 => pattern is {2,(4,2,4,2,4,6,2,6)\*} and the repeating portion adds to  
4+2+4+2+4+6+2+6 = 30.

## On To The Program
The primeGapper process described about is related to the 'Eratothesnes Sieve'.  
The program finds the patterns starting from 1 (special prime, that does not divide anything) and continues with the next prime and so on.  
It is in Python using normal python integers and works upto about 31.  The failure after that is probably due to number overflow or the size of the pattern being too large for the memory etc.

# Usage
Download the repo and:  
python primeGapper.py <N> #give the patterns and the primes below N.  
ex: python primeGapper.py 100

# Advanced Info
In the pattern form: {a,(b,c,d,e,..)*} for prime p, we can derive the next pattern as:  
The next prime = p+a  
In b,c,d,e,.. remove the element that is a multiple of p+a. The first element is b (or p+a+b). 
(p+a+b) mod (p+a) = b (assume that b < p+a).  Now the element b repeats after pf(p).  Since p+a is not a factor  
of pf(p) we can apply the modVattam theorem (mod circle) and find the occurence of b where the mod is zero (i.e. it is  
divisible by p+a). There will be only one occurence in the periodic pattern for p+a. That occurence can be eliminated.  
The same is done for all b,c,d,e.. and the new pattern can be derived.

The modVattam theorem is that the mode goes thru all possible numbers for m and n where m and n have no common factors as m  
goes from m ... nm. Example: 2 and 3 => mods are 2%3=2, 4%3=1 6%3=0.  The method of its application here is (p+a+b)%(p+a) which is  
b, (p+a+b+pf(p))%(p+a) = 




