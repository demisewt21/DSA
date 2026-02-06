'''
The smallest positive integer that is a multiple of 2 and n means their LCM
LCM(2,n) = 2*n/(gcd(2,n))
if n is even, gcd(2,n) = 2 then LCM(2,n) = n
if n is odd, gcd(2,n) = 1 then LCM(2,n) = 2n   

'''


class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
            product = 2*n
            if n%2 == 0:
                print(f"The smallest positive integer that is a multiple of both 2 and {n} is {n}")
                return n
            else:
                 print(f"The smallest positive integer that is a multiple of both 2 and {n} is {product}")
                 return product
    

    
        