class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=2:
            return 0
        primes=[True]*n
        count=0
        primes[0]=primes[1]=False
        for i in range(2,n):
            if primes[i]==True:
                count+=1
            for j in range(i*i,n,i):
                primes[j]=False
        return count