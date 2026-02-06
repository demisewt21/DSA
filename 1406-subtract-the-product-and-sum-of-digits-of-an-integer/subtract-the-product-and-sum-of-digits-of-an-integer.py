class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sum  = 0
        for digit in str(n):
            value = int(digit)
            product *= value
            sum += value
        return product - sum


        