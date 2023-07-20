#Program usess erasmus sieve to find the Gaps between prime numbers

import math,sys
import logging
import logging.config

logging.config.fileConfig('logging.conf')
logger = logging.getLogger('simpleExample')


class PrimeGapper:

    def __init__(self):

        self.repeatPeriod = 1
        self.primes=[]
        logger.info(f'PrimeGapper Version 1.0')

    def updatePrParams(self,npr,reset=False):
        #add a new prime (npr)
        if reset:
            self.repeatPeriod = 1
            self.primes=[] 
        else:       
            self.primes.append(npr)
            self.repeatPeriod = self.repeatPeriod*npr

    def getGaps(self,startPr,pattern):
        #calculate the new values
        nextPrime=startPr+pattern[0]
        self.updatePrParams(nextPrime)
        #Algorithm to get the next pattern:
        #1. Expand the existing pattern to cover the new repeatPeriod
        #2. In the expanded pattern remove the numbers that are divisible by the new prime
        # These will be (nextPrime^2), nextPrime*(nextPrime+gap1), (nextPrime*(nextPrime+gap1+gap2..)) 
        #1.
        repPart=pattern[1:]
        repSum= sum(repPart)
        repTimes = math.ceil(self.repeatPeriod/repSum)
        tPattern=[]
        for i in range(repTimes):tPattern.extend(repPart)

        # 2. eliminate to derive new pattern
        acc = nextPrime
        np2 = nextPrime*nextPrime
        idxToEliminate=[]
        ngp = 0
        npPlus=nextPrime
        for idx in range(len(tPattern)):
            acc +=tPattern[idx]
            if acc == np2:
                idxToEliminate.append(idx)
                #Find the next np2 (a guess)
                npPlus +=tPattern[ngp]
                np2= nextPrime*npPlus
                ngp +=1
            else: continue
        #2 The cells to be removed are marked with a -1 and then all -1's are removed
        for dIdx in idxToEliminate:
            if dIdx==len(tPattern) -1:
                tPattern[dIdx] += tPattern[0]
            else:
                tPattern[dIdx] +=tPattern[dIdx+1]
                tPattern[dIdx+1]=-1 #marker means to remove
        #logger.info(f'nextPrime: {nextPrime}, repeatPeriod = {repeatPeriod}; nPattern= {tPattern}')
        tPattern = [g for g in tPattern if g>0]

        return nextPrime,tPattern
    
    def printPattern(self,pr,patt):
        #print using a format like [1,(n,n2..)*]
        logger.info(f'Pattern for prime: {pr}, length of pattern= {len(patt)}')
        if logger.level == logging.DEBUG or len(patt)<=5:
            part2= f'{patt[1:]}'
        else: part2=f'{patt[1:4]}..'
        part2=part2.replace('[','').replace(']','')    

        logger.info(f'[{patt[0]}, ({part2})*]')

    def findPrimesBelowN(self,N):
        #Algorithm:
        #1. Find the candidate primes for the lowest P where P > sqrt(N)
        #2. Count the candidate primes below N (and add the number of primes before P)
        primes=[]
        nxtp,newp=1,[1,1]
        lowestP = math.ceil(math.sqrt(N))
        logger.info(f'lowestP = {lowestP}')

        while True:
            nxtp,newp=self.getGaps(nxtp,newp)
            self.printPattern(nxtp,newp)
            primes.append(nxtp)
            if nxtp > lowestP: break
        #accumulate the candidate primes less than N into primes
        acc=nxtp
        for g in newp:
            acc +=g
            if acc > N: break
            primes.append(acc)
        logger.info(f'There are {len(primes)} primes below {N}:\n{primes}')

#test routines to test the class
def test(t):
    tc = PrimeGapper()
    match t:
        case 1:
            args = sys.argv
            logger.info(f'args={args}')
            if len(args)>= 2: N= int(args[1])
            else: N=100
            tc.findPrimesBelowN(N)

        case 3:
            pattern=[1,1]
            pr = 1
            #find gap pattern for first 5 primes
            nxtp,newp = tc.getGaps(1,pattern)
            nxtp,newp = tc.getGaps(nxtp,newp)
            nxtp,newp = tc.getGaps(nxtp,newp)
            nxtp,newp = tc.getGaps(nxtp,newp)
            nxtp,newp = tc.getGaps(nxtp,newp)
            nxtp,newp = tc.getGaps(nxtp,newp)

test(1)

