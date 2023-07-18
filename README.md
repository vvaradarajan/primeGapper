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
pf(5) = all primes 5 and below multiplied = 2x3x5 = 30 => pattern is {2,(4,2,4,2,4,6,2,6)\*} and the repeating portion adds to 2+4=6 

## On To The Program
The primeGapper process described about is related to the 'Eratothesnes Sieve'.  
The program finds the patterns starting from 1 (special prime, that does not divide anything) and continues with the next prime and so on.  
It is in Python using normal python integers and works upto about 31.  The failure after that is probably due to number overflow or the size of the pattern being too large for the memory etc.


