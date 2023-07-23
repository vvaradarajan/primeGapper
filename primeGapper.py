#Program usess erasmus sieve to find the Gaps between prime numbers

import math,sys
import logging
import logging.config

logging.config.fileConfig('./logging.conf')
logger = logging.getLogger('./simpleExample')


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
            rp = 1
            for p in self.primes: rp=rp*i
            self.repeatPeriod = rp

    def getGapsNew(self,startPr,pattern):        
        #calculate the new values
        nextPrime=startPr+pattern[0]
        self.updatePrParams(nextPrime)
        #Algorithm to get the next pattern:
        #1. Expand the existing pattern to cover the new repeatPeriod
        #2. In the expanded pattern remove the numbers that are mod 0 for the new prime:
        #2a. Create a table of circular mods of old repeatPeriod with the new prime
        #2b. Find where each term in the old repeatPeriod has a mod 0. Mark this to be 'removed' in the expanded pattern
        #3. Collapse the expanded pattern to get the new pattern
        # These will be (nextPrime^2), nextPrime*(nextPrime+gap1), (nextPrime*(nextPrime+gap1+gap2..)) 
        #1.
        repPart=pattern[2:]
        repPart.append(pattern[1])
        repSum= sum(repPart)
        repTimes = math.ceil(self.repeatPeriod/repSum)
        tPattern=[]
        for i in range(repTimes):tPattern.extend(repPart)
        #2a: create the modVattam table
        mv=[0]
        for i in range(repTimes):
            mv[i] = i*repSum % nextPrime
        



    def getGaps(self,startPr,pattern):
        def eliminate(patt,idxToEliminate):
            #2 The cells to be removed are marked with a -1 and then all -1's are removed
            for dIdx in idxToEliminate:
                if dIdx==len(patt) -1:
                    patt[dIdx] += patt[0]
                else:
                    patt[dIdx] +=patt[dIdx+1]
                    patt[dIdx+1]=-1 #marker means to remove
            #logger.info(f'nextPrime: {nextPrime}, repeatPeriod = {repeatPeriod}; nPattern= {patt}')
            return [g for g in patt if g>0]
        
        def getExpandedPattern(p,pattern):
            #returns the next prime and the expanded pattern
            nxtp=p+pattern[0]
            nxtGap = pattern[1]
            repPart = pattern[2:]
            repPart.append(nxtGap)
            nxtPattern=[nxtGap]
            for i in range(nxtp):nxtPattern.extend(repPart)
            return nxtp,repPart,nxtPattern
        
        def createMvd(p,sp,ep):
            #crate the modVattam distance for each cp in ep
            #p=prime, sp=sub pattern (ex: for 5 it is 4,2)
            sSp = sum(sp)
            lSp = len(sp)
            xv = ep[0]
            mv={}
            idxToDelete=[]
            for idx,cp in enumerate(sp):
                #if cp in mv: continue
                xv +=cp
                t1=xv % p
                #now find occurence where t1 =0. occurrence = t1+n*sum(sp)
                n=0
                while True:
                    if t1==0:
                        mv[idx]=n
                        idxToDelete.append(n*lSp+idx+1)

                        break
                    else: 
                        t1 +=sSp
                        t1 = t1 % p
                        n +=1
            #print(f'mv={mv}, sSp={sSp}, idxToDelete={idxToDelete}')
            patt = eliminate(ep,idxToDelete)
            #self.printPattern(p,patt)
            return p,patt
            #create the idx to delete

        p,sp,patt = getExpandedPattern(startPr,pattern)
        return createMvd(p,sp,patt)


        #pattern test
        p,sp,patt = getExpandedPattern(3,[2,2,4])
        self.printPattern(p,patt)
        #createMvdTest
        
        createMvd(p,sp,patt)
        exit(0)


    def printPattern(self,pr,patt):
        #print using a format like [1,(n,n2..)*]
        lp = 60 #print upto here and then ...
        logger.info(f'Pattern for prime: {pr}, length of pattern= {len(patt)}')
        if logger.level == logging.INFO or len(patt)<=10:
            part2= f'{patt[1:]}'
        else: part2=f'{patt[1:lp]}..'
        part2=part2.replace('[','').replace(']','')    

        logger.info(f'[{patt[0]}, ({part2})*]')

    def findPrimesBelowN(self,N):
        #Algorithm:
        #1. Find the candidate primes for the lowest P where P > sqrt(N)
        #2. Count the candidate primes below N (and add the number of primes before P)
        primes=[]
        nxtp,newp=1,[1,1]
        lowestP = math.floor(math.sqrt(N))
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

